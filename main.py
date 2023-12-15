import streamlit as st
import pickle
import requests

def fetch_posters(movie_id):
    res = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e6d1b15b107428620bb15fc78adb1608'.format(movie_id))
    data = res.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recomdations(movie):
    ind = moviess[moviess['title'] == movie].index[0]
    distances = similarities[ind]

    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    movies_ind_list = []
    for i in movies:
        movies_ind_list.append(i[0])

    titles = []
    posters_path = []

    for i in movies_ind_list:

        titles.append(moviess.iloc[i]['title'])
        posters_path.append(fetch_posters(moviess.iloc[i]['movie_id']))

    return titles,posters_path

similarities = pickle.load(open("similarities.pkl","rb"))

st.title("Movie Recommender System")

moviess = pickle.load(open("movies.pkl","rb"))
movie_list = moviess['title'].values

selected_movie = st.selectbox("Select a movie",movie_list)
if(st.button("Recommend")):
    rec,pos = recomdations(selected_movie)

    col1,col2,col3,col4,col5  = st.columns(5)

    with col1:
        st.text(rec[0])
        st.image(pos[0])
    with col2:
        st.text(rec[1])
        st.image(pos[1])
    with col3:
        st.text(rec[2])
        st.image(pos[2])
    with col4:
        st.text(rec[3])
        st.image(pos[3])
    with col5:
        st.text(rec[4])
        st.image(pos[4])

