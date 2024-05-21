# Recommendation System using Apriori Algorithm

This project implements a recommendation system using both the Apriori algorithm for frequent itemset mining and association rule generation, as well as collaborative filtering for personalized recommendations.

## Introduction

The goal of this recommendation system is to suggest relevant products to users based on their past purchase history. It utilizes the Apriori algorithm to discover frequent itemsets from transaction data and generate association rules, alongside collaborative filtering techniques to enhance recommendation accuracy.

## Installation

To set up the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Ubeydkhoiri/recommender-system-using-apriori.git

    # move to the directory
    cd recommender-system-using-apriori
    ```

2. Create your virtual environtment:

    ```bash
    python -m venv venv_name

    # activate your virtual envirotnment
    venv_name\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the recommendation system:

    ```bash
    streamlit run app.py
    ```

## Result Example
Below is an example of the recommendation system's output after running `app.py`:

![Result Example](result-example.png)