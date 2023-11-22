import streamlit as st
import pickle
import requests
from dotenv import load_dotenv
import os

# Load Data
movies_df = pickle.load(open('data/pkl_data/movies_df.pkl','rb'))
similarity = pickle.load(open('data/pkl/similarity.pkl','rb'))

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
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    
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
    st.set_page_config(page_title="Movie Recommender", page_icon=":camera:", layout="wide")
    st.title('Movie Recommendation System')
    selected_movie = st.selectbox(
        label="Select a movie",
        options=movies_df['title'],
        placeholder = "Choose a movie",
        index=None)


    if st.button('Recommend'):            
        try:    
            names,posters = recommend(selected_movie)
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                st.text(names[0])
                st.image(posters[0],width=150)
                
                st.text(names[5])
                st.image(posters[5],width=150)

            with col2:
                st.text(names[1])
                st.image(posters[1],width=150)

                st.text(names[6])
                st.image(posters[6],width=150)
                
            with col3:
                st.text(names[2])
                st.image(posters[2],width=150)
                
                st.text(names[7])
                st.image(posters[7],width=150)

            with col4:
                st.text(names[3])
                st.image(posters[3],width=150)
                
                st.text(names[8])
                st.image(posters[8],width=150)
            
            with col5:
                st.text(names[4])
                st.image(posters[4],width=150)
                
                st.text(names[9])
                st.image(posters[9],width=150)
                
        except IndexError:
            st.error("No movies selected.")
        
        except TypeError:
            st.error("Currently we don't have any information about this movie.")
            
            
if __name__=="__main__": 
    main()