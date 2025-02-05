

# AI-Driven Guest Experience Personalization System for Hospitality

The implementation of an **AI-Driven Guest Experience Personalization System** for the hospitality industry, developed during the **Infosys Springboard Internship**. The project leverages **Large Language Models (LLMs)** and various AI techniques to create a seamless, personalized guest experience. Key components of the system include sentiment analysis, personalized recommendations, dynamic profile management, and a staff notification system.

## Project Components

### 1. **Sentiment Analysis Engine**
   - **Objective**: Provide real-time sentiment analysis based on guest feedback.
   - **Features**:
     - Detect guest sentiments and generate alerts and suggestions in real-time.
     - Alerts based on detected changes in guest sentiment to provide immediate support.
   - **Implementation**: 
     - Built using **Streamlit** to allow users to interact and provide feedback for sentiment analysis.

### 2. **Personalized Recommendation System**
   - **Objective**: Provide personalized recommendations to guests based on their historical interactions.
   - **Features**:
     - Recommends services or offers to guests based on similar guest behavior.
     - Uses **Cosine Similarity** to match similar users and provide tailored recommendations.
   - **Implementation**:
     - Data is loaded from interaction data (stored in CSV files), and recommendations are generated in real-time using **Streamlit**.

### 3. **Dynamic Profile Management System**
   - **Objective**: Manage user profiles in real-time, adjusting based on user behavior and preferences.
   - **Features**:
     - Dynamically create, modify, and manage user profiles as guests interact with the system.
     - Real-time updates based on guest behavior, allowing for personalized experiences.
   - **Implementation**:
     - Built with **Python** to integrate real-time profile management with a back-end database.

### 4. **Staff Notification System**
   - **Objective**: Notify staff regarding potential service issues or personalization opportunities based on guest feedback.
   - **Features**:
     - Alerts sent to staff via **Slack** and **Email** to help improve service quality and optimize personalization opportunities.
   - **Implementation**:
     - Automated alerts and notifications are generated and sent based on guest feedback in real-time.

---

## Milestones

### **Milestone 1: Environment Setup and Dataset Creation**
- The initial setup involves creating a Python virtual environment and installing required libraries for the project.
- A **mock CRM dataset** (Sentiment.csv) is created using sources like **HuggingFace** for guest feedback and **Datablist** for user information.

### **Milestone 2: Sentiment Analysis Engine Implementation**
- A **sentiment analysis engine** is deployed to analyze guest feedback and provide real-time sentiment results, suggestions, and alerts.
- The system uses a simple user interface to allow users to input feedback and receive sentiment analysis.

### **Milestone 3: Personalized Recommendation System & Dynamic Profile Management**
1. **Personalized Recommendation System**:
   - The recommendation system uses **Cosine Similarity** to match similar users and provide personalized service or product recommendations.
   
2. **Dynamic Profile Management**:
   - The system allows users to dynamically create, modify, and manage profiles in real-time based on user preferences and behaviors, enhancing the guest experience.

### **Milestone 4: Staff Notification System (Slack & Email Integration)**
- The system integrates with **Slack** and **Email** to automatically notify staff about potential service issues and recommend personalized services to users.

---

### **Final Integration: Complete Hospitality Management System**
- All the components from the above milestones are integrated into one seamless webpage that allows users to interact with the system and receive real-time feedback, recommendations, and notifications.
- The system ensures that:
  - API keys and environment configurations are correctly set up.
  - All necessary datasets are generated.
  - Versions match for dependencies, and database tables are ready.
  - Slack bot integration works, and email notifications are configured.

---

## Requirements
Make sure to install all the required libraries for smooth project execution.



### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


