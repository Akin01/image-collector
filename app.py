import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False)

st.header("Image Cropping")
img_file = st.sidebar.file_uploader(
    label='Upload a photo', type=['png', 'jpg'])

box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')

if 'img_col' not in st.session_state:
    st.session_state.img_col = []
elif 'img_query' not in st.session_state:
    st.session_state.img_query = []

option = st.selectbox(
    "Image Type",
    ("Image Collection", "Image Query"),
)

if img_file:
    img = Image.open(img_file)

    cropped_img = st_cropper(img, realtime_update=True, box_color=box_color)

    btn_add, btn_clear_C, btn_clear_Q, _ = st.columns([2, 4, 4, 8])

    with btn_add:
        if cropped_img and st.button('add'):
            if option == "Image Collection":
                st.session_state.img_col.append(cropped_img)
            elif option == "Image Query":
                st.session_state.img_query.append(cropped_img)

    with btn_clear_C:
        if st.button('clear collection'):
            st.session_state.img_col = []

    with btn_clear_Q:
        if st.button('clear query'):
            st.session_state.img_query = []


img_col_picked = st.session_state.img_col
img_query_picked = st.session_state.img_query

if len(img_col_picked):
    st.markdown('#### Image Collection')
    st.image(img_col_picked, width=100)

if len(img_query_picked):
    st.markdown('#### Image Query')
    st.image(img_query_picked, width=100)

st.markdown("#### Image Data")
with st.expander("Show"):
    st.json(st.session_state)
