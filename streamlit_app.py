import streamlit as st


# project title page 

st.set_page_config(
    page_title="ServeMe"
)

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Admin", "Super Admin"]


def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()

role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")

super_admin_1 = st.Page(
    "pages/super-admin.py",
    title="Super Admin 1",
    icon=":material/healing:",
    default=(role == "Super Admin"),
)

admin_1 = st.Page(
    "pages/admin.py",
    title="Admin 1",
    icon=":material/person_add:",
    default=(role == "Admin"),
)
admin_2 = st.Page("pages/user.py", title="Admin 2", icon=":material/security:")

dashboard = st.Page(
    "./pages/dashboard.py",
    title="Dashboard",
    # icon=":materiral/house",
        )

account = st.Page(
    "./pages/account.py",
    title="Account",
    # icon=":materiral/person",
        )

account_pages = [logout_page, settings]
super_admin_pages = [super_admin_1]
admin_pages = [admin_1, admin_2]
menu_pages = [dashboard, account]


# st.title("Request manager")
st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

page_dict = {}
if st.session_state.role in ["Admin", "Super Admin"]:
    page_dict["Admin"] = admin_pages
if st.session_state.role == "Super Admin":
    page_dict["Super Admin"] = super_admin_pages
    page_dict["Menu"] = menu_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()

