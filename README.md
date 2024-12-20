# ai-driven-hospitality

Restaurant Customer Feedback Dataset
This repository contains a simulated Restaurant Customer Feedback Dataset. The dataset includes customer feedback, preferences, and other relevant details, created using Python's Faker library to generate realistic data for various restaurant customer interactions.

Table of Contents
Overview
Steps to Create the Dataset

Overview
This dataset simulates restaurant feedback and customer preferences. It includes over 2300 rows of data with various customer experiences (positive, neutral, and negative), along with other customer-related information such as age, contact details, feedback timestamps, and dining preferences. The dataset is designed for use in data analysis, sentiment analysis, and customer experience modeling.

Steps to Create the Dataset

The dataset was generated using the following steps:

Importing Libraries: The necessary libraries, such as csv, random, and Faker, were imported. The Faker library was used to generate fake names, emails, phone numbers, and other data fields.

Defining the Columns: A list of columns was defined, including customer details (name, email, contact), feedback specifics (feedback content, sentiment), and customer preferences (dining, room type, wellness, etc.).

Defining Feedback Categories: Three categories of feedback (positive, neutral, and negative) were defined. Each category contained multiple pre-written feedback examples to simulate various customer experiences.

Generating Random Data: A function generate_random_row was created to generate a random row of data. For each row, random values were chosen for:

Customer details (name, email, contact)
Feedback sentiment (chosen randomly from positive, neutral, negative feedback)
Additional customer preferences (dining, room, wellness, etc.)
Creating Data Rows: Using a list comprehension, 2300 rows of random data were generated, representing different customer feedback entries.

Writing the Data to CSV: The csv module was used to write the headers and data rows to a CSV file. The file was saved with the name restaurant_feedback_data.csv.

Date and Time Considerations: The date and time for each feedback entry were generated in Indian Standard Time (IST) to represent the feedback timestamp correctly for a restaurant in India.

