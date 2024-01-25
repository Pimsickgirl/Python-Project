from logging import root
import tkinter as tk
from tkinter import ttk, messagebox

candidates = ["Spark", "Develop", "Reliable", "ผิง", "Guard", "SIREN", "Free Energy", "Miracle"]
votes = {candidate: 0 for candidate in candidates}
students = 2733

def vote(candidate):
    if candidate in candidates:
        votes[candidate] += 1
        messagebox.showinfo("Takpittayakhom Vote", f"โหวตให้\n พรรค: {candidate} สำเร็จแล้ว")
    else:
        messagebox.showerror("Invalid Candidate Takpittayakhom", "ผู้สมัครไม่ถูกต้อง")

def display_results():
    result_text = "\nผลการเลือกตั้ง:\n-----------------\n"
    total_votes = sum(votes.values())
    total_student = students
    not_voted = total_student - total_votes

    for candidate, vote_count in votes.items():
        percentage = (vote_count / total_votes) * 100 if total_votes > 0 else 0
        not_voteds = (not_voted / total_student) * 100
        result_text += f"พรรค: {candidate}: {vote_count} โหวต ({percentage:.2f}%)\n"
    result_text += "-----------------\n"
    result_text += f"ทั้งหมด: {total_votes} โหวต\n"
    result_text += f"จากนักเรียนทั้งหมด: {total_student} คน\n"
    result_text += f"ไม่มาเลือกตั้งลงคะแนนเสียง: {not_voted} คน ({not_voteds:.2f}%)"

    messagebox.showinfo("Results Takpittayakhom", result_text)

def confirm_vote(candidate):
    response = messagebox.askyesno("Confirmation", f"คุณแน่ใจที่จะเลือกพรรค: {candidate} ใช่หรือไม่?")
    if response:
        vote(candidate)

def vote_button_clicked(candidate):
    confirm_vote(candidate)

def main():
    tps = tk.Tk()
    tps.title("Takpittayakhom School | Election Systems")
    tps.geometry("500x650")
    tps.iconbitmap("tps.ico")
    tps.resizable(width=False, height=False)

    style = ttk.Style()
    style.configure("TButton", padding=(10, 5), font=('Angsana New', 16))

    app_name = tk.Label(tps, text="ระบบเลือกตั้ง 2567 | โรงเรียนตากพิทยาคม", font=('Angsana New', 20), bg='#f0f0f0', fg='#000000')
    app_name.pack(pady=5)

    for candidate in candidates:
        button = ttk.Button(tps, text=candidate, command=lambda c=candidate: vote_button_clicked(c))
        button.pack(pady=5)

    label_credit = tk.Label(tps, text="สร้างโดย ศุภกานต์ สียะ ชั้นมัธยมศึกษาปีที่ 6 ", font=('Angsana New', 18), bg='#f0f0f0', fg='#000000')
    label_credit.pack(pady=5)

    result_button = ttk.Button(tps, text="ผลการเลือกตั้ง", command=display_results)
    result_button.pack(pady=10)

    tps.mainloop()

main()
