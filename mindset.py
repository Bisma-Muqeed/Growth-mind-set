#streamlit
import streamlit as st 

st.set_page_config(page_title="Growth Mindset Project", page_icon="🧠", layout='wide')
st.title("Growth Mindset Challange: Web App with Streamlit ")

st.header("🌟 **Welcome to Your Growth Journey ** 🚀")
st.write("*Embrace challenges, learn from mistakes, and unlock full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achivements! 🌟*")

#quote section
st.header("💡 Today's Growth Mindset Quote")
st.write('"Success is not final, failure is not fatal: it is the courage to continue that counts." - Winston Churchill')

st.header("💪✨ **What's Your Challenge Today?** 🚀🤔")
user_input = st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
    st.success(f"💪you are facing: {user_input}. Keep pushing forward towards your goal")
else:
    st.warning("Tell us about Your challenge to get started!")


#reflexing
st.header("Reflect on your Learning")
reflection = st.text_area("Write Your reflections here:")

if reflection:
    st.success(f"✨Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiencehelp you grow! Share Your difficulties")


#achivements
st.header("🎊 Celebrate Your Wins! 🎉")
achivement =st.text_input("Share something you've recently accomplished:")


if achivement:
    st.success(f"🎉 Amazing! You achieved: {achivement} 🏆")
else:
    st.info("Big or small, every achievement counts! 🌟✨ Share one now! 🚀💯")

#footer
st.write("---")
st.write("🌟 Keep believing in yourself. ✨ Growth is a journey, not a destination 🚀")
st.write("**Created by BISMA MUQEED**")
