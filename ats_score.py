def calculate_ats_score(resume_text):

    skills = [
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

    found_skills = []

    resume_lower = resume_text.lower()

    for skill in skills:

        if skill in resume_lower:
            found_skills.append(skill)

    score = int(
        (len(found_skills) / len(skills)) * 100
    )

    return score, found_skills