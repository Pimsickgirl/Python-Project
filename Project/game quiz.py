import random

print("ยินดีต้อนรับสู่โปรแกรมตอบคำถามทางคณิตศาสตร์!")
while True:
    
    # สุ่มตัวเลขสองจำนวน
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # เลือกการดำเนินการสุ่ม
    operator = random.choice(['+', '-', '*', '/'])

    # สร้างคำถาม
    question = f"{num1} {operator} {num2}"

    # คำนวณคำตอบ
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        answer = num1 / num2
    
    print(f"คำถามของคุณคือ: {question} = {answer}")
    user_choice = input("โปรดเลือก 'ถูก' หรือ 'ผิด': ")
    
    # ตรวจสอบคำตอบ
    if (user_choice == 'ถูก' and answer % 1 == 0) or (user_choice == 'ผิด' and answer % 1 != 0):
        print("คำตอบของคุณถูกต้อง!")
    else:
        print("เสียใจด้วย! คำตอบของคุณไม่ถูกต้อง")
    
    play_again = input("คุณต้องการเล่นอีกครั้งหรือไม่? (y/n): ")
    if play_again != 'y':
        print("ขอบคุณที่ใช้บริการ ลาก่อน!")
        break
