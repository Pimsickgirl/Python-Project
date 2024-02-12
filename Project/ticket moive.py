import json
import os

# ตรวจสอบว่าไฟล์ 'ticketsmovie.json' มีหรือไม่
if not os.path.isfile('ticketsmovie.json'):
    # ถ้าไม่มี สร้างไฟล์ใหม่
    with open('ticketsmovie.json', 'w', encoding='utf-8') as json_file:
        json_file.write("[]") # เขียนข้อมูลเป็นรูปแบบ JSON array ว่าง

while True:
    print("ยินดีต้อนรับสู่การจองตั๋วหนัง")
    name = input("โปรดป้อนชื่อ: ")
    movie_name = input("โปรดป้อนชื่อหนังที่คุณต้องการดู: ")
    number_of_tickets = int(input("โปรดป้อนจำนวนตั๋วที่ต้องการซื้อ: "))
    row_choice = input("โปรดเลือกแถวที่นั่ง (A, B, C, D, E): ").upper()

    # ตรวจสอบว่าแถวที่เลือกถูกต้องหรือไม่
    valid_rows = ['A', 'B', 'C', 'D', 'E']
    if row_choice not in valid_rows:
        print("กรุณาเลือกแถวที่ถูกต้อง")
        continue

    print("\nรายละเอียดการจอง:")
    print("----------------------------")
    print("คุณ: ", name)
    print("ชื่อหนัง: ", movie_name)
    print("จำนวนตั๋ว: ", number_of_tickets)
    print("แถวที่นั่ง: ", row_choice)
    print("----------------------------")

    while True:
        confirm = input("ยืนยันการจองตั๋วหรือไม่? (ใช่/ไม่): ")
        if confirm.lower() == "ใช่":
            tickets_moviedata = {
                "คุณ": name,
                "ชื่อหนัง": movie_name,
                "จำนวนตั๋ว": number_of_tickets,
                "แถวที่นั่ง": row_choice
            }

            # อ่านข้อมูล JSON ที่มีอยู่ในไฟล์
            with open('ticketsmovie.json', 'r', encoding='utf-8') as json_file:
                try:
                    data = json.load(json_file)
                except json.decoder.JSONDecodeError:
                    data = []

            # เพิ่มข้อมูลการจองตั๋วใหม่ลงในรายการ
            data.append(tickets_moviedata)

            # เขียนข้อมูล JSON ลงในไฟล์
            with open('ticketsmovie.json', 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=2)

            print("บันทึกข้อมูลการจองตั๋วลงใน ticketmovie.json สำเร็จแล้ว")
            break
        elif confirm.lower() == "ไม่":
            print("การจองตั๋วถูกยกเลิก")
            break
        else:
            print("โปรดระบุให้ชัดเจนว่าต้องการยืนยันหรือไม่")

    while True:
        continue_prompt = input("ต้องการซื้อตั๋วหนังเพิ่มอีกหรือไม่? (ใช่/ไม่): ")
        if continue_prompt.lower() == "ใช่":
            break
        elif continue_prompt.lower() == "ไม่":
            print("กำลังปิดโปรแกรม...")
            quit()
        else:
            print("โปรดระบุให้ชัดเจนว่าต้องการซื้อหรือไม่")
