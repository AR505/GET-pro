# استيراد مكتبة customtkinter (نسخة مطورة من tkinter)
import customtkinter as ctk
from tkinter import messagebox

# تفعيل الثيم الحديث واللون العام (dark أو light)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# إنشاء نافذة اللعبة
root = ctk.CTk()
root.title("لعبة X O المطورة 🎮")
root.geometry("400x450")

# ضبط الخلفية بلون مميز
root.configure(fg_color=("#20232a"))  # خلفية داكنة شيك

# المتغير اللي بيحدد اللاعب الحالي
player = "O"

# مصفوفة اللعبة (9 خانات فاضية)
board = [""] * 9

# قائمة الأزرار
buttons = []

# دالة عند الضغط على الزر
def click(index):
    global player
    # لو المربع فاضي
    if board[index] == "":
        board[index] = player
        # تغيير نص الزر وشكله
        buttons[index].configure(text=player, fg_color="#0078ff" if player == "O" else "#ff006e")
        buttons[index].configure(state="disabled")

        # التحقق من الفوز
        if check_winner():
            messagebox.showinfo("🏆result ", f" player {player} winner")
            reset()
        elif "" not in board:
            messagebox.showinfo("تعادل", "مفيش فائز المره دي!")
            reset()
        else:
            # تبديل الدور
            player = "X" if player == "O" else "O"

# دالة التحقق من الفوز
def check_winner():
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # صفوف
        (0,3,6), (1,4,7), (2,5,8),  # أعمدة
        (0,4,8), (2,4,6)            # أقطار
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != "":
            return True
    return False

# دالة لإعادة تشغيل اللعبة
def reset():
    global board, player
    board = [""] * 9
    player = "O"
    for b in buttons:
        b.configure(text="", fg_color="#3b3b3b", state="normal")#الاعدادات تتغير من هنا

# عنوان اللعبة في الأعلى
title_label = ctk.CTkLabel(root, text="X Game O  ", font=("Arial", 26, "bold"), text_color="#00ffff")
title_label.pack(pady=20)

# إطار (Frame) يحتوي على الأزرار
frame = ctk.CTkFrame(root, fg_color="#282c34", corner_radius=15)
frame.pack(padx=20, pady=10, fill="both", expand=True)

# إنشاء شبكة الأزرار (3×3)
for i in range(9):
    btn = ctk.CTkButton(
        frame,
        text="",
        width=100,
        height=100,
        font=("Arial", 24, "bold"),
        fg_color="#3b3b3b",
        corner_radius=20,  # يخلي الزر مدوّر الأطراف
        hover_color="#505050",  # اللون عند المرور بالماوس
        command=lambda i=i: click(i)
    )
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# تشغيل البرنامج
root.mainloop()
print (" good ") 