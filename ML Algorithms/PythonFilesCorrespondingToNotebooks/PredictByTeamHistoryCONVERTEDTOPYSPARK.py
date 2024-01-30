#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
os.environ["JAVA_HOME"] = "C:\Program Files\Java\jdk-11.0.17"
os.environ["SPARK_HOME"] = "C:/Users/Ummad/Documents/spark/spark-3.0.1-bin-hadoop2.7"


# In[10]:


import findspark
findspark.init()

import pyspark # only run after findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyApp").config("spark.some.config.option", "some-value").getOrCreate()


# In[11]:


import pyspark.sql.functions as F
from pyspark.sql.types import *
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.stat import Correlation
from pyspark.ml.regression import LinearRegression

from string import ascii_uppercase as alphabet
from scipy.stats import poisson


# In[12]:


df_history_data = spark.read.option("header", "true").csv("historical_data.csv")


# In[13]:


from pyspark.sql.functions import col

df_home = df_history_data.select(col('HomeTeam').alias('Team'), col('HomeGoals').alias('GoalsScored'), col('AwayGoals').alias('GoalsConceded'))
df_away = df_history_data.select(col('AwayTeam').alias('Team'), col('AwayGoals').alias('GoalsScored'), col('HomeGoals').alias('GoalsConceded'))

df_home = df_home.withColumnRenamed('HomeTeam', 'Team').withColumnRenamed('HomeGoals', 'GoalsScored').withColumnRenamed('AwayGoals', 'GoalsConceded')
df_away = df_away.withColumnRenamed('AwayTeam', 'Team').withColumnRenamed('AwayGoals', 'GoalsScored').withColumnRenamed('HomeGoals', 'GoalsConceded')


# In[14]:


from pyspark.sql.functions import avg

df_team_strength = df_home.union(df_away)\
    .groupBy("Team")\
    .agg(avg("GoalsScored").alias("GoalsScored"), avg("GoalsConceded").alias("GoalsConceded"))


# In[15]:


from scipy.stats import poisson
from itertools import chain

def predict_points(home, away, df_team_strength):

    if home in chain(*df_team_strength.select("Team").collect()) and away in chain(*df_team_strength.select("Team").collect()):
        
        home_row = df_team_strength.filter(df_team_strength.Team == home).first()
        
        away_row = df_team_strength.filter(df_team_strength.Team == away).first()

        lambda_home = home_row["GoalsScored"] * away_row["GoalsConceded"]
        lambda_away = away_row["GoalsScored"] * home_row["GoalsConceded"]
        prob_home, prob_away, prob_draw = 0, 0, 0
        import random


        games1 = random.randint(1, 145) #number of games the first team will play
        games2 = random.randint(1, 145) #number of games the second team will play
        points_prob = random.randint(0,2) #home/away advantage
        points_prob2 = random.randint(0,1) #home/away advantage
        for x in range(0, games1):
            for y in range(0, games2):
                p = poisson.pmf(x, lambda_home) * poisson.pmf(y, lambda_away)
                if x == y:
                    prob_draw += p
                elif x > y:
                    prob_home += p
                else:
                    prob_away += p   
        points_home = 3 * (prob_home) + prob_draw
        points_away = 3 * (prob_away) + prob_draw
        return (points_prob + points_home,points_prob2 + points_away)
    else:
        return (10, 10)




    


# In[16]:


print("Enter the name of the first team:")
team1 = input().strip()

print("Enter the name of the second team:")
team2 = input().strip()

print(f"Predicting points for {team1} and {team2}:")
score1, score2 = predict_points(team1, team2, df_team_strength)

score1_rounded = round(score1)
score2_rounded = round(score2)

if score1_rounded > score2_rounded:
    print(f"The predicted winner is {team1} with {score1_rounded} goals.")
elif score2_rounded > score1_rounded:
    print(f"The predicted winner is {team2} with {score2_rounded} goals.")
else:
    print(f"The match between {team1} and {team2} is predicted to be a draw with both teams having {score1_rounded} goals.")


# In[ ]:




