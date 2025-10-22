import streamlit as st

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Toren Kochman"
PROGRAM = "Computer Science"
INTRO = (
    "I study computer science at MSU Denver, and some of my favorite classes revolve around logic, theoretical computer science, and sciences in general. "
    "I enjoy seeing the more complex and in depth components of how we make machines work and how we use mathematics to understand the world around us."
)
FUN_FACTS = [
    "I love video games of all types",
    "I’m learning how to code and utilize it to make programs that I find useful",
    "I want to build my own game at some point in the future",
]

PHOTO_PATH = "../../streamlit_CS/assets/your_photo.jpg"  # Put a file in repo root or set a URL

import os

st.write("Current working directory:", os.getcwd())
st.write("Absolute photo path:", os.path.abspath(PHOTO_PATH))
st.write("Does file exist?:", os.path.exists(PHOTO_PATH))

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception:
        st.info("Add a photo named `your_photo.jpg` to the repo root, or change PHOTO_PATH.")
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
