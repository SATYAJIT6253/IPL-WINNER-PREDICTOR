import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
         'Mumbai Indians',
         'Royal Challengers Bangalore',
         'Kolkata Knight Riders',
         'Kings XI Punjab',
         'Chennai Super Kings',
         'Rajasthan Royals',
         'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali']

st.title('IPL WIN PREDICTOR')
pipe = pickle.load(open('pipe.pkl', 'rb'))

batting_team = st.selectbox('Select the batting team',sorted(teams))
bowling_team = st.selectbox('Select the bowling team',sorted(teams))
selected_city = st.selectbox('Select host city',sorted(cities))
target = st.number_input('Select Target')
score = st.number_input('Give the Score')
overs = st.number_input('Overs completed')
wickets = st.number_input('Wickets out')
if st.button('Predict Probability'):
    run_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    if overs == 0:
        curr = 0
    else :
        curr = score/overs
    reqr = (run_left * 6) / balls_left

    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city],
                             'run_left': [run_left], 'balls_left': [balls_left], 'wickets_left': [wickets],
                             'total_runs_x': [target], 'curr': [curr], 'reqr': [reqr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.subheader(batting_team + "- " + str(round(win * 100)) + "%")
    st.subheader(bowling_team + "- " + str(round(loss * 100)) + "%")