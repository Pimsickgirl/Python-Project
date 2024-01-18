import tkinter as tk
from tkinter import messagebox

def convert_to_cm(height_cm):
    return height_cm / 100

def calculate_bmi():

    weight = float(entry_weight.get())
    height_cm = float(entry_height.get())

    height = convert_to_cm(height_cm)
    bmi_result = weight / (height ** 2)

    if bmi_result < 18.5:
        interpretation = "น้ำหนักน้อย (Underweight)"
    elif 18.5 <= bmi_result < 24.9:
        interpretation = "น้ำหนักปกติ (Normal weight)"
    elif 25 <= bmi_result < 29.9:
        interpretation = "ท้วม (Overweight)"
    else:
        interpretation = "อ้วน (Obese)"

    label_result.config(text=f"ดัชนีมวลกาย (BMI): {bmi_result:.2f}\nผลลัพธ์: {interpretation}", font=('Angsana New', 14), fg='#333')

def on_closing():
    if messagebox.askokcancel("ยืนยัน", "คุณต้องการปิดโปรแกรมหรือไม่?"):
        messagebox.showinfo("ขอบคุณ!", ":)\nดูแลสุขภาพตัวเองด้วยนะ")
        window.destroy()

#สร้างหน้าต่าง GUI
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x300")
window.configure(bg='#f0f0f0')
window.iconbitmap("jinky.ico")

#ไม่ให้ผู้ใช้ปรับขนาด GUI
window.resizable(width=False, height=False)

# สร้างวิตเจ็ตและเพิ่มลงใน GUI
label_weight = tk.Label(window, text="น้ำหนัก (กิโลกรัม):", font=('Angsana New', 16), bg='#f0f0f0')
label_weight.grid(row=0, column=0, padx=10, pady=10)
entry_weight = tk.Entry(window, font=('Angsana New', 16))
entry_weight.grid(row=0, column=1, padx=10, pady=10)

label_height = tk.Label(window, text="ส่วนสูง (เมตร):", font=('Angsana New', 16), bg='#f0f0f0')
label_height.grid(row=1, column=0, padx=10, pady=10)
entry_height = tk.Entry(window, font=('Angsana New', 16))
entry_height.grid(row=1, column=1, padx=10, pady=10)

btn_calculate = tk.Button(window, text="คำนวณ BMI", command=calculate_bmi, font=('Angsana New', 13, 'bold'), bg='#4CAF50', fg='white')
btn_calculate.grid(row=2, column=0, columnspan=2, pady=10)

label_result = tk.Label(window, text="", font=('Angsana New', 12, 'bold'), bg='#f0f0f0')
label_result.grid(row=3, column=0, columnspan=2, pady=10)

#เครดิตผู้สร้าง
label_credit = tk.Label(window, text="สร้างโดย ศุภกานต์ สียะ ม.6/7 เลขที่ 13", font=('Angsana New', 16), bg='#f0f0f0', fg='#555')
label_credit.grid(row=4, column=0, columnspan=2, pady=5)

#ทำงานเมื่อกดปิด GUI
window.protocol("WM_DELETE_WINDOW", on_closing)

#เริ่มการทำงานของ GUI
window.mainloop()
