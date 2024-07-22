import pandas as pd
# Load the drug-review dataset
df = pd.read_csv("drug.csv")
def get_reviews(drug_name):
 # Filter the dataset for the given drug name
 filtered_df = df[df['drugName'].str.lower() == drug_name.lower()]
 # Get the required columns: condition, rating, review, and useful count
 conditions = filtered_df['condition']
 ratings = filtered_df['rating']
 reviews = filtered_df['review']
 useful_counts = filtered_df['usefulCount']
 return conditions, ratings, reviews, useful_counts
# Prompt the user to input a drug name
drug_name = input("Enter a drug name: ")
# Get the reviews for the specified drug name
conditions, ratings, reviews, useful_counts = get_reviews(drug_name)
if len(conditions) > 0:
 # Print the information for each review
 print(f"Reviews for '{drug_name}':")
 for condition, rating, review, useful_count in zip(conditions, ratings, reviews, useful_counts):
 if rating > 5:
 print(f"Condition: {condition}")
 print(f"Rating: {rating}")
 print(f"Rating: good")
 print(f"Review: {review}")
 print(f"Useful Count: {useful_count}")
 print("====================")
 elif rating == 5:
 print(f"Condition: {condition}")
 print(f"Rating: {rating}")
 print(f"Rating: Average")
 print(f"Review: {review}")
 print(f"Useful Count: {useful_count}")
 print("====================")
 elif rating <5:
 print(f"Condition: {condition}")
 print(f"Rating: {rating}")
 print(f"Rating: bad")
 print(f"Review: {review}")
 print(f"Useful Count: {useful_count}")
 print("====================")
else:
 print(f"No reviews found for '{drug_name}'.")
