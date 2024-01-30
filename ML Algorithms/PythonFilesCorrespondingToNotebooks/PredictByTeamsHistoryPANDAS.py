#!/usr/bin/env python
# coding: utf-8

# In[2]:


teamnames = ['Arsenal', 'Aston Villa', 'Brentford', 'Brighton & Hove Albion', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds United', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Nottingham Forest', 'Southampton', 'Tottenham Hotspur', 'West Ham United']


# In[3]:


import pandas as pd
from string import ascii_uppercase as alphabet
import pickle
from scipy.stats import poisson
# !pip install scipy

df_history_data = pd.read_csv('historical_data.csv')
df_history_data.to_csv('historical_data.csv',index=False)

df_home = df_history_data[['HomeTeam', 'HomeGoals', 'AwayGoals']]
df_away = df_history_data[['AwayTeam', 'HomeGoals', 'AwayGoals']]

df_home = df_home.rename(columns={'HomeTeam':'Team','HomeGoals': 'GoalsScored', 'AwayGoals':'GoalsConceded'})
df_away = df_away.rename(columns={'AwayTeam':'Team','HomeGoals': 'GoalsConceded', 'AwayGoals':'GoalsScored'})

df_team_strength = pd.concat([df_home,df_away],ignore_index=True).groupby('Team').mean() 

def predict_points(home,away):
    if home in df_team_strength.index and away in df_team_strength.index:
        lambda_home = df_team_strength.at[home,'GoalsScored']*df_team_strength.at[away,'GoalsConceded']
        lambda_away = df_team_strength.at[away,'GoalsScored']*df_team_strength.at[home,'GoalsConceded']
        prob_home, prob_away,prob_draw = 0,0,0
        for x in range(0,11):#A match can have only 0 to 10 goals
            for y in range(0,11):
                p = poisson.pmf(x,lambda_home)*poisson.pmf(y, lambda_away)
                if x == y:
                    prob_draw += p
                elif x > y:
                    prob_home += p
                else:
                    prob_away += p
        points_home = 3 * prob_home + prob_draw
        points_away = 3 * prob_away + prob_draw
        return(points_home,points_away)
    else:
        return(0,0)
    
    teamnames = ['Arsenal', 'Aston Villa', 'Brentford', 'Brighton & Hove Albion', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds United', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Nottingham Forest', 'Southampton', 'Tottenham Hotspur', 'West Ham United']

print("Enter first team:")
team1 = input().strip()
while team1 not in teamnames:
    print("Invalid team name. Please enter a team from the list:")
    team1 = input().strip()

print("Enter second team:")
team2 = input().strip()
while team2 not in teamnames:
    print("Invalid team name. Please enter a team from the list:")
    team2 = input().strip()

score1, score2 = predict_points(team1, team2)

score1_rounded = round(score1)
score2_rounded = round(score2)

if score1_rounded > score2_rounded:
    print(f"The predicted winner is {team1} with {score1_rounded} goals.")
elif score2_rounded > score1_rounded:
    print(f"The predicted winner is {team2} with {score2_rounded} goals.")
else:
    print(f"The match between {team1} and {team2} is predicted to be a draw with both teams having {score1_rounded} goals.")



# In[ ]:




