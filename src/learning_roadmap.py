# src/learning_roadmap.py

LEARNING_ROADMAP = {
    "python": [
        "Learn Python basics (syntax, loops, functions)",
        "Practice data structures (lists, dicts, sets)",
        "Work with files and APIs"
    ],
    "sql": [
        "Learn basic SQL queries (SELECT, WHERE, JOIN)",
        "Practice aggregation functions",
        "Solve real SQL interview questions"
    ],
    "machine learning": [
        "Understand ML fundamentals",
        "Learn supervised vs unsupervised learning",
        "Practice with scikit-learn projects"
    ],
    "statistics": [
        "Learn descriptive statistics",
        "Understand probability & distributions",
        "Apply statistics in data analysis"
    ],
    "power bi": [
        "Learn Power BI interface",
        "Create basic dashboards",
        "Practice real datasets"
    ],
    "tableau": [
        "Learn Tableau basics",
        "Build interactive dashboards",
        "Publish Tableau public projects"
    ],
    "numpy": [
        "Learn NumPy arrays",
        "Practice vectorized operations",
        "Use NumPy for numerical computing"
    ],
    "pandas": [
        "Learn DataFrames & Series",
        "Data cleaning & manipulation",
        "EDA with real datasets"
    ]
}


def generate_learning_roadmap(missing_skills):
    """
    Generates a learning roadmap for missing skills.
    """
    roadmap = {}

    for skill in missing_skills:
        if skill in LEARNING_ROADMAP:
            roadmap[skill] = LEARNING_ROADMAP[skill]
        else:
            roadmap[skill] = [
                f"Learn basics of {skill}",
                f"Practice {skill} with small projects",
                f"Apply {skill} in real-world scenarios"
            ]

    return roadmap
