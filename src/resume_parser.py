import pdfplumber

# -----------------------------
# List of skills we want to detect
# -----------------------------
SKILLS = [
    "python", "java", "c++", "c",
    "data science", "machine learning", "deep learning",
    "nlp", "sql", "mysql", "postgresql",
    "pandas", "numpy", "matplotlib", "seaborn",
    "excel", "power bi", "tableau",
    "statistics", "scikit-learn", "tensorflow", "pytorch"
]

# -----------------------------
# Function to extract text from PDF
# -----------------------------
def extract_text_from_pdf(pdf_path):
    """
    Reads a PDF file and extracts all text from it.
    Returns the extracted text as a single string.
    """
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text

# -----------------------------
# Function to extract skills from text
# -----------------------------
def extract_skills_from_text(text):
    """
    Finds skills from the resume text using keyword matching.
    """
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return sorted(set(found_skills))

# -----------------------------
# Test the functions
# -----------------------------
if __name__ == "__main__":
    resume_path = "data/sample_resume.pdf"

    resume_text = extract_text_from_pdf(resume_path)
    skills = extract_skills_from_text(resume_text)

    print("Extracted Skills:")
    for skill in skills:
        print("-", skill)
