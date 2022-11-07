# movie-recommender
Spend your time WATCHING not SEARCHING

## Inspiration
Our inspiration stemmed out of our joint desire to do something AI related as well as the need to make a movie recommender that actually recommended to us movies that we like.
## What it does
It used the ALS algorithm to obtain a number, called factors, for each user in the users table and movie in the movies table (in SingleStore). These factors are floating point numbers greater than 0.5 but less than 1. On multiplying the factor of a user with the factor of a movie, you get a number. Higher the number, the more recommended the movie is for you.
Therefore, by using the correct SQL statements, we can present to you the top 10 movies you would like to watch based on your gender, age and genre preference.
## How we built it
We started by uploading data to single store. It took over 9000 queries and over 3 hours to successfully upload all the data into two separate tables in SingleStore. After that, we created a Streamlit website where the user can enter their gender, age and genre preference and the coded the backend of the project, where we have written the necessary SQL queries to get the required information.
## Challenges we ran into
Our biggest challenge was actually uploading the data because we first had to get the data into a pyspark dataframe to calculate the factor of each record (row). These factors where then converted to binary form so that it we could add them as a new column in the pyspark dataframe, after which we had to upload the data to SingleStore, which took forever.
## Accomplishments that we're proud of
Making our first ML project is something we are definitely proud of, along with the fact that we used a complex algorithm (ALS). We used SingleStore, which was completely new territory for us and we managed to overcome all the challenges we faced.
