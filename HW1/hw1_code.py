import random
import numpy as np
import networkx as nx
from praducci_simulation import read_graph, read_haters, read_costs, simulate_influence, submit_influencers

# קבועים
BUDGET = 1500
ID1 = '325468510'
ID2 = '213690928'
FILENAME = f'{ID1}_{ID2}.csv'

def select_candidates_from_cluster(cluster, valid_users, costs, degree_centrality, betweenness_centrality, top_n=2):
    filtered = [u for u in cluster if u in valid_users and costs[u] <= 100]
    sorted_users = sorted(
        filtered,
        key=lambda u: 0.6 * degree_centrality[u] + 0.4 * betweenness_centrality[u],
        reverse=True
    )
    return sorted_users[:top_n]

def get_initial_candidates(communities, valid_users, costs, degree_centrality, betweenness_centrality):
    initial_candidates = []
    for cluster in communities:
        candidates = select_candidates_from_cluster(
            cluster, valid_users, costs, degree_centrality, betweenness_centrality
        )
        initial_candidates.extend(candidates)
    return initial_candidates

def greedy_selection(initial_candidates, graph, costs, haters):
    selected = []
    total_cost = 0
    best_score = 0

    for user in initial_candidates:
        cost = costs[user]
        if total_cost + cost > BUDGET:
            continue
        temp_group = selected + [user]
        score = simulate_influence(graph, temp_group, haters)
        if score > best_score:
            selected.append(user)
            total_cost += cost
            best_score = score

    return selected

def get_neighbor(current, valid_users, costs):
    new = current[:]
    if len(new) > 1:
        new.remove(random.choice(new))
    budget_left = BUDGET - sum(costs[u] for u in new)
    options = [u for u in valid_users if u not in new and costs[u] <= budget_left]
    if options:
        new.append(random.choice(options))
    return new

def simulated_annealing(start_group, graph, haters, valid_users, costs, temp_start=100, cooling=0.95):
    best = start_group[:]
    best_score = simulate_influence(graph, best, haters)
    current = best[:]
    current_score = best_score
    temperature = temp_start

    while temperature > 1:
        neighbor = get_neighbor(current, valid_users, costs)
        neighbor_score = simulate_influence(graph, neighbor, haters)

        if neighbor_score > current_score or random.random() < np.exp((neighbor_score - current_score) / temperature):
            current = neighbor
            current_score = neighbor_score
            if neighbor_score > best_score:
                best = neighbor
                best_score = neighbor_score

        temperature *= cooling

    return best, best_score

if __name__ == '__main__':
    random.seed(42)
    np.random.seed(42)

    # קריאה
    graph = read_graph()
    haters = read_haters()
    costs = read_costs()

    # סינון
    valid_users = [node for node in graph.nodes if node not in haters and node in costs]

    # מדדי מרכזיות
    degree_centrality = nx.degree_centrality(graph)
    betweenness_centrality = nx.betweenness_centrality(graph, k=100, seed=1)

    # קהילות
    communities = list(nx.community.greedy_modularity_communities(graph))

    # בחירת מועמדים וגרידיאני
    initial_candidates = get_initial_candidates(communities, valid_users, costs, degree_centrality, betweenness_centrality)
    initial_group = greedy_selection(initial_candidates, graph, costs, haters)

    # שיפור עם Simulated Annealing
    best, best_score = simulated_annealing(initial_group, graph, haters, valid_users, costs)

    # שמירה
    submit_influencers(best, ID1, ID2, costs, haters, filename=FILENAME)

