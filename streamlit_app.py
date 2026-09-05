from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="OPP Seminar",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .stApp {
            background: #eef8fc;
        }

        .block-container {
            max-width: 100%;
            padding: 0;
        }

        header[data-testid="stHeader"] {
            display: none;
        }

        footer {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "index.html"

if not html_path.exists():
    st.error("index.html blev ikke fundet.")
    st.stop()

html_code = html_path.read_text(encoding="utf-8")

components.html(
    html_code,
    height=7000,
    scrolling=True,
)
