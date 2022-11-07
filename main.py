from zocrypt import decrypter
import streamlit as st
import pandas as pd
import pymysql
import os
import random
key = st.secrets["SIDKEY"]
host = decrypter.decrypt_text(
    "^(~x|P~@/&^W|x`-/u|&/m^#~,^v|u~@^P|Bu/@~2Tw/v`,v#W^v/B^T^u/H/w`@|m/(`K`T^5w`<&^w/1`4`5|w9|6~1/T`0~8/s`6`T/Pw`s2|T0^20/4|T|9|1`s`1`1/<5|5|T~P`B`u", key)
user= st.secrets["USER"]
password=st.secrets["PASSWORD"]


def init_connection():
    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        db='recommender_db',
        port=3306
    )


conn = init_connection()


gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
age = st.sidebar.number_input("Enter Age", min_value=0, max_value=100)
genre = st.sidebar.selectbox('Genre', ['Drama',
                                       'Action',
                                       'Crime',
                                       'Comedy',
                                       'Animation',
                                        'Adventure',
                                        'Fantasy',
                                        'Sci-Fi',
                                        'Childrens',
                                        'Thriller',
                                        'Romance',
                                        'Crime',
                                       'Horror',])
reset = st.sidebar.button("Reset")
if reset:
    age=0                         
st.subheader("Movie Recommendations")
if age==0:
    tagline=st.markdown("Spend your time **WATCHING** not _SEARCHING_")
    tagline_2=st.text("Enter your age, gender and genre to get movie recommendations")
    banner=st.image("https://storage.googleapis.com/afs-prod/media/e53811360eed4b8ba26b5f635d703a7c/3000.jpeg", width=400)
if age>0:
    with st.spinner('Wait for it...'):
    
        def get_gender():
            if gender == "Male":
                return "M"
            else:
                return "F"
        

        def get_age_range():
            if age <= 25:
                return 16,25
            elif age >= 26 and age <= 35:
                return 26,35
            elif age >= 36 and age <= 45:
                return 36,45
            elif age >= 46 and age <= 50:
                return 46,50
            elif age >= 51 and age <= 55:
                return 51,55
            elif age >= 56:
                return 51,55

        gender=get_gender()
        upper,lower=get_age_range()
        recommended_movies = pd.read_sql("""
    SELECT movies.title,
        DOT_PRODUCT(UNHEX(users.factors), UNHEX(movies.factors)) AS score
    FROM users JOIN movies
    WHERE users.gender = %s AND users.age BETWEEN %s AND %s and movies.genres = %s
    ORDER BY score DESC
    LIMIT 10;
    """, conn, params=([gender, upper, lower, genre]))
        empty = []
        for i in range(10):
            if recommended_movies["title"][i] in empty:
                continue
            empty.append(recommended_movies["title"][i])
            cols = st.columns(1)
            cols[0].header(recommended_movies["title"][i])
            imdb_url="https://www.imdb.com/find?q="+recommended_movies["title"][i].replace(" ", "%20")+"&ref_=nv_sr_sm"
            cols[0].write(f"Check the movie out [here]({imdb_url})")
