#importing necessary libraries
import streamlit as st
import pandas as pd
import pickle as pkl
import matplotlib.pyplot as plt
import time







#setiing page title, icon and layout
st.set_page_config(page_title="Cricklytics: IPL Match Predictor", page_icon="/Users/siddharthjain/Desktop/SJ/cuvette/python ML program/Add On Projects/IPL Prediction by me/IPL_LOGO.png", layout="wide", initial_sidebar_state="expanded")

st.image("IPL_LOGO.png", width=100)
st.title("🏏 Cricklytics: IPL Match Predictor") #page title


#Importing data and model from pickle files
teams = pkl.load(open('teams.pkl', 'rb'))
cities = pkl.load(open('city.pkl', 'rb'))
model = pkl.load(open('model.pkl', 'rb'))

#first row and columns
col1, col2, col3 = st.columns(3)
#first column
with col1:
    batting_team = st.selectbox("Select Batting Team", options=sorted(teams))

#second column
with col2:
    bowling_team = st.selectbox("Select Bowling Team", options=sorted(teams))

#third column
with col3:
    selected_city = st.selectbox("📍Select Host City", options=cities)


target = st.number_input("Target Score", min_value = 0, max_value = 1000, step = 1)



#second row and columns
col4, col5, col6 = st.columns(3)
#fourth column
with col4:
    score = st.number_input("Current_Score", min_value = 0, max_value = 1000, step = 1)
#fifth column
with col5:
    overs = st.number_input("Overs Done", min_value = 0, max_value = 20, step = 1)
#sixth column
with col6:
    wickets = st.number_input("Wickets", min_value = 0, max_value = 10, step = 1)

#team colors
team_colors = {
    'Sunrisers Hyderabad': '#F26522',       # Orange
    'Mumbai Indians': '#045093',            # Blue
    'Gujarat Titans': '#1C1C1C',            # Dark gray / black
    'Royal Challengers Bangalore': '#DA1818',  # Red
    'Kolkata Knight Riders': '#3A225D',     # Purple
    'Delhi Capitals': '#17449B',            # Blue
    'Kings XI Punjab': '#D71920',           # Red
    'Chennai Super Kings': '#FDB913',       # Yellow
    'Rajasthan Royals': '#EA1A7F',          # Pink
}


#button to predict
def making_prediction():
    msg = st.toast("Gathering information...")
    time.sleep(2)
    msg.toast('Making prediction...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🏏")

if st.button("Predict Win Probability"):
    making_prediction()
    

# if st.button(""):
    if score == 0 or overs == 0 or target <= score:
        st.error("⚠️ ❌ Invalid Input: Target, Score, and Overs must be non-zero values.")
        st.stop()
    else:
        runs_left = target - score
        balls_left = (20 - overs) * 6
        wickets_left = 10 - wickets
        CRR = score / overs
        RRR = (runs_left * 6) / balls_left if balls_left != 0 else 0
    
    runs_left = target - score
    balls_left = (20 - overs) * 6
    wickets_left = 10 - wickets
    CRR = score/overs
    RRR = (runs_left*6)/balls_left

    #creating a dataframe with the input values
    input_data = pd.DataFrame({'batting_team' : [batting_team],
                               'bowling_team' : [bowling_team],
                               'city' : [selected_city],
                               'Score': [score],
                               'Wickets Left' : [wickets_left],
                               'Remaining Balls': [balls_left], 
                               'target_left': [runs_left], 
                               'CRR' : [CRR], 
                               'RRR' : [RRR]
                               })
    
    result = model.predict_proba(input_data)
    # print(result)
    # print(type(result))
    loss = result[0][0]
    win = result[0][1]


    # store in session_state
    st.session_state.win = win
    st.session_state.loss = loss
    st.session_state.score = score
    st.session_state.target = target
    st.session_state.batting_team = batting_team
    st.session_state.bowling_team = bowling_team



    st.header("Win Probability")
    st.write(f'{batting_team} - {round(win*100, 2)}%')
    st.write(f'{bowling_team} - {round(loss*100, 2)}%')

    # Horizontal win probability bar
    fig, ax = plt.subplots(figsize=(8, 0.5))

    # Bar for win percentage (batting team)
    ax.barh(0, win * 100, color=team_colors[batting_team], height=0.3)
    # Bar for loss percentage (bowling team)
    ax.barh(0, loss * 100, left=win * 100, color=team_colors[bowling_team],  height=0.3)

    # Text labels inside the bars
    ax.text(win * 50, 0, f"{batting_team}: {win*100:.1f}%", va='center', ha='center', color='black', fontsize=5)
    ax.text(win * 100 + loss * 50, 0, f"{bowling_team}: {loss*100:.1f}%", va='center', ha='center', color='black', fontsize=5)

    # Remove axes
    ax.axis('off')
    st.pyplot(fig)

if st.button("Show Win Probability Visuals") and 'win' in st.session_state:
    with st.spinner("Wait for it...", show_time=True):
        time.sleep(5)
    st.success("Done!")
    
        
    #retrieving values from session_state
    win = st.session_state.win
    loss = st.session_state.loss
    score = st.session_state.score
    target = st.session_state.target
    batting_team = st.session_state.batting_team
    bowling_team = st.session_state.bowling_team
    

    


#creating two columns for the visuals
    st.header("Win Probability Visuals")
    col1, col2 = st.columns(2)
    #first column
    with col1:
        #plotting the win probability dounut chart
        labels = [batting_team, bowling_team]
        sizes = [win*100, loss*100]
        colors = [team_colors[batting_team], team_colors[bowling_team]]
        explode = (0.1, 0)  # explode the first slice (batting team)
        fig, ax = plt.subplots(figsize=(3, 3))  # Create a figure and axis
        #ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=50, shadow=True)
        # Create donut chart
        wedges, texts, autotexts = ax.pie(
            sizes,
            explode=explode,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            startangle=50,
            shadow=True,
            wedgeprops=dict(width=0.4)  # Donut hole
    )

        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)
        
    
    #second column:
    with col2:
        
        #displaying bar chart for score  and target 
        fig, ax = plt.subplots(figsize=(2, 2))
        labels = ['Current_Score', 'Target']
        values = [score, target]
        colors = [team_colors[batting_team], team_colors[bowling_team]]

        #plot
        fig,ax = plt.subplots(figsize=(8, 6))
        bars = ax.bar(labels, values, color=colors)
        ax.set_title(f"{batting_team} vs {bowling_team} - Score vs Target")

        #trendline
        ax.axhline(y=score, color='green', linestyle = ':', label='Current Score')

        #labels on bar as team names
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{height}', ha='center', fontsize=10)
        
        ax.set_ylabel('Runs')
        ax.set_title('Score Comparison')
        ax.legend()
        st.pyplot(fig)

        

    #footer
    st.markdown(''' Made with ❤️ by **Siddharth Jain** ''')

    st.markdown(''' https://www.linkedin.com/in/siddharth-jain-8b56a2321/''')
    st.markdown(''' https://github.com/S-AILAB ''')