import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_ai_feedback(resume_text, job_description):
    """
    Generates AI-based resume feedback using OpenRouter LLM.
    """

    prompt = f"""
You are an expert resume reviewer and technical recruiter.

Analyze the RESUME and JOB DESCRIPTION below and provide:
1. Overall feedback
2. Top 3 improvements
3. Missing or weak skills
4. ATS optimization tips

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Give clear, concise, and actionable advice.
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[
            {"role": "system", "content": "You are a professional resume coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=600
    )

    return response.choices[0].message.content
