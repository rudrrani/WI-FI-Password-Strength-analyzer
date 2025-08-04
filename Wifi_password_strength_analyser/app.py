import streamlit as st
import streamlit as st
import base64

st.set_page_config(
    page_title="Wi-Fi Password Strength Analyzer",
    layout="centered"
)

# 🔧 Convert your local image to a base64 string
def get_base64_of_bin_file(bin_file_path):
    with open(bin_file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image_file):
    bin_str = get_base64_of_bin_file(image_file)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# ✅ Apply background
set_background("cyber.png")

st.set_page_config(
    page_title="Wi-Fi Password Strength Analyzer",
    layout="centered",  # use "wide" for full width if needed
    initial_sidebar_state="collapsed"
)

import streamlit as st
from strength_utils import calculate_entropy, classify_strength, estimate_crack_time, is_common_password
from chart import show_strength_chart_streamlit
from tips import give_tips, analyze_complexity

st.title("🔐 Wi-Fi Password Strength Analyzer")

password = st.text_input("Enter your Wi-Fi password", type="password")

if password:
    if is_common_password(password):
        st.warning("⚠️ This is a very common password!")

    entropy = calculate_entropy(password)
    category = classify_strength(entropy)
    crack_time = estimate_crack_time(entropy)

    st.metric("🧠 Entropy Score", entropy)
    st.metric("🔍 Strength", category)
    st.metric("⏳ Time to Crack", crack_time)

    show_strength_chart_streamlit(entropy)

    st.subheader("🔎 Password Complexity")
    complexity = analyze_complexity(password)
    for key, val in complexity.items():
        st.write(f"- {key}: {'✅' if val else '❌'}")

    st.subheader("🛠️ Tips to Improve")
    for tip in give_tips(password):
        st.write(f"• {tip}")
