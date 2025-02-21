import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Growth Mindset Project",
    page_icon="🧠",
    layout='wide'
)

# Custom CSS for professional look
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
            padding: 20px;
            font-family: 'Arial', sans-serif;
        }
        .title, .header {
            text-align: center;
            color: #333333;
        }
        .stTextInput>div>div>input, .stTextArea>div>textarea {
            border-radius: 10px;
            border: 1px solid #ccc;
            padding: 10px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 24px;
            font-size: 16px;
        }
        .footer {
            text-align: center;
            font-size: 18px;
            color: #555;
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Introduction
st.title("🚀 Growth Mindset Challenge: Web App with Streamlit 🧠")
st.header("🌟 **Welcome to Your Growth Journey** 🚀")
st.write("""
*Embrace challenges, learn from mistakes, and unlock your full potential.*
This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟
""")

# Quote Section
st.header("💡 Today's Growth Mindset Quote")
st.info("\"Success is not final, failure is not fatal: it is the courage to continue that counts.\" - Winston Churchill")

# Challenge Section
st.header("💪✨ **What's Your Challenge Today?** 🚀🤔")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 You are facing: {user_input}. Keep pushing forward towards your goal!")
else:
    st.warning("⚡ Tell us about your challenge to get started!")

# Reflection Section
st.header("📝 Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"✨ Great insight! Your reflection: {reflection}")
else:
    st.info("💡 Reflecting on past experiences helps you grow! Share your thoughts.")

# Achievements Section
st.header("🎊 Celebrate Your Wins! 🎉")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🎉 Amazing! You achieved: {achievement} 🏆")
else:
    st.info("🌟 Big or small, every achievement counts! 🚀 Share one now!")

# Footer Section
st.markdown("""
    <div class='footer'>
        🌟 Keep believing in yourself. ✨ Growth is a journey, not a destination 🚀<br>
        <strong>Created by BISMA MUQEED</strong>
    </div>
""", unsafe_allow_html=True)  
