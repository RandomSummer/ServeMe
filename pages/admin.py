import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.title("This page is available to all admins")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

# chart_data = pd.DataFrame(
#     "../simulated_waste_bins.csv",
#     columns=["location_lat", "location_lon"],
# )

# st.pydeck_chart(
#     pdk.Deck(
#         map_style=None,
#         initial_view_state=pdk.ViewState(
#             latitude=23.074893,
#             longitude=76.855259,
#             zoom=11,
#             pitch=50,
#         ),
#         layers=[
#             pdk.Layer(
#                 "HexagonLayer",
#                 data=chart_data,
#                 get_position="[lon, lat]",
#                 radius=200,
#                 elevation_scale=4,
#                 elevation_range=[0, 1000],
#                 pickable=True,
#                 extruded=True,
#             ),
#             pdk.Layer(
#                 "ScatterplotLayer",
#                 data=chart_data,
#                 get_position="[lon, lat]",
#                 get_color="[200, 30, 0, 160]",
#                 get_radius=200,
#             ),
#         ],
#     )
# )