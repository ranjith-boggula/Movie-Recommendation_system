
import streamlit as st
import pickle
import joblib

st.title("Movie Recommendation System")


# Load movie data and similarity matrix
@st.cache_resource
def load_data():

    with open("movies.pickle", "rb") as m:
        movies = pickle.load(m)

    similarity = joblib.load("similarities.joblib")

    return movies, similarity


movies, similarity = load_data()


# Movie recommendation function
def recommend(name_movie):

    movie_index = movies[movies["title"] == name_movie].index[0]

    recommendations = similarity[movie_index]

    movie_list = sorted(
        enumerate(recommendations),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# Streamlit interface
name_movie = st.selectbox(
    "Enter the Movie Name",
    movies["title"].values
)

if st.button("Recommend"):

    recommended_movies = recommend(name_movie)

    st.write("The Recommended Movies are:")

    for movie in recommended_movies:
        st.write(movie)

