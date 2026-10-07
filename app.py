import streamlit as st
import pandas as pd

st.set_page_config(page_title="StudySpot", page_icon="📚")
st.title("📚 StudySpot")
st.write("Find a study place that matches how you want to work today.")

spots = pd.read_csv("data/study_spots.csv")

quiet = st.slider("How important is quiet?", 1, 5, 4)
wifi = st.slider("How important is Wi-Fi?", 1, 5, 4)
seating = st.slider("How important is finding a seat?", 1, 5, 3)
mode = st.radio("How are you studying?", ["Solo", "Group"])

# Simple weighted score: intentionally transparent and easy to explain.
spots["score"] = (
    spots["quiet"] * quiet
    + spots["wifi"] * wifi
    + spots["seating"] * seating
    + spots["group_friendly"] * (5 if mode == "Group" else 1)
)

best = spots.sort_values("score", ascending=False).iloc[0]

st.subheader("Best match")
st.success(best["name"])
st.write(best["description"])
st.caption(f"Type: {best['type']} · Walk: {best['walk_minutes']} min")

with st.expander("Why this recommendation?"):
    st.write(
        f"{best['name']} scored well for your preferences. "
        "StudySpot uses a simple weighted score rather than a black-box model, "
        "so the recommendation is easy to understand and improve."
    )

st.subheader("Other options")
st.dataframe(
    spots.sort_values("score", ascending=False)[["name", "type", "walk_minutes", "score"]].head(4),
    hide_index=True,
)
