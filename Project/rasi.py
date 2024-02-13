print("การหาราศีโดยการใส่วันและเดือนเกิด")
print("อิงจากเว็บไทยรัฐออนไลน์ 2565")

while True:

    day = int(input("ป้อนวันเกิด (1-31): "))
    month = int(input("ป้อนเดือนเกิด (1-12): "))

    if day <= 0 or month <= 0:
        print("กรุณากรอกข้อมูลใหม่")
        continue

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        sign = "ราศีเมษ (Aries)"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        sign = "ราศีพฤษภ (Taurus)"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        sign = "ราศีเมถุน (Gemini)"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        sign = "ราศีกรกฎ (Cancer)"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        sign = "ราศีสิงห์ (Leo)"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        sign = "ราศีกันย์ (Virgo)"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        sign = "ราศีตุลย์ (Libra)"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        sign = "ราศีพิจิก (Scorpio)"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        sign = "ราศีธนู (Sagittarius)"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        sign = "ราศีมังกร (Capricorn)"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        sign = "ราศีกุมภ์ (Aquarius)"
    else:
        sign = "ราศีมีน (Pisces)"
    
    # แสดงผลลัพธ์
    print(f"คุณเป็น {sign}")

    while True:
        again = input("คุณต้องการตรวจราศีอีกครั้งหรือไม่ (ใช่/ไม่): ")
        if again == 'ใช่':
            break
        elif again == 'ไม่':
            quit()
        else:
            print("โปรดป้อนให้ถูกต้องระหว่าง (ใช่/ไม่)")
