from resume_parser import extract_text_from_pdf, extract_skills_from_text
from job_parser import extract_job_skills
from skill_matcher import compare_skills

# Resume
resume_text = extract_text_from_pdf("data/sample_resume.pdf")
resume_skills = extract_skills_from_text(resume_text)

# Job Description
with open("data/sample_job_description.txt", "r", encoding="utf-8") as file:
    job_text = file.read()

job_skills = extract_job_skills(job_text)

# Compare
matched, missing, score = compare_skills(resume_skills, job_skills)

print("\nResume Match Score:")
print(score, "%")

print("\nMatched Skills:")
for skill in matched:
    print("-", skill)

print("\nMissing Skills:")
for skill in missing:
    print("-", skill)
