import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import os


st.title("Collect Digit Data")


digit = st.number_input(
    "Enter digit label",
    min_value=0,
    max_value=9
)


canvas = st_canvas(
    fill_color="black",
    stroke_width=10,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="collector"
)


if st.button("Save Image"):

    if canvas.image_data is not None:

        img = Image.fromarray(
            canvas.image_data.astype("uint8")
        )

        img = img.convert("L")

        img = img.resize((28,28))

        folder = f"my_digits/{digit}"

        os.makedirs(folder, exist_ok=True)

        count = len(os.listdir(folder))

        img.save(
            f"{folder}/{count}.png"
        )

        st.success("Saved!")