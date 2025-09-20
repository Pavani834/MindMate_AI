import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive", "Great! Keep up the positive vibes. Try some mood-boosting activities."
    elif polarity < -0.1:
        return "Negative", "It seems you're feeling down. Consider journaling or listening to calming music."
    else:
        return "Neutral", "Feeling neutral? Maybe try some relaxation exercises or meditation."

def main():
    st.title("MindMate AI - Mental Health Companion")
    
    st.write("Enter your feelings or thoughts below:")
    user_input = st.text_area("Your message")
    
    if st.button("Analyze Emotion") and user_input.strip() != "":
        emotion, recommendation = analyze_sentiment(user_input)
        st.write(f"Detected Emotion: {emotion}")
        st.write(recommendation)
        
if __name__ == "__main__":
    main()


