# ai-driven-hospitality

Restaurant Customer Feedback Dataset
This repository contains a simulated Restaurant Customer Feedback Dataset. The dataset includes customer feedback, preferences, and other relevant details, created using Python's Faker library to generate realistic data for various restaurant customer interactions.

Table of Contents

1.Overview

2.Steps to Create the Dataset

3.Columns Description

4.How to Use the Dataset

1.Overview

This dataset simulates restaurant feedback and customer preferences. It includes over 2300 rows of data with various customer experiences (positive, neutral, and negative), along with other customer-related information such as age, contact details, feedback timestamps, and dining preferences. The dataset is designed for use in data analysis, sentiment analysis, and customer experience modeling.

2.Steps to Create the Dataset

The dataset was generated using the following steps:

1)Importing Libraries: The necessary libraries, such as csv, random, and Faker, were imported. The Faker library was used to generate fake names, emails, phone numbers, and other data fields.

2)Defining the Columns: A list of columns was defined, including customer details (name, email, contact), feedback specifics (feedback content, sentiment), and customer preferences (dining, room type, wellness, etc.).

3)Defining Feedback Categories: Three categories of feedback (positive, neutral, and negative) were defined. Each category contained multiple pre-written feedback examples to simulate various customer experiences.

4)Generating Random Data: A function generate_random_row was created to generate a random row of data. For each row, random values were chosen for:

Customer details (name, email, contact)
Feedback sentiment (chosen randomly from positive, neutral, negative feedback)
Additional customer preferences (dining, room, wellness, etc.)
Creating Data Rows: Using a list comprehension, 2300 rows of random data were generated, representing different customer feedback entries.

5)Writing the Data to CSV: The csv module was used to write the headers and data rows to a CSV file. The file was saved with the name restaurant_feedback_data.csv.

6)Date and Time Considerations: The date and time for each feedback entry were generated in Indian Standard Time (IST) to represent the feedback timestamp correctly for a restaurant in India.

3.Columns Description

Customer Name- Type: Text (Random name generated)

cust mail id- Type: Text (Random email generated)

Feedback- Type: Text (Random feedback chosen from pre-defined categories)

Date and time- Type: Datetime (Generated in Indian Standard Time)

care-empid- Type: Text (Random employee ID)

cust-age- Type: Integer (Random age between 18 and 70)

cust-contact- Type: Text (Random phone number generated)

sentiment - future -Type: Categorical (Positive/Neutral/Negative)

dept- Type: Categorical (HR/Sales/Support/Finance/Engineering)

customer-stay duration- Type: Integer (Random stay duration between 1 and 30 days)

customer-n visits past- Type: Integer (Random number of visits between 0 and 10)

customer-membership status- Type: Categorical (Active/Inactive)

NPS (Net Promoter Score)- Type: Integer (Random score between 1 and 10)

Dining - Vegetarian/vegan- Type: Categorical (Vegetarian/Vegan/Non-Vegetarian)

Room preference- Type: Categorical (Deluxe/Standard/Suite)

Sports activities - [table tennis, golf, ...]- Type: Categorical (Table tennis/Golf/Swimming/Badminton)

Wellness - gym, sauna, massage- Type: Categorical (Gym/Sauna/Massage)

pricing patterns - frugal/luxury-Type: Categorical (Frugal/Luxury)

4.How to Use the Dataset
1. Download the CSV File
The dataset is available as a CSV file. You can download it directly from the repository.

2. Load the Data for Analysis
To load and analyze the data, you can use the Python Pandas library:

3. Use the Data for Sentiment Analysis or Machine Learning
This dataset is useful for:
Training sentiment analysis models
Building customer recommendation systems
Analyzing customer behavior and feedback trends


