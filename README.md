# Recommendation System using Apriori Algorithm

This project implements a recommendation system using the Apriori algorithm for frequent itemset mining and association rule generation.

## Introduction

The recommendation system aims to suggest relevant products to users based on their past purchase history. It utilizes the Apriori algorithm to discover frequent itemsets from transaction data and generate association rules to make recommendations.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/recommendation-system.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the recommendation system:

    ```bash
    python recommendation_system.py
    ```

## Usage

To recommend products using the Apriori algorithm, you can use the `recommend_products_apriori()` function provided in `recommendation_system.py`. Here's how to use it:

```python
from recommendation_system import recommend_products_apriori

# Generate recommendations for a given product ID
recommendations = recommend_products_apriori(product_id='123456', num_recommendations=5)
print("Recommended products:", recommendations)
