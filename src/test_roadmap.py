from src.learning_roadmap import generate_learning_roadmap

missing_skills = ["machine learning", "power bi", "deep learning"]

roadmap = generate_learning_roadmap(missing_skills)

for skill, steps in roadmap.items():
    print(f"\nRoadmap for {skill}:")
    for step in steps:
        print("-", step)
