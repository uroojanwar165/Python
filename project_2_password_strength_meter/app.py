import streamlit as st
import re

# Function to check password strength
def checking_password_strength(password):
    score = 0

    # Checking length
    if len(password) >= 8:
        score += 1

    # Checking upper case
    if re.search(r"[A-Z]", password):
        score += 1

    # Checking lower case
    if re.search(r"[a-z]", password):
        score += 1

    # Checking digits 
    if re.search(r"[0-9]", password):
       score += 1

    # Checking special characters
    if re.search(r"[! @ # $ % ^ & *]", password):
       score += 1

    return score

# Streamlit interface
st.title("Password Strength Meter")

# Get user input
password = st.text_input("Enter your password:", type = "password")

# Button for checking password strength
if st.button("Check Strength"):
    if password:
        # Get password strength score
        strength_score = checking_password_strength(password)

        # Display the progress bar
        progress = strength_score / 5
        st.write(f"Score: {strength_score}/5")  # Display the score (e.g., 1/5, 2/5, etc.)
        st.progress(progress)

        # Strength Rating
        if strength_score == 5:
            st.success("✅ Strong password!")
        elif strength_score == 4:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestion below:")

        # Suggestion based on score
        if strength_score < 5:
            if len(password) < 8:
                st.write("❌ Password should be at least 8 characters long.")
            if not re.search(r"[A-Z]", password):
                st.write("❌ Include at least one Upper Case letters.")
            if not re.search(r"[a-z]", password):
                st.write("❌ Include at least one Lower Case letters.")
            if not re.search(r"[0-9]", password):
                st.write("❌ Include at least one number [0-9].")
            if not re.search(r"[! @ # $ % ^ & *]", password):
                st.write("❌ Include at least one special character [! @ # $ % ^ & *].")
    else:
        st.warning("⚠️ Please enter a password first!")