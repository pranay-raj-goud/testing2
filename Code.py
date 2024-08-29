import streamlit as st
# Set the title of the app
st.title("Display Image from GitHub")
# URL of the image in your GitHub repository
image_url = "https://raw.githubusercontent.com/pranay-raj-goud/testing2/main/Pic.png"
# Display the image with a caption
st.image(image_url, caption="Sample Image from GitHub", use_column_width=True
