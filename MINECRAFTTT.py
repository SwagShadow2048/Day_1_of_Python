import streamlit as st
import numpy as np

st.set_page_config(page_title="Mini Minecraft Demo", layout="wide")
st.title("🟩 Mini Minecraft-Style Block Builder")

# Available block types
BLOCK_TYPES = {
    "Air": "⬜",
    "Grass": "🟩",
    "Dirt": "🟫",
    "Stone": "⬛",
    "Water": "🟦"
}

# Initialize a 10x10 world
if "world" not in st.session_state:
    st.session_state.world = np.full((10, 10), "⬜", dtype=object)

# Block selector
selected_block = st.selectbox("Choose a block to place:", list(BLOCK_TYPES.keys()))

st.write("Click a tile to place your block:")

# Render grid
for i in range(10):
    cols = st.columns(10)
    for j in range(10):
        if cols[j].button(st.session_state.world[i][j], key=f"{i}-{j}"):
            st.session_state.world[i][j] = BLOCK_TYPES[selected_block]
            st.rerun()

# Reset button
if st.button("Reset World"):
    st.session_state.world = np.full((10, 10), "⬜", dtype=object)
    st.rerun()
