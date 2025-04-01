import random
import nltk
import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Dữ liệu về CNTT
it_knowledge = {
    "hệ điều hành": "Hệ điều hành là phần mềm quản lý tài nguyên phần cứng và cung cấp dịch vụ cho các chương trình máy tính. Ví dụ: Windows, Linux, macOS.",
    "ngôn ngữ lập trình": "Ngôn ngữ lập trình là công cụ để lập trình viên viết mã nguồn. Ví dụ: Python, Java, C++, JavaScript.",
    "database": "Cơ sở dữ liệu (database) là tập hợp có tổ chức của dữ liệu, có thể được truy vấn và quản lý dễ dàng. Ví dụ: MySQL, PostgreSQL, MongoDB.",
    "bảo mật": "Bảo mật thông tin là việc bảo vệ dữ liệu khỏi truy cập trái phép, tấn công hoặc phá hoại. Ví dụ: mã hóa dữ liệu, xác thực hai yếu tố, firewall.",
    "mạng máy tính": "Mạng máy tính là hệ thống kết nối nhiều máy tính để chia sẻ tài nguyên và dữ liệu. Ví dụ: mạng LAN, WAN, Internet.",
    "cloud computing": "Điện toán đám mây là mô hình cung cấp tài nguyên máy tính qua Internet thay vì lưu trữ trên máy tính cá nhân. Ví dụ: AWS, Google Cloud, Azure.",
    "big data": "Dữ liệu lớn (Big Data) là tập hợp dữ liệu có khối lượng lớn, đa dạng và tốc độ cao, đòi hỏi công nghệ đặc biệt để xử lý. Ví dụ: Hadoop, Spark.",
    "DevOps": "DevOps là phương pháp phát triển phần mềm kết hợp giữa phát triển (Dev) và vận hành (Ops) để tăng tốc độ triển khai và cải thiện chất lượng phần mềm.",
    "blockchain": "Blockchain là công nghệ lưu trữ dữ liệu phân tán, an toàn và minh bạch, thường được ứng dụng trong tiền mã hóa như Bitcoin, Ethereum.",
    "IoT": "Internet of Things (IoT) là mạng lưới các thiết bị kết nối Internet, có thể trao đổi dữ liệu và tự động hóa nhiều quy trình. Ví dụ: smart home, wearable devices.",
    "machine learning": "Machine Learning là một nhánh của AI cho phép máy tính học hỏi từ dữ liệu mà không cần lập trình rõ ràng. Ví dụ: nhận diện khuôn mặt, dự đoán tài chính."
}

# Định nghĩa các mẫu câu hỏi và phản hồi
pairs = [
    [
        r"xin chào|chào bạn|hello",
        ["Chào bạn!", "Xin chào!", "Hello, tôi có thể giúp gì cho bạn?"],
    ],
    [
        r"bạn tên là gì\??",
        ["Tôi là chatbot hỗ trợ bạn!", "Bạn có thể gọi tôi là trợ lý AI."],
    ],
    [
        r"tạm biệt|bye",
        ["Tạm biệt! Hẹn gặp lại bạn!", "Chúc bạn một ngày tốt lành!"],
    ],
    [
        r"(.*)",
        ["Xin lỗi, tôi chưa hiểu câu hỏi đó.", "Bạn có thể nói rõ hơn không?"],
    ],
]

# Khởi tạo chatbot
chatbot = Chat(pairs, reflections)

def chatbot_algorithm(user_input):
    """Thuật toán xử lý phản hồi chatbot."""
    user_input = user_input.lower() 
    for key in it_knowledge:
        if key in user_input:
            return it_knowledge[key]
    response = chatbot.respond(user_input)
    if response:
        return response
    else:
        return "Tôi chưa hiểu câu hỏi của bạn, vui lòng thử lại!"

def send_message():
    user_input = entry.get()
    if user_input.lower() in ["tạm biệt", "bye"]:
        chat_log.insert(tk.END, "Bạn: " + user_input + "\n", "user")
        chat_log.insert(tk.END, "Chatbot: Tạm biệt! Hẹn gặp lại bạn!\n", "bot")
        root.quit()
    else:
        response = chatbot_algorithm(user_input)
        chat_log.insert(tk.END, "Bạn: " + user_input + "\n", "user")
        chat_log.insert(tk.END, "Chatbot: " + response + "\n", "bot")
    entry.delete(0, tk.END)

# Giao diện Tkinter
root = tk.Tk()
root.title("Chatbot CNTT")
root.geometry("500x600")
root.configure(bg="#34495e")

chat_log = scrolledtext.ScrolledText(root, height=20, width=60, bg="#ecf0f1", fg="#2c3e50", font=("Arial", 12), wrap=tk.WORD, borderwidth=5, relief=tk.GROOVE)
chat_log.pack(pady=10, padx=10)
chat_log.tag_config("user", foreground="#2980b9", font=("Arial", 12, "bold"))
chat_log.tag_config("bot", foreground="#27ae60", font=("Arial", 12, "italic"))

entry_frame = tk.Frame(root, bg="#34495e")
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, width=40, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50", borderwidth=3, relief=tk.SUNKEN)
entry.grid(row=0, column=0, padx=10, pady=5)

send_button = tk.Button(entry_frame, text="Gửi", command=send_message, font=("Arial", 12, "bold"), bg="#3498db", fg="white", padx=15, pady=5, relief=tk.RAISED, borderwidth=3)
send_button.grid(row=0, column=1)

root.mainloop()