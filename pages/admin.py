import streamlit as st

st.title("This page is available to all admins")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

# pages = {
#     "Your account": [
#         st.Page("./pages/dashboard.py", title="Create your account"),
#         st.Page("./pages/account.py", title="Manage your account"),
#     ],
#     "Resources": [
#         st.Page("./pages/user.py", title="Learn about us"),
#         st.Page("./pages/super-admin.py", title="Try it out"),
#     ],
# }

# pg = st.navigation(pages)
# pg.run()