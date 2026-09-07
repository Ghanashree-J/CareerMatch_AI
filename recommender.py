import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CareerRecommender:

    def __init__(self, file_path):

        # Load dataset
        self.data = pd.read_csv(file_path)

        # Clean empty values
        self.data = self.data.fillna("")

        # Create one text profile for every role
        self.data["profile_text"] = (
            self.data["role"] + " " +
            self.data["skills"] + " " +
            self.data["description"] + " " +
            self.data["category"]
        )

        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )

        # Convert all career roles into vectors
        self.role_vectors = self.vectorizer.fit_transform(
            self.data["profile_text"]
        )


    def clean_list(self, text):

        if not text:
            return []

        values = text.split(",")

        cleaned_values = []

        for value in values:

            value = value.strip().lower()

            if value and value not in cleaned_values:
                cleaned_values.append(value)

        return cleaned_values


    def get_role_skills(self, skills_text):

        return self.clean_list(skills_text)


    def calculate_skill_match(self, user_skills, role_skills):

        if not role_skills:
            return 0.0

        matched_skills = set(user_skills).intersection(
            set(role_skills)
        )

        return (
            len(matched_skills) / len(role_skills)
        ) * 100


    def calculate_preference_match(
        self,
        preferred_category,
        role_category
    ):

        if not preferred_category:
            return 50.0

        if (
            preferred_category.lower().strip()
            ==
            role_category.lower().strip()
        ):
            return 100.0

        return 0.0


    def recommend(
        self,
        user_skills,
        user_interests="",
        preferred_category="",
        top_n=3
    ):

        # Convert list of skills into text
        skills_text = " ".join(user_skills)

        # Create complete user profile
        user_profile = (
            skills_text + " " +
            user_interests + " " +
            preferred_category
        ).strip()

        # Convert user profile to TF-IDF vector
        user_vector = self.vectorizer.transform(
            [user_profile]
        )

        # Calculate semantic similarity
        similarity_scores = cosine_similarity(
            user_vector,
            self.role_vectors
        ).flatten()

        results = []

        # Analyze every career role
        for index, row in self.data.iterrows():

            role_skills = self.get_role_skills(
                row["skills"]
            )

            # Exact skill match
            skill_match = self.calculate_skill_match(
                user_skills,
                role_skills
            )

            # Category preference match
            preference_match = (
                self.calculate_preference_match(
                    preferred_category,
                    row["category"]
                )
            )

            # Convert cosine similarity to percentage
            semantic_match = (
                similarity_scores[index] * 100
            )

            # Final transparent weighted score
            final_score = (
                semantic_match * 0.35 +
                skill_match * 0.55 +
                preference_match * 0.10
            )

            matched_skills = []

            missing_skills = []

            for skill in role_skills:

                if skill in user_skills:
                    matched_skills.append(skill)

                else:
                    missing_skills.append(skill)

            results.append({
                "role": row["role"],
                "category": row["category"],
                "description": row["description"],

                "profile_match_score": round(
                    final_score,
                    2
                ),

                "semantic_match": round(
                    semantic_match,
                    2
                ),

                "skill_match": round(
                    skill_match,
                    2
                ),

                "preference_match": round(
                    preference_match,
                    2
                ),

                "matched_skills": matched_skills,

                "missing_skills": missing_skills
            })

        # Sort by final score
        results.sort(
            key=lambda x: x["profile_match_score"],
            reverse=True
        )

        return results[:top_n]