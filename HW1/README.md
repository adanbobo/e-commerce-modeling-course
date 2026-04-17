#  E-Commerce Models – Influence Maximization

This repository contains my solution for **Homework 1** in the course
**"Models for Electronic Commerce"**.


grade: 99/100
---

##  Project Overview

This project models an **influence maximization problem** in a social network within an e-commerce context.

A fashion company (**Praducci**) aims to promote its products through a social platform (**NoseBook**) by selecting a group of **initial influencers**. The goal is to maximize the number of users who adopt the product through a probabilistic spread process.

---

##  Objective

Select a set of initial influencers under a budget constraint such that the **expected number of influenced users after 6 rounds is maximized**.

---

##  Methodology

* Represent the social network as a graph:

  * Nodes → users
  * Edges → social connections

* Model influence spread using a **stochastic process**

* Consider:

  * Influencer costs (budget constraint)
  * Presence of **negative influencers ("haters")**
  * Probabilistic propagation between neighbors

* Evaluate performance using simulations and expected influence spread

---

## 📂 Repository Structure

```
HW1/
├── hw1_code.py     # Implementation of the solution
├── hw1_report.pdf      # Explanation of approach and methodology
└── README.md
```

---

##  Note on Data & Provided Files

> The dataset files (CSV) and simulation code provided in the assignment are **not included** in this repository, as they are part of the official course materials.

---

##  Technologies Used

* Python
* NumPy
* NetworkX
* Pandas

---

##  Key Highlights

* Applied graph-based modeling to a real-world marketing problem
* Designed a strategy for selecting cost-effective influencers
* Handled uncertainty using probabilistic simulations
* Analyzed the impact of negative influence in networks



##  Summary

This project demonstrates the application of **network theory, probabilistic modeling, and simulation techniques** to solve a complex optimization problem in e-commerce.

---
