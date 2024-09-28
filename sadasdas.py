import streamlit as st
import matplotlib.pyplot as plt

# Dữ liệu ví dụ
months = ['January', 'February', 'March', 'April', 'May']
sales = [200, 300, 150, 400, 350]

# Vẽ biểu đồ cột
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(months, sales, color='skyblue')

# Thêm nhãn và tiêu đề
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Sales (in USD)', fontsize=12)
ax.set_title('Monthly Sales Data', fontsize=16)

# Hiển thị biểu đồ trên Streamlit
st.pyplot(fig)
