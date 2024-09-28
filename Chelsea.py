import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Hàm vẽ logo Chelsea đơn giản
def draw_logo():
    fig, ax = plt.subplots(figsize=(6, 6))

    # Vẽ hình tròn
    circle = plt.Circle((0.5, 0.5), 0.4, color='#003DA5', ec='white', lw=8)
    ax.add_artist(circle)

    # Vẽ chữ "Chelsea"
    ax.text(0.5, 0.5, 'Chelsea', color='white', fontsize=30, ha='center', va='center', fontweight='bold')

    # Thiết lập trục
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    plt.axis('off')

    return fig

# Tiêu đề ứng dụng
st.title("Logo Chelsea Đơn Giản")

# Vẽ logo
logo_fig = draw_logo()
st.pyplot(logo_fig)
