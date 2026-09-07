from recommender import CareerRecommender


def format_skill(skill):

    special_names = {
        "sql": "SQL",
        "api": "API",
        "apis": "APIs",
        "aws": "AWS",
        "ai": "AI",
        "etl": "ETL",
        "qa": "QA",
        "ci/cd": "CI/CD",
        "html": "HTML",
        "css": "CSS",
        "ui": "UI",
        "ux": "UX",
        "javascript": "JavaScript",
        "typescript": "TypeScript",
        "node.js": "Node.js",
        "power bi": "Power BI"
    }

    skill = skill.strip().lower()

    if skill in special_names:
        return special_names[skill]

    return skill.title()


# ==========================================================
# PROFILE MATCH METER
# ==========================================================

def display_match_meter(score):

    total_blocks = 20
    filled_blocks = round(score / 5)

    if filled_blocks > total_blocks:
        filled_blocks = total_blocks

    empty_blocks = total_blocks - filled_blocks

    meter = (
        "█" * filled_blocks +
        "░" * empty_blocks
    )

    print("\n" + "-" * 70)
    print("PROFILE MATCH METER")
    print("-" * 70)

    print(f"\n                     {score}%")

    if score >= 80:

        level = "STRONG ALIGNMENT"

        message = (
            "Your profile strongly aligns with this career role."
        )

    elif score >= 60:

        level = "GOOD ALIGNMENT"

        message = (
            "Your profile has a good foundation for this career role."
        )

    elif score >= 40:

        level = "GROWING ALIGNMENT"

        message = (
            "Your profile has potential and shows a developing alignment "
            "with this career role."
        )

    elif score >= 20:

        level = "NEEDS GROWTH"

        message = (
            "You have some relevant skills, but important areas need "
            "further development."
        )

    else:

        level = "EARLY STAGE"

        message = (
            "This career role requires significant skill development "
            "to improve your profile alignment."
        )

    print(f"              {level}\n")
    print(f"        [{meter}]\n")
    print(message)


# ==========================================================
# LEARNING PRIORITY
# ==========================================================

def get_priority_skills(missing_skills):

    high_priority = missing_skills[:3]

    medium_priority = missing_skills[3:]

    return high_priority, medium_priority


# ==========================================================
# PERSONALIZED SUGGESTIONS
# ==========================================================

def generate_suggestions(score, missing_skills):

    suggestions = []

    if score >= 70:

        suggestions.append(
            "You already have a strong foundation for this career role."
        )

        suggestions.append(
            "Focus on advanced projects and strengthening your portfolio."
        )

    elif score >= 50:

        suggestions.append(
            "You have a good foundation for this role."
        )

        suggestions.append(
            "Improving your missing core skills can significantly "
            "strengthen your profile."
        )

    elif score >= 30:

        suggestions.append(
            "You have some relevant skills, but you should focus on "
            "building stronger core knowledge."
        )

    else:

        suggestions.append(
            "Start by learning the fundamental skills required for "
            "this career role."
        )

    for skill in missing_skills[:3]:

        suggestions.append(
            f"Learn and practice {format_skill(skill)}."
        )

    if missing_skills:

        suggestions.append(
            "Build one practical project using both your existing "
            "skills and newly learned skills."
        )

    suggestions.append(
        "Add your projects and technical skills to your resume "
        "and GitHub profile."
    )

    return suggestions


# ==========================================================
# RECOMMENDATION EXPLANATION
# ==========================================================

def create_explanation(role, matched_skills, score):

    if matched_skills:

        skills_text = ", ".join(
            format_skill(skill)
            for skill in matched_skills[:4]
        )

        return (
            f"{role} was recommended because your profile contains "
            f"relevant skills such as {skills_text}. "
            f"Your overall profile match score is {score}%."
        )

    return (
        f"{role} was recommended based on the overall similarity "
        f"between your skills, interests, and the career role."
    )


# ==========================================================
# PROJECT SUGGESTIONS
# ==========================================================

def get_project_suggestion(category):

    if category == "Data and AI":

        return (
            "Build a data analysis or machine learning project "
            "using a real-world dataset."
        )

    elif category == "Software Development":

        return (
            "Build a complete application and upload the source "
            "code with a clear README to GitHub."
        )

    elif category == "Cloud and DevOps":

        return (
            "Build a cloud deployment or automation project using "
            "cloud and DevOps tools."
        )

    elif category == "Cybersecurity":

        return (
            "Build a legal cybersecurity lab project and document "
            "your analysis and findings."
        )

    return (
        "Build a practical project related to the career role."
    )


# ==========================================================
# MAIN PROGRAM
# ==========================================================

def main():

    # ======================================================
    # PROJECT INTRODUCTION
    # ======================================================

    print("\n" + "=" * 70)

    print(
        "       CAREERMATCH AI - CAREER RECOMMENDATION SYSTEM"
    )

    print("=" * 70)

    print("\nThis system recommends career roles by analyzing:")

    print("• Your technical skills")

    print("• Your career interests")

    print("• Your preferred career category")


    # ======================================================
    # LOAD DATASET
    # ======================================================

    try:

        recommender = CareerRecommender(
            "data/job_roles.csv"
        )

    except FileNotFoundError:

        print("\nERROR: job_roles.csv file not found.")

        print(
            "Make sure job_roles.csv is inside the data folder."
        )

        return


    # ======================================================
    # TOTAL CAREER ROLES
    # ======================================================

    print(
        f"\nTotal Career Roles Available: {len(recommender.data)}"
    )


    # ======================================================
    # GET USER SKILLS
    # ======================================================

    print("\n" + "-" * 70)

    skills_input = input(
        "\nEnter your technical skills separated by commas.\n"
        "Example: Python, SQL, Data Analysis, Cloud\n\n"
        "Enter your skills: "
    )

    user_skills = recommender.clean_list(
        skills_input
    )

    if not user_skills:

        print(
            "\nYou must enter at least one skill."
        )

        return


    # ======================================================
    # GET USER INTERESTS
    # ======================================================

    print("\n" + "-" * 70)

    user_interests = input(
        "\nWhat are you interested in?\n"
        "Example: AI, Data, Websites, Cloud, Security\n\n"
        "Enter your interests: "
    )


    # ======================================================
    # CATEGORY SELECTION
    # ======================================================

    print("\n" + "-" * 70)

    print("\nAvailable career categories:")

    print("1. Data and AI")

    print("2. Software Development")

    print("3. Cloud and DevOps")

    print("4. Cybersecurity")

    print("5. No Preference")


    category_choice = input(
        "\nChoose a category (1-5): "
    )


    category_map = {

        "1": "Data and AI",

        "2": "Software Development",

        "3": "Cloud and DevOps",

        "4": "Cybersecurity",

        "5": ""
    }


    preferred_category = category_map.get(
        category_choice,
        ""
    )


    # ======================================================
    # GET RECOMMENDATIONS
    # ======================================================

    recommendations = recommender.recommend(
        user_skills=user_skills,
        user_interests=user_interests,
        preferred_category=preferred_category,
        top_n=3
    )


    # ======================================================
    # DISPLAY USER PROFILE
    # ======================================================

    print("\n\n" + "=" * 70)

    print("YOUR CAREER PROFILE")

    print("=" * 70)


    print("\nTECHNICAL SKILLS")

    for skill in user_skills:

        print(
            f"✓ {format_skill(skill)}"
        )


    print("\nCAREER INTERESTS")

    if user_interests:

        print(
            user_interests
        )

    else:

        print(
            "No specific interest entered."
        )


    print("\nPREFERRED CATEGORY")

    if preferred_category:

        print(
            preferred_category
        )

    else:

        print(
            "No category preference"
        )


    # ======================================================
    # DISPLAY TOP RECOMMENDATIONS
    # ======================================================

    for rank, result in enumerate(
        recommendations,
        start=1
    ):

        score = result[
            "profile_match_score"
        ]

        role = result[
            "role"
        ]

        category = result[
            "category"
        ]

        matched_skills = result[
            "matched_skills"
        ]

        missing_skills = result[
            "missing_skills"
        ]


        high_priority, medium_priority = (
            get_priority_skills(
                missing_skills
            )
        )


        suggestions = generate_suggestions(
            score,
            missing_skills
        )


        # ==================================================
        # RECOMMENDATION HEADER
        # ==================================================

        print("\n\n" + "=" * 70)

        print(
            f"CAREER RECOMMENDATION #{rank}"
        )

        print("=" * 70)


        print(
            f"\nROLE: {role.upper()}"
        )

        print(
            f"CATEGORY: {category}"
        )


        # ==================================================
        # UNIQUE PROFILE MATCH METER
        # ==================================================

        display_match_meter(score)


        # ==================================================
        # SCORE BREAKDOWN
        # ==================================================

        print("\n" + "-" * 70)

        print("MATCH SCORE BREAKDOWN")

        print("-" * 70)

        print(
            f"Semantic Similarity: "
            f"{result['semantic_match']}%"
        )

        print(
            f"Skill Match: "
            f"{result['skill_match']}%"
        )

        print(
            f"Preference Match: "
            f"{result['preference_match']}%"
        )


        # ==================================================
        # ROLE DESCRIPTION
        # ==================================================

        print("\nROLE DESCRIPTION")

        print(
            result["description"]
        )


        # ==================================================
        # WHY RECOMMENDED
        # ==================================================

        print(
            "\nWHY THIS ROLE WAS RECOMMENDED"
        )

        print(
            create_explanation(
                role,
                matched_skills,
                score
            )
        )


        # ==================================================
        # MATCHED SKILLS
        # ==================================================

        print("\nMATCHED SKILLS")

        if matched_skills:

            for skill in matched_skills:

                print(
                    f"✓ {format_skill(skill)}"
                )

        else:

            print(
                "No direct skill matches found."
            )


        # ==================================================
        # SKILL GAPS
        # ==================================================

        print("\nSKILL GAPS")

        if missing_skills:

            for skill in missing_skills:

                print(
                    f"✗ {format_skill(skill)}"
                )

        else:

            print(
                "No major skill gaps found."
            )


        # ==================================================
        # LEARNING PRIORITY
        # ==================================================

        print("\nLEARNING PRIORITY")


        if high_priority:

            print("\nHIGH PRIORITY:")

            for skill in high_priority:

                print(
                    f"• {format_skill(skill)}"
                )


        if medium_priority:

            print("\nMEDIUM PRIORITY:")

            for skill in medium_priority:

                print(
                    f"• {format_skill(skill)}"
                )


        # ==================================================
        # HOW TO IMPROVE
        # ==================================================

        print(
            "\nHOW TO IMPROVE YOUR PROFILE"
        )

        for number, suggestion in enumerate(
            suggestions,
            start=1
        ):

            print(
                f"{number}. {suggestion}"
            )


        # ==================================================
        # PROJECT SUGGESTION
        # ==================================================

        print("\nPROJECT SUGGESTION")

        print(
            get_project_suggestion(
                category
            )
        )


    # ======================================================
    # FINAL MESSAGE
    # ======================================================

    print("\n\n" + "=" * 70)

    print("CAREER ANALYSIS COMPLETE")

    print("=" * 70)


    print(
        "\nNote: The Profile Match Score is a recommendation score "
        "based on skills, semantic similarity, and career preferences."
    )

    print(
        "It is not a guarantee of job selection or hiring."
    )


# ==========================================================
# RUN THE PROGRAM
# ==========================================================

if __name__ == "__main__":

    main()