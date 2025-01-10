import streamlit as st

# Page configuration
st.set_page_config(page_title="ServeMe", layout="wide")

# Define roles and pages
ROLES = [None, "Admin", "Super Admin"]
PAGES = {
    "Dashboard": lambda: st.write("Welcome to the Dashboard!"),
    "Settings": lambda: st.write("Settings Page"),
    "Admin Page": lambda: st.write("Admin Page"),
    "Super Admin Page": lambda: st.write("Super Admin Page"),
}

# Session state initialization
if "role" not in st.session_state:
    st.session_state.role = None

def login():
    st.title("Log in")
    role = st.selectbox("Choose your role", ROLES)
    if st.button("Log in"):
        st.session_state.role = role

def app():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(PAGES.keys()))
    PAGES[page]()

    if st.sidebar.button("Log out"):
        st.session_state.role = None

# Main flow
if st.session_state.role is None:
    login()
else:
    app()
