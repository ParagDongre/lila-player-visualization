import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(layout="wide")

st.title("LILA Player Journey Visualization Tool")

# Load data
import os
import pandas as pd

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "backend", "events.csv")

df = pd.read_csv(csv_path)

# Clean event column
df["event"] = df["event"].astype(str)

# Convert timestamp
df["ts"] = pd.to_datetime(df["ts"])

# Sidebar filters
st.sidebar.header("Filters")

map_filter = st.sidebar.selectbox(
    "Select Map",
    df["map_id"].unique()
)

match_filter = st.sidebar.selectbox(
    "Select Match",
    df["match_id"].unique()
)

show_heatmap = st.sidebar.checkbox("Show Heatmap", True)

# Filter data
filtered = df[
    (df["map_id"] == map_filter) &
    (df["match_id"] == match_filter)
]

st.write("Total Events:", len(filtered))

# Timeline slider
filtered["ts_num"] = filtered["ts"].astype("int64") // 10**9

min_time = int(filtered["ts_num"].min())
max_time = int(filtered["ts_num"].max())

if min_time == max_time:
    time_selected = min_time
else:
    time_selected = st.slider(
        "Match Timeline",
        min_value=min_time,
        max_value=max_time,
        value=min_time
    )

timeline_data = filtered[filtered["ts_num"] <= time_selected]

# ------------------------
# Player Journeys
# ------------------------

st.subheader("Player Journeys")

journey_fig = px.line(
    timeline_data,
    x="x",
    y="y",
    color="user_id"
)

st.plotly_chart(journey_fig, use_container_width=True)

# ------------------------
# Game Events + Minimap
# ------------------------

st.subheader("Game Events")

event_fig = px.scatter(
    timeline_data,
    x="x",
    y="y",
    color="event",
    symbol="event"
)

minimap_dict = {
    "AmbroseValley": "minimaps/AmbroseValley_Minimap.png",
    "GrandRift": "minimaps/GrandRift_Minimap.png",
    "Lockdown": "minimaps/Lockdown_Minimap.jpg"
}

minimap_path = minimap_dict.get(map_filter)

if minimap_path:
    event_fig.update_layout(
        images=[
            dict(
                source=Image.open(minimap_path),
                xref="x",
                yref="y",
                x=timeline_data["x"].min(),
                y=timeline_data["y"].max(),
                sizex=timeline_data["x"].max() - timeline_data["x"].min(),
                sizey=timeline_data["y"].max() - timeline_data["y"].min(),
                sizing="stretch",
                opacity=0.6,
                layer="below"
            )
        ]
    )

st.plotly_chart(event_fig, use_container_width=True)

# ------------------------
# Heatmap
# ------------------------

if show_heatmap:

    st.subheader("Player Activity Heatmap")

    heatmap = px.density_heatmap(
        timeline_data,
        x="x",
        y="y"
    )

    st.plotly_chart(heatmap, use_container_width=True)
