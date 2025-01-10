import streamlit as st
from streamlit_option_menu import option_menu

import dashboard, account

st.set_page_config(
    page_title="ServeMe"
)
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

        with st.sidebar:
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
                dashboard.app()
            if app == "Account":
                account.app()
            
    run()