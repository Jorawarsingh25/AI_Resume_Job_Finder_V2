def get_missing_skills(resume_text):

    required_skills = [
        "python",
        "sql",
        "power bi",
        "excel",
        "machine learning",
        "statistics",
        "tableau",
        "azure",
        "pandas",
        "numpy"
    ]

    resume_text = resume_text.lower()

    missing = []

    for skill in required_skills:

        if skill not in resume_text:
            missing.append(skill)

    return missing