import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

from src.resume_parser import extract_text_from_pdf, extract_skills_from_text
from src.job_parser import extract_job_skills
from src.skill_matcher import compare_skills, calculate_final_fit_score
from src.similarity_matcher import calculate_similarity
from src.learning_roadmap import generate_learning_roadmap
from src.ai_feedback import generate_ai_feedback

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="SkillSync AI",
    page_icon="🧠",
    layout="wide"
)

# --------------------------------------------------
# Global CSS
# --------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0F172A, #020617);
}
.block-container {
    padding: 3rem 4rem;
}
.navbar {
    background: linear-gradient(90deg, #7C3AED, #9333EA);
    padding: 1.2rem 2.5rem;
    border-radius: 16px;
    color: white;
    font-size: 1.6rem;
    font-weight: 800;
    margin-bottom: 2.5rem;
}
.section-title {
    font-size: 1.8rem;
    font-weight: 700;
    margin: 2.5rem 0 1.5rem 0;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Navbar
# --------------------------------------------------
st.markdown("""
<div class="navbar">
    🧠 SkillSync AI — Resume Intelligence Platform
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Tabs
# --------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📊 Analyzer", "📈 Visual Insights", "🤖 AI Suggestions", "🧠 AI Coach", "ℹ️ About"]
)

# ==================================================
# TAB 1 — ANALYZER
# ==================================================
with tab1:
    st.markdown('<div class="section-title">📄 Resume & Job Analysis</div>', unsafe_allow_html=True)

    colA, colB = st.columns(2)
    with colA:
        resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    with colB:
        job_description = st.text_area("Paste Job Description")

    if resume_file and job_description:
        with st.spinner("🔍 Analyzing resume..."):
            time.sleep(1)

            with open("temp_resume.pdf", "wb") as f:
                f.write(resume_file.getbuffer())

            resume_text = extract_text_from_pdf("temp_resume.pdf")
            resume_skills = extract_skills_from_text(resume_text)
            job_skills = extract_job_skills(job_description)

            matched, missing, skill_score = compare_skills(resume_skills, job_skills)
            semantic_score = calculate_similarity(resume_text, job_description)
            final_fit_score = calculate_final_fit_score(skill_score, semantic_score)

            roadmap = generate_learning_roadmap(missing)

        c1, c2, c3 = st.columns(3)
        c1.metric("⭐ Final Fit Score", f"{final_fit_score}%")
        c2.metric("🎯 Skill Match", f"{skill_score}%")
        c3.metric("🧠 Semantic Match", f"{semantic_score}%")

        st.success("✅ Matched Skills")
        st.write(matched)

        st.error("❌ Missing Skills")
        st.write(missing)

    else:
        st.info("Upload resume and paste job description to begin.")

# ==================================================
# TAB 2 — VISUAL INSIGHTS
# ==================================================
with tab2:
    st.markdown('<div class="section-title">📈 Skill Visual Analytics</div>', unsafe_allow_html=True)

    if "matched" in locals():

        labels = ["Matched Skills", "Missing Skills"]
        values = [len(matched), len(missing)]

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_title("Skill Match Overview")
        st.pyplot(fig)

        all_skills = list(set(job_skills))
        radar_values = [1 if skill in resume_skills else 0 for skill in all_skills]

        angles = np.linspace(0, 2 * np.pi, len(all_skills), endpoint=False)
        radar_values += radar_values[:1]
        angles = np.concatenate([angles, [angles[0]]])

        fig2 = plt.figure()
        ax2 = fig2.add_subplot(111, polar=True)
        ax2.plot(angles, radar_values)
        ax2.fill(angles, radar_values, alpha=0.3)
        ax2.set_thetagrids(np.degrees(angles[:-1]), all_skills)
        ax2.set_title("Skill Coverage Radar")

        st.pyplot(fig2)

    else:
        st.info("Analyze a resume to see charts.")

# ==================================================
# TAB 3 — AI SUGGESTIONS (RULE-BASED)
# ==================================================
with tab3:
    st.markdown('<div class="section-title">🤖 AI Resume Improvement Suggestions</div>', unsafe_allow_html=True)

    if "missing" in locals():

        suggestions = []

        if len(missing) > 3:
            suggestions.append("Add projects or certifications for missing skills.")

        if skill_score < 50:
            suggestions.append("Tailor resume keywords to the job description.")

        if not suggestions:
            suggestions.append("Resume is well aligned. Focus on clarity and metrics.")

        for s in suggestions:
            st.write("✅", s)

    else:
        st.info("Analyze a resume to get suggestions.")

# ==================================================
# TAB 4 — AI COACH (LLM)
# ==================================================
with tab4:
    st.markdown("## 🧠 AI Resume Coach")

    st.info("Generate advanced AI feedback using a Large Language Model.")

    if "resume_text" in locals() and "job_description" in locals():
        if st.button("✨ Generate AI Resume Feedback"):
            with st.spinner("🤖 AI is reviewing your resume..."):
                try:
                    feedback = generate_ai_feedback(resume_text, job_description)
                    st.success("AI Feedback Generated")
                    st.write(feedback)
                except Exception as e:
                    st.error("AI feedback failed.")
                    st.caption(str(e))
    else:
        st.info("Upload resume and job description first.")

# ==================================================
# TAB 5 — ABOUT
# ==================================================
with tab5:
    st.markdown("""
    ## ℹ️ About SkillSync AI

    **SkillSync AI** is a portfolio-grade AI application that demonstrates:

    - Resume parsing & skill extraction
    - Machine learning semantic matching
    - Visual skill analytics
    - Rule-based + LLM-based AI feedback

    ### 🛠 Tech Stack
    - Python
    - Streamlit
    - scikit-learn
    - Matplotlib
    - LLM APIs (OpenRouter)

    ### 🎯 Goal
    To build an end-to-end AI system that mimics real-world resume screening and guidance.
    """)
