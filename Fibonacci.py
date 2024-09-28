import streamlit as st
import matplotlib.pyplot as plt

# Hàm tính dãy Fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

# Tiêu đề ứng dụng
st.title("Ứng dụng Biểu đồ Dãy Fibonacci")

# Nhập số lượng phần tử Fibonacci từ người dùng
n = st.number_input("Nhập số lượng phần tử trong dãy Fibonacci:", min_value=2, value=10)

# Tính dãy Fibonacci
fib_sequence = fibonacci(n)

# Vẽ biểu đồ
plt.figure(figsize=(10, 5))
plt.plot(fib_sequence, marker='o', label='Dãy Fibonacci', color='blue')
plt.title("Biểu đồ Dãy Fibonacci")
plt.xlabel("Chỉ số")
plt.ylabel("Giá trị")
plt.grid()
plt.legend()

# Hiển thị biểu đồ trong Streamlit
st.pyplot(plt)
