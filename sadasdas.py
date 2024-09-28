import matplotlib.pyplot as plt
import streamlit

# Dữ liệu
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Vẽ biểu đồ
plt.plot(x, y, marker='o')

# Thêm tiêu đề và nhãn
plt.title('Biểu đồ hàm số y = x^2')
plt.xlabel('Giá trị x')
plt.ylabel('Giá trị y')

# Hiển thị biểu đồ
plt.grid(True)
plt.show()
