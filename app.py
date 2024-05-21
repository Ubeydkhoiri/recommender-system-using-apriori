import joblib
import streamlit as st
import pandas as pd
from pathlib import Path

# Define the parent directory path
PARENT_PATH = Path(__file__).resolve().parent


# Load datasets
product_details_df = pd.read_csv(PARENT_PATH / 'dataset/product_details.csv')
product_details_df['Details'] = product_details_df['Product ID'].astype(str) + ' (' \
                                +  product_details_df['Category'] + ' ' \
                                '$' + product_details_df['Price'].astype(str) + ')'

# Load association rules
rules = joblib.load('rules.joblib')

def fetch_image(product_id):
    """Fetches the image path for a given product ID."""
    image_path = f"images/{product_id}.png"
    return image_path

def recommend_products(product_id, num_recommendations=10):
    """Recommends products based on a given product ID."""
    related_products = rules[(rules['antecedents'] == frozenset({product_id}))]
    related_products_sorted = related_products.sort_values(by='lift', ascending=False)
    related_products_sorted = related_products_sorted['consequents'].apply(lambda x: list(x))
    recommended_products = related_products_sorted.values[0]
    for list_product in related_products_sorted:
        for product in list_product:
            if product not in recommended_products:
                recommended_products.append(product)
            if len(recommended_products) > num_recommendations:
                recommended_products = recommended_products[:10]
                break
    return recommended_products

def recommend(product_id):
    """Generates recommendations for a given product ID."""
    recommended_products = recommend_products(product_id)
    product_names = []
    product_images = []
    for product_id in recommended_products:
        product_info = product_details_df[product_details_df['Product ID'] == product_id]
        image = fetch_image(product_info['Product ID'].values[0])
        product_names.append(product_info['Category'].values[0])
        product_images.append(image)

    return product_names, product_images


def main():
    """Main function to run the Streamlit app."""
    st.header('Product Recommender System')

    product_list = product_details_df['Details'].values
    selected_product = st.selectbox(
        "Type or select a movie from the dropdown",
        product_list
    )

    if st.button('Show Recommendation'):
        selected_product_id = int(selected_product.split(' ')[0])
        recommended_product_names, recommended_product_images = recommend(selected_product_id)

        # Display text explaining user choice
        st.write(f"You choose this product")
         # Display example result image
        st.image(fetch_image(selected_product_id), caption=f"Product ID {selected_product_id}", use_column_width=True)

        # Display text explaining user choice
        st.write(f"You may like these product")
        # Display recommended products
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text(recommended_product_names[0])
            st.image(recommended_product_images[0])
        with col2:
            st.text(recommended_product_names[1])
            st.image(recommended_product_images[1])
        with col3:
            st.text(recommended_product_names[2])
            st.image(recommended_product_images[2])

        col4, col5, col6 = st.columns(3)
        with col4:
            st.text(recommended_product_names[3])
            st.image(recommended_product_images[3])
        with col5:
            st.text(recommended_product_names[4])
            st.image(recommended_product_images[4])
        with col6:
            st.text(recommended_product_names[5])
            st.image(recommended_product_images[5])

if __name__ == "__main__":
    main()