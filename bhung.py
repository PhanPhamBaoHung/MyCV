import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Tiêu đề ứng dụng
st.title("Ứng dụng Biểu đồ với Streamlit")

# Tạo dữ liệu
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Vẽ biểu đồ
plt.figure(figsize=(10, 5))
plt.plot(x, y, marker='o')
plt.title("Biểu đồ hàm số y = sin(x)")
plt.xlabel("Giá trị x")
plt.ylabel("Giá trị y")
plt.grid(True)

# Hiển thị biểu đồ trong Streamlit
st.pyplot(plt)
