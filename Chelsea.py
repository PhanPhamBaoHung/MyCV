import streamlit as st
import matplotlib.pyplot as plt

# Hàm vẽ hình tròn
def draw_circle(x, y, radius, color, fill=True):
    circle = plt.Circle((x, y), radius, color=color, fill=fill)
    plt.gca().add_patch(circle)

# Hàm vẽ chữ
def draw_text(text, x, y, fontsize, color):
    plt.text(x, y, text, fontsize=fontsize, fontweight='bold', ha='center', va='center', color=color)

# Hàm vẽ logo Chelsea đơn giản
def draw_chelsea_logo():
    fig, ax = plt.subplots()

    # Thiết lập khung hình
    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    plt.axis('off')  # Tắt khung trục tọa độ

    # Vẽ vòng tròn lớn bên ngoài - đường viền xanh
    draw_circle(0, 0, 1.8, color='blue', fill=True)
    draw_circle(0, 0, 1.6, color='white', fill=True)

    # Vẽ vòng tròn nhỏ bên trong - nền xanh dương
    draw_circle(0, 0, 1.4, color='blue', fill=True)

    # Vẽ vòng tròn trung tâm - biểu tượng đơn giản
    draw_circle(0, 0, 0.6, color='white', fill=True)
    draw_circle(0, 0, 0.4, color='blue', fill=True)

    # Vẽ tên Chelsea ở phía trên
    draw_text("CHELSEA", 0, 1.2, fontsize=20, color='white')

    # Vẽ tên Football Club ở phía dưới
    draw_text("FOOTBALL CLUB", 0, -1.2, fontsize=15, color='white')

    # Hiển thị logo
    return fig

# Tạo giao diện với Streamlit
st.title("Chelsea Football Club Logo")

# Vẽ và hiển thị logo
fig = draw_chelsea_logo()
st.pyplot(fig)
