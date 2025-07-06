from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_schools(query, df):
    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(df["facilities"] + " " + df["board"])
    query_vec = tfidf.transform([query])
    similarity = cosine_similarity(query_vec, matrix).flatten()
    top_indices = similarity.argsort()[-5:][::-1]
    return df.iloc[top_indices]
