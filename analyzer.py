from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_skills(text):

    skills = [
        "python",
        "java",
        "sql",
        "excel",
        "communication",
        "leadership",
        "microsoft office",
        "project management"
    ]

    text = text.lower()

    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    return found


def analyze_resume(resume_text, job_description):

    embeddings = model.encode([resume_text, job_description])

    similarity = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
     )[0][0]

    score = float(round(similarity * 100, 2))

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    missing = list(set(jd_skills) - set(resume_skills))

    suggestions = [
        "Add measurable achievements",
        "Highlight relevant projects"
    ]

    return {
        "match_score": score,
        "resume_skills": resume_skills,
        "missing_skills": missing,
        "suggestions": suggestions
    }