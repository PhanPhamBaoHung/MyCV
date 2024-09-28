import streamlit as st
from PIL import Image

# Tải ảnh logo Chelsea
logo = Image.open("chelsea_logo.png")  # Thay bằng đường dẫn tới file logo Chelsea

# Tiêu đề của ứng dụng
st.title("Chelsea Football Club Logo")

# Hiển thị logo Chelsea
st.image(logo, caption='Chelsea FC', use_column_width=True)
