def compare_skills(resume_skills, job_skills):
    """
    Compares resume skills with job skills.
    Returns matched skills, missing skills, and skill match score.
    """
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched = resume_set.intersection(job_set)
    missing = job_set - resume_set

    if len(job_set) == 0:
        skill_score = 0
    else:
        skill_score = round((len(matched) / len(job_set)) * 100, 2)

    return sorted(list(matched)), sorted(list(missing)), skill_score


def calculate_final_fit_score(skill_score, semantic_score):
    """
    Calculates final fit score using weighted average.
    """
    final_score = (0.6 * skill_score) + (0.4 * semantic_score)
    return round(final_score, 2)
