# src/job_parser.py

from src.resume_parser import extract_skills_from_text


def extract_job_skills(job_text):
    """
    Extracts skills from a job description.
    """
    return extract_skills_from_text(job_text)


if __name__ == "__main__":
    with open("data/sample_job_description.txt", "r", encoding="utf-8") as file:
        job_text = file.read()

    skills = extract_job_skills(job_text)

    print("Job Required Skills:")
    for skill in skills:
        print("-", skill)
