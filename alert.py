# %%
!pip install slack-sdk

# %%
from slack_sdk.webhook import WebhookClient
url="https://hooks.slack.com/services/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"

# %%
pip install groq

# %%
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# Email login credentials


SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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" # Replace with actual URL
client = Groq(api_key="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")  # Replace with your actual API key



# Function to analyze sentiment and extract areas
def sentiment_and_areas(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a sentiment analyzer that processes text and outputs a JSON object with the schema: "
                    f"{json.dumps({'Sentiment': 'Positive/Negative', 'Areas': []})}. "
                    "Provide the JSON output directly without any additional explanation."
                ),
            },
            {"role": "user", "content": f"Analyze this text: '{text}'."},
        ],
        model="llama3-8b-8192",
    )
    response_text = chat_completion.choices[0].message.content.strip()
    try:
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Received response: {response_text}")
        return {"Sentiment": "Unknown", "Areas": []}

# Function to generate suggestions
def suggestion_generator(sentiment_dict, text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a suggestion generator that provides actionable suggestions for areas mentioned. "
                    f"Output a JSON object with the schema: {json.dumps({'Area': 'Suggestion'})}."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Provide suggestions to improve the areas: {sentiment_dict['Areas']} based on the review: {text}."
                ),
            },
        ],
        model="llama3-8b-8192",
    )
    response_text = chat_completion.choices[0].message.content.strip()
    try:
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Received response: {response_text}")
        return {}

# Build user profiles and similarity matrix
def build_user_profiles(data):
    user_profiles = data.pivot_table(index="User_ID", columns="Activity", values="Rating").fillna(0)
    similarity_matrix = cosine_similarity(user_profiles)
    return similarity_matrix, user_profiles

# Get similar users
def get_similar_users(data, user_id, n=5, similarity_matrix=None):
    if user_id not in data["User_ID"].values:
        raise KeyError(f"User ID {user_id} not found in the data.")
    
    if similarity_matrix is None:
        similarity_matrix, user_profiles = build_user_profiles(data)
    
    user_profiles = data.pivot_table(index="User_ID", columns="Activity", values="Rating").fillna(0)
    user_idx = user_profiles.index.get_loc(user_id)
    user_similarities = similarity_matrix[user_idx]
    similar_user_indices = user_similarities.argsort()[::-1][1 : n + 1]
    similar_users = user_profiles.index[similar_user_indices]
    return list(similar_users)

# Generate recommendations
def get_recommendations(data, user_id, n=5, similarity_matrix=None):
    if similarity_matrix is None:
        similarity_matrix, user_profiles = build_user_profiles(data)
    similar_users = get_similar_users(data, user_id, n, similarity_matrix)
    user_profiles = data.pivot_table(index="User_ID", columns="Activity", values="Rating").fillna(0)
    similar_users_data = user_profiles[user_profiles.index.isin(similar_users)]
    similar_users_df = similar_users_data.mean(axis=0)
    unseen_activities = user_profiles.loc[user_id][user_profiles.loc[user_id] == 0].index
    recommended = similar_users_df[similar_users_df.index.isin(unseen_activities)].sort_values(ascending=False)
    return recommended.head(n).index.tolist()
\
# Email login credentials
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
email_user  =  "example@gmail.com"
email_password = "your_password"
subject="Review Alert"

# Function to send email notification
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl

# Function to send email notification
from email.message import EmailMessage
import smtplib
import ssl

# Function to send email notification
def send_email_notification(sender_email, sender_password, receiver_email, subject, body):
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Set the plain-text body content
    msg.set_content(body)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as sm:
            sm.login(sender_email, sender_password)
            sm.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")




# Process review and send Slack message
def process_review(user_id, review_text, to_email, n=5):
    sentiment_result = sentiment_and_areas(review_text)
    suggestions = suggestion_generator(sentiment_result, review_text)
    
    # Handling cases when suggestions might be empty or not in expected format
    # if not suggestions:
    #     suggestions_text = "No suggestions available."
    # else:
    #     suggestions_text = "\n".join(
    #         [f"• {area}: {suggestion}" for area, suggestion in suggestions.items()]
    #     )
    
    similarity_matrix, _ = build_user_profiles(data)
    recommendations = get_recommendations(data, user_id, n, similarity_matrix)

    message_text = (
        f"⚠ Review Alert for {user_id} ⚠\n\n"
        f"Review: {review_text}\n"
        f"Sentiment: {sentiment_result['Sentiment']}\n"
        f"Areas Mentioned: {', '.join(sentiment_result['Areas'])}\n"
        # f"Suggestions: {suggestions_text}\n"
        f"Recommended Activities: {', '.join(recommendations)}"
    )

    # Send Slack Message
    slack_message = {"text": message_text}
    response = requests.post(
        SLACK_WEBHOOK_URL, data=json.dumps(slack_message), headers={"Content-Type": "application/json"}
    )
    if response.status_code == 200:
        print("Message sent to Slack successfully!")
    else:
        print(f"Failed to send message to Slack. Status code: {response.status_code}")

    # Send Email Notification
    send_email_notification(email_user,email_password,to_email, f"Review Alert for {user_id}", message_text)


def send_slack_message(message):
    response = requests.post(
        SLACK_WEBHOOK_URL, data=json.dumps(message), headers={"Content-Type": "application/json"}
    )
    if response.status_code == 200:
        print("Message sent to Slack successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

# Main execution
if __name__ == "__main__":
    user_id = input("Enter User ID: ")
    review_text = input("Enter Review Text: ")
    to_email = "patlollasindu@gmail.com"
    # Ensure the user_id exists in the data
    try:
        slack_message = process_review(user_id, review_text,to_email)
        if slack_message:
            send_slack_message(slack_message)
    except KeyError as e:
        print(f"Error: {e}. Please check that the User ID exists in the dataset.")




