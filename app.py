import streamlit as st
import pickle
import requests
from dotenv import load_dotenv
import os

# Load Data
movies_df = pickle.load(open('data/movies_df.pkl','rb'))
similarity = pickle.load(open('data/similarity.pkl','rb'))

# Function:
def configure():
    load_dotenv()
    
def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={os.getenv('API_KEY')}&language=en-US")
    data = response.json()
    return "https://image.tmdb.org/t/p/original"+data['poster_path']

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        id = movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_poster.append(fetch_poster(id))
    return recommended_movies,recommended_movies_poster

# Web App
def main():
    configure()
    st.set_page_config(page_title="Movie Recommender", page_icon=":camera:",layout="wide")
    
    st.title('Movie Recommendation System')
    selected_movie = st.selectbox("Select a movie",movies_df['title'])

    if st.button('Recommend'):
        names,posters = recommend(selected_movie)
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.text(names[0])
            st.image(posters[0])

        with col2:
            st.text(names[1])
            st.image(posters[1])
            
        with col3:
            st.text(names[2])
            st.image(posters[2])

        with col4:
            st.text(names[3])
            st.image(posters[3])
        
        with col5:
            st.text(names[4])
            st.image(posters[4])

if __name__=="__main__": 
    main()