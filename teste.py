import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_excel(r'C:\Users\sigab\OneDrive\Área de Trabalho\machine\recomendacao\netflix_titles.xlsx')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['listed_in'])

print(tfidf_matrix[:10, :10].toarray())

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recomendar_filmes(titulo, top_n=5):
   
    idx = df[df['title'] == titulo].index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    sim_scores = sim_scores[1:top_n+1]  
    movie_indices = [i[0] for i in sim_scores]

    return df[['title', 'listed_in']].iloc[movie_indices]

recomendados = recomendar_filmes("Naruto Shippuden the Movie: Blood Prison", top_n=5)
print("Filmes recomendados:")
print(recomendados)
