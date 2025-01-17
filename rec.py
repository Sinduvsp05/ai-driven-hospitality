# %%
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

import random

data = pd.read_csv("Sentiment_Analysis_data.csv")
data.fillna("", inplace=True)


# %%
print(data)

# %%
# Step 1: Generate User Data
import random
def generate_user_data(num_users=500, num_days=30):
    user_data = []

    # Define possible activities and their categories
    activities = {
        'amenities': ['pool', 'spa', 'gym', 'tennis_court', 'business_center'],
        'dining': ['main_restaurant', 'cafe', 'bar', 'room_service', 'buffet'],
        'activities': ['city_tour', 'beach_activity', 'cooking_class', 'yoga', 'golf']
    }

    # Generate random user interactions
    # start_date = datetime.now() - timedelta(days=num_days)

    for user_id in range(num_users):
        # User preferences (1-5 rating)
        for category in activities:
            for activity in activities[category]:
                # Not all users will have interactions with all activities
                
                    user_data.append({
                        'user_id': f'{user_id}',
                        'category': category,
                        'activity': activity,
                        'rating': random.randint(1, 5),
                    })

    return pd.DataFrame(user_data)

# %%
data = generate_user_data()
data

# %%
data.to_csv("recommendation_data.csv")

# %%
data[data['user_id'] == "user_0"]['activity'].value_counts()

# %%
# Step 2: Build User Profiles and Similarity Matrix
def build_user_profiles(data):
    
    # Create a user-activity matrix
    user_profiles = data.pivot_table(index='user_id', columns='activity', values='rating').fillna(0)

    # Compute similarity matrix using cosine similarity
    similarity_matrix = cosine_similarity(user_profiles)
    return similarity_matrix, user_profiles



# %%
print(data.head())


# %%
print(data['rating'].dtype)


# %%
similarity_matrix, user_profiles = build_user_profiles(data)
print(similarity_matrix)


# %%
user_profiles

# %%
import pandas as pd
import random
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 1: Generate User Data
def generate_user_data(num_users=500, num_days=30):
    
    user_data = []

    # Define possible activities and their categories
    activities = {
        'amenities': ['pool', 'spa', 'gym', 'tennis_court', 'business_center'],
        'dining': ['main_restaurant', 'cafe', 'bar', 'room_service', 'buffet'],
        'activities': ['city_tour', 'beach_activity', 'cooking_class', 'yoga', 'golf']
    }

    # Generate random user interactions
    for user_id in range(num_users):
        for category in activities:
            for activity in activities[category]:
                # Randomly decide if the user interacted with the activity
                if random.random() < 0.3:  # 30% chance of interaction
                    user_data.append({
                        'user_id': f'{user_id}',
                        'category': category,
                        'activity': activity,
                        'rating': random.randint(1, 5),
                    })

    return pd.DataFrame(user_data)

# Step 2: Build User Profiles and Similarity Matrix
def build_user_profiles(data):
  
    # Create a user-activity matrix
    user_profiles = data.pivot_table(index='user_id', columns='activity', values='rating').fillna(0)

    # Compute similarity matrix using cosine similarity
    similarity_matrix = cosine_similarity(user_profiles)
    return similarity_matrix, user_profiles

# Step 3: Find Similar Users
def get_similar_users(data, user_id, n=5, similarity_matrix=None):
    
    if similarity_matrix is None:
        similarity_matrix, user_profiles = build_user_profiles(data)

    user_profiles = data.pivot_table(index='user_id', columns='activity', values='rating').fillna(0)
    user_idx = user_profiles.index.get_loc(user_id)
    user_similarities = similarity_matrix[user_idx]

    # Get indices of the top `n` similar users (excluding the user itself).
    similar_user_indices = user_similarities.argsort()[::-1][1:n + 1]
    similar_users = user_profiles.index[similar_user_indices]

    return list(similar_users)

# Step 4: Generate Recommendations
def get_recommendations(data, user_id, n=5, similarity_matrix=None):
    
    if similarity_matrix is None:
        similarity_matrix, user_profiles = build_user_profiles(data)

    similar_users = get_similar_users(data, user_id, n=5, similarity_matrix=similarity_matrix)

    # Filter activities rated by similar users
    similar_users_data = data[data['user_id'].isin(similar_users)]

    # Calculate average ratings for activities
    recommendations = similar_users_data.groupby('activity').agg({
        'rating': 'mean'
    }).sort_values('rating', ascending=False)

    # Filter out activities the user has already tried
    user_activities = set(data[data['user_id'] == user_id]['activity'])
    new_activities = recommendations[~recommendations.index.isin(user_activities)]

    return new_activities.head(n)

# Step 5: User Interaction
if __name__ == "__main__":
    # Generate synthetic user data
    data = generate_user_data(num_users=100, num_days=30)

    # User input
    user_id = input("Enter your user ID (e.g., '0'): ")

    # Generate recommendations
    similarity_matrix, _ = build_user_profiles(data)
    recommendations = get_recommendations(data, user_id, n=10, similarity_matrix=similarity_matrix)

    # Output
    if recommendations.empty:
        print(f"No new recommendations available for User {user_id}.")
    else:
        print(f"Recommendations for User {user_id}:")
        print(recommendations)



