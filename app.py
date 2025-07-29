import streamlit as st

# Streamlit page setup
st.set_page_config(page_title="Color Picker", page_icon="🎨")
st.title("🎨 Color Picker (Streamlit Version) by RUSHO")

# Switch (like your s1 trackbar)
switch = st.radio("Switch", ["OFF", "ON"])

# RGB sliders
r = st.slider("R", 0, 255, 0)
g = st.slider("G", 0, 255, 0)
b = st.slider("B", 0, 255, 0)

# Display color based on switch
if switch == "OFF":
    color = (0, 0, 0)  # Black
else:
    color = (r, g, b)

# Convert RGB to HEX
color_hex = "#{:02x}{:02x}{:02x}".format(*color)

# Show current color
st.write(f"**RGB:** {color}")
st.write(f"**HEX:** {color_hex}")

# Display color box
st.markdown(
    f"<div style='background-color:{color_hex}; width:500px; height:300px; border-radius:10px'></div>",
    unsafe_allow_html=True
)
