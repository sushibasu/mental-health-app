import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Title of the website
st.title("🌱 Mental Health Support Website")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Well-being Tips", "Mood Tracker", "Journal"])

# Home Page
if page == "Home":
    st.header("Welcome 💚")
    st.write("This is a safe space for you to relax, reflect, and take care of your mental health.")
    st.image("https://images.unsplash.com/photo-1507537297725-24a1c029d3ca", caption="Take a deep breath 🌿")

# Well-being Tips Page
elif page == "Well-being Tips":
    st.header("Daily Well-being Tips ✨")
    tips = [
        "Take 5 deep breaths slowly.",
        "Go for a short walk outside.",
        "Write down 3 things you're grateful for.",
        "Drink water and stay hydrated.",
        "Talk to a trusted friend or family member."
    ]
    for tip in tips:
        st.success(tip)

# Mood Tracker Page
elif page == "Mood Tracker":
    st.header("How are you feeling today? 📝")
    mood = st.selectbox("Select your mood:", ["😊 Happy", "😔 Sad", "😡 Angry", "😌 Calm", "😴 Tired"])
    
    if st.button("Submit Mood"):
        # Save mood in CSV
        new_entry = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d %H:%M:%S"), mood]], 
                                 columns=["Date", "Mood"])
        if os.path.exists("moods.csv"):
            old_data = pd.read_csv("moods.csv")
            data = pd.concat([old_data, new_entry], ignore_index=True)
        else:
            data = new_entry
        data.to_csv("moods.csv", index=False)
        st.success(f"Your mood ({mood}) has been recorded! 💌")

    # Show mood history chart
    if os.path.exists("moods.csv"):
        st.subheader("📊 Your Mood History")
        data = pd.read_csv("moods.csv")
        st.line_chart(data.set_index("Date")["Mood"].value_counts())
        st.table(data.tail(5))  # Show last 5 entries

# Journal Page
elif page == "Journal":
    st.header("Personal Journal 📖")
    note = st.text_area("Write your thoughts here:")
    if st.button("Save Entry"):
        with open("journal.txt", "a") as f:
            f.write(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {note}")
        st.success("Your entry has been saved! 💌")
