# CareerMatch AI

CareerMatch AI is an AI-based career recommendation system that recommends suitable technology career roles by analyzing a user's technical skills, career interests, and preferred career category.

The system uses content-based recommendation techniques and TF-IDF with cosine similarity to compare a user's profile with predefined career-role profiles.

---

## Project Overview

Choosing a suitable technology career can be difficult when a person has multiple skills and interests.

CareerMatch AI helps solve this problem by:

- Collecting the user's technical skills
- Understanding their career interests
- Considering their preferred career category
- Comparing the user profile with available career roles
- Ranking the most suitable career roles
- Showing matched skills and skill gaps
- Providing personalized learning suggestions
- Suggesting practical projects for career development

---

## Key Features

### 1. Skill-Based Matching

The system accepts multiple technical skills such as:

- Python
- SQL
- Machine Learning
- JavaScript
- Cloud
- Linux
- Git

The entered skills are compared with the skills required by different career roles.

### 2. Interest-Based Matching

Users can enter career interests such as:

- AI
- Data
- Websites
- Cloud
- Security

These interests are included in the profile comparison.

### 3. Career Category Preference

Users can select a preferred category:

1. Data and AI
2. Software Development
3. Cloud and DevOps
4. Cybersecurity
5. No Preference

### 4. TF-IDF and Cosine Similarity

The system uses TF-IDF vectorization to convert career profiles into numerical representations.

Cosine similarity is then used to measure the semantic similarity between the user's profile and each career role.

### 5. Transparent Match Score

Each recommendation includes a Profile Match Score based on:

- Semantic similarity
- Exact skill matching
- Career category preference

The score is intended to help compare career-role alignment and is not a prediction of hiring or job selection.

### 6. Match Score Breakdown

The system displays:

- Semantic Similarity
- Skill Match
- Preference Match

This makes the recommendation process easier to understand.

### 7. Matched Skills

The system identifies skills that the user already has which are relevant to the recommended role.

### 8. Skill Gaps

The system identifies important skills required by the recommended role that are not currently present in the user's profile.

### 9. Learning Priorities

Missing skills are organized into learning priorities so the user can focus on developing the most relevant areas first.

### 10. Personalized Improvement Suggestions

The system provides suggestions based on the user's match score and skill gaps.

### 11. Project Suggestions

The system recommends a practical project idea related to the career category.

### 12. Career Match Meter

A visual terminal-based match meter provides a quick representation of the profile alignment.

Example:

    PROFILE MATCH METER

                         65%

                  GOOD ALIGNMENT

        [█████████████░░░░░░░]

---

## Recommendation Process

The recommendation system follows these main stages:

    User Profile
          |
          v
    Skill & Interest Analysis
          |
          v
    TF-IDF Vectorization
          |
          v
    Similarity Calculation
          |
          v
    Skill & Preference Matching
          |
          v
    Weighted Score Calculation
          |
          v
    Ranking
          |
          v
    Top Career Recommendations

---

## Scoring Approach

The final Profile Match Score combines three components:

- Semantic Similarity: 35%
- Exact Skill Match: 55%
- Career Preference Match: 10%

This weighted approach combines semantic understanding with direct skill matching and the user's selected career category.

---

## Available Career Roles

The current dataset contains roles including:

- Data Scientist
- Data Analyst
- Machine Learning Engineer
- Data Engineer
- Backend Developer
- Frontend Developer
- Full Stack Developer
- DevOps Engineer
- Cloud Engineer
- Cybersecurity Analyst
- QA Automation Engineer

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- CSV Dataset
- Git & GitHub

---

## Project Structure

```text
CareerMatch_AI/
│
├── data/
│   └── job_roles.csv
│
├── main.py
├── recommender.py
├── requirements.txt
├── .gitignore
└── README.md