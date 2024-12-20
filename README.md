# ai-driven-hospitality
This repository contains a Restaurant Customer Feedback Dataset that simulates customer interactions, feedback, and preferences for a restaurant. The dataset includes a range of details, including feedback sentiment (positive, neutral, and negative), customer information, feedback specifics, and additional preferences related to dining, room choices, wellness, and more.

Table of Contents
Overview
Dataset Structure
Columns Description
Feedback Sentiments
How to Use the Dataset
License
Overview
The dataset simulates restaurant feedback, including customer interactions, ratings, and detailed feedback about dining experiences, stay duration, and preferences. It is designed to assist in the development and testing of recommendation systems, sentiment analysis, or customer service automation in the restaurant industry.

The dataset is created with the help of the Faker library, and it generates over 2300 rows of realistic customer feedback, providing varied data points that can be used for machine learning, statistical analysis, or other data-driven applications.

Dataset Structure
The dataset is structured as a CSV file with the following columns. It contains both categorical and numerical data related to restaurant customer experiences, ensuring a comprehensive dataset for a variety of use cases.

The dataset has 2300 rows, each representing a simulated feedback entry for a customer at a restaurant.

Columns Description
Customer Name

Type: Text
Description: A randomly generated name for the customer.
cust mail id

Type: Text
Description: A randomly generated email address for the customer.
Feedback

Type: Text
Description: A detailed feedback statement generated from three categories: Positive, Neutral, and Negative.
Date and time

Type: Datetime
Description: A timestamp of when the feedback was provided. All timestamps are in Indian Standard Time (IST), and the dates are randomly generated within the past year.
caretaker/server name

Type: Text
Description: A randomly generated name of the server or caretaker who attended the customer.
care-empid

Type: Text
Description: A randomly generated employee ID for the caretaker/server.
cust-age

Type: Integer
Description: The age of the customer, randomly selected between 18 and 70.
cust-contact

Type: Text
Description: A randomly generated phone number for the customer.
sentiment - future

Type: Categorical (Positive/Neutral/Negative)
Description: The sentiment regarding a future visit to the restaurant. The values are selected randomly between "Positive", "Neutral", and "Negative".
dept

Type: Categorical
Description: The department associated with the customer or their service experience. Options include "HR", "Sales", "Support", "Finance", and "Engineering".
customer-stay duration
Type: Integer
Description: The duration (in days) of the customer's stay at the restaurant, selected randomly between 1 and 30 days.
customer-n visits past
Type: Integer
Description: The number of times the customer has visited the restaurant in the past, randomly chosen between 0 and 10.
customer-membership status
Type: Categorical
Description: The membership status of the customer. Options include "Active" and "Inactive".
customer-amt to be paid
Type: String
Description: The amount the customer needs to pay, randomly generated between $50 and $500.
NPS (Net Promoter Score)
Type: Integer
Description: A score indicating the customer's likelihood to recommend the restaurant, randomly selected between 1 and 10.
Dining - Vegetarian/vegan
Type: Categorical
Description: The customer's dining preference. Options include "Vegetarian", "Vegan", and "Non-Vegetarian".
Room preference
Type: Categorical
Description: The customer's preferred room type (if applicable). Options include "Deluxe", "Standard", and "Suite".
Sports activities - [table tennis, golf, ...]
Type: Categorical
Description: The type of sports activity the customer prefers. Options include "Table tennis", "Golf", "Swimming", and "Badminton".
Wellness - gym, sauna, massage
Type: Categorical
Description: The customer's preferred wellness service. Options include "Gym", "Sauna", and "Massage".
pricing patterns - frugal/luxury
Type: Categorical
Description: The customer's pricing preference. Options include "Frugal" and "Luxury".
Feedback Sentiments
Positive Feedback
Examples of positive feedback include statements like:
"The dining experience was absolutely amazing! The staff were friendly, the food was served hot, and the flavors were exceptional."
"I had a wonderful time at the restaurant. The ambiance was cozy, the service was prompt, and the chef even came out to greet us."
Neutral Feedback
Neutral feedback represents an average or mixed experience:
"The food was good, but it took quite a while to arrive. The staff were courteous, but the restaurant was a bit too crowded for my taste."
"The dining was okay. Nothing too extraordinary, but the staff were polite, and the restaurant was clean."
Negative Feedback
Negative feedback reflects poor customer experiences:
"The restaurant failed to meet basic expectations. The staff seemed inattentive, and the dishes lacked seasoning."
"Unfortunately, the dining experience was below par. The pasta was soggy, the soup was bland, and the waiter forgot one of our orders."
