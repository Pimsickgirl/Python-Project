# แคลลอรี่ที่เสียต่อหน่วย (ค่าประมาณ)
calories_per_kilometer_walk = 55
calories_per_kilometer_run = 70
calories_per_kilometer_jog = 65

while True:
    # รับประเภทการทำกิจกรรมจากผู้ใช้
    activity_type = input("โปรดเลือกประเภทของกิจกรรม (วิ่ง/เดิน/จ๊อกกิ๊ง): ")

    # ตรวจสอบว่าประเภทของกิจกรรมถูกต้องหรือไม่
    if activity_type not in ["เดิน", "วิ่ง", "จ๊อกกิ๊ง"]:
        print("ประเภทของกิจกรรมไม่ถูกต้อง")
        continue

    # รับระยะทางจากผู้ใช้
    distance_in_km = float(input("กรุณาป้อนระยะทางที่ทำได้ในกิโลเมตร: "))

    # คำนวณแคลลอรี่ที่เสียไปตามประเภทของกิจกรรม
    if activity_type == "เดิน":
        calories_burned = distance_in_km * calories_per_kilometer_walk
    elif activity_type == "วิ่ง":
        calories_burned = distance_in_km * calories_per_kilometer_run
    elif activity_type == "จ๊อกกิ๊ง":
        calories_burned = distance_in_km * calories_per_kilometer_jog

    print(f"{activity_type}ไป {distance_in_km} กิโลเมตรจะลดไปประมาณ {calories_burned} แคลลอรี่")

    while True:
        # ถามผู้ใช้ว่าต้องการทำรายการเพิ่มเติมหรือไม่
        another_activity = input("คุณต้องการทำรายการเพิ่มเติมหรือไม่? (ใช่/ไม่): ")
        if another_activity == "ใช่":
            break
        elif another_activity == 'ไม่':
            print("โดย ศุภกานต์ มูลเปี้ย ม.6/7 เลขที่ 30")
            quit()
        else:
            print("โปรดใส่ (ใช่/ไม่)")
