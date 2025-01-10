import streamlit as st
from streamlit_option_menu import option_menu


st.title("This page is available to super-admins")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")


# Using "with" notation

class ServeMe:

    def __init__(self):
        self.apps = []    

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func 
        })

    def run():

    
            app = option_menu(
                menu_title="ServeMe",
                options=["Dashboard", "Account"],
                icons=["house", "person"],
                menu_icon="waste",
                styles= {
                    "container": {"background-color": "#202125"},
                    "icon": {"color": "white", "font-size": "14px", "font-weight": "400", "text-decoration": "none"},
                    "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#00b370"},
                }
            )

            if app == "Dashboard":
                st.Page("dashboard.py")
            if app == "Account":
                st.Page("account.py")
            
    run()