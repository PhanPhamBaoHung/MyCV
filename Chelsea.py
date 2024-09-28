import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Hàm vẽ hình tròn
def draw_circle(x, y, radius, color, fill=True):
    circle = plt.Circle((x, y), radius, color=color, fill=fill)
    plt.gca().add_patch(circle)

# Hàm vẽ hình bầu dục
def draw_ellipse(x, y, width, height, angle, color):
    ellipse = plt.Ellipse((x, y), width, height, angle=angle, color=color)
    plt.gca().add_patch(ellipse)

# Hàm vẽ miệng
def draw_mouth(x, y, width, height, color):
    mouth = plt.Rectangle((x - width / 2, y), width, height, color=color)
    plt.gca().add_patch(mouth)

# Hàm vẽ mắt
def draw_eyes():
    # Mắt trái
    draw_circle(-0.4, 0.3, 0.25, color='white')
    draw_circle(-0.4, 0.3, 0.1, color='black')
    # Mắt phải
    draw_circle(0.4, 0.3, 0.25, color='white')
    draw_circle(0.4, 0.3, 0.1, color='black')

# Hàm vẽ hình tổng thể
def draw_frog_face():
    fig, ax = plt.subplots()

    # Thiết lập khung hình
    ax.set_aspect('equal')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    plt.axis('off')  # Tắt khung trục tọa độ

    # Vẽ đầu (hình tròn)
    draw_circle(0, 0, 1, color='green')

    # Vẽ mắt
    draw_eyes()

    # Vẽ miệng
    draw_mouth(0, -0.5, 1, 0.1, color='brown')

    # Hiển thị logo
    return fig

# Tạo giao diện với Streamlit
st.title("Simple Frog Face Drawing")

# Vẽ và hiển thị hình ảnh
fig = draw_frog_face()
st.pyplot(fig)
