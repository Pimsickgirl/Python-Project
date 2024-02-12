while True:
    # แสดงรายการเมนูอาหาร
    print("รายการน้ำคาเฟ่:")
    print("1: น้ำเปล่า - ราคา 10 บาท")
    print("2: ชาเขียว - ราคา 25 บาท")
    print("3: กาแฟ - ราคา 30 บาท")
    print("4: นมสด - ราคา 25 บาท")
    print("5: โกโก้ - ราคา 30 บาท")
    print("5: ชานมเย็น - ราคา 25 บาท")

    # รับเลือกเมนูและจำนวน
    select_menu = input("โปรดเลือกหมายเลขเมนูน้ำ: ")
    amount = int(input("โปรดระบุจำนวนที่ต้องการ: "))

    # ตรวจสอบเมนูที่เลือกและคำนวณราคารวม
    if select_menu == "1":
        total_price = 10 * amount
        print(f"คุณเลือก น้ำเปล่า จำนวน {amount} ชุด")
        print(f"ราคารวมทั้งหมด: {total_price} บาท")
    elif select_menu == "2":
        total_price = 25 * amount
        print(f"คุณเลือก ชาเขียว จำนวน {amount} ชุด")
        print(f"ราคารวมทั้งหมด: {total_price} บาท")
    elif select_menu == "3":
        total_price = 30 * amount
        print(f"คุณเลือก กาแฟ จำนวน {amount} ชุด")
        print(f"ราคารวมทั้งหมด: {total_price} บาท")
    elif select_menu == "4":
        total_price = 25 * amount
        print(f"คุณเลือก นมสด จำนวน {amount} ชุด")
        print(f"ราคารวมทั้งหมด: {total_price} บาท")
    elif select_menu == "5":
        total_price = 30 * amount
        print(f"คุณเลือก โกโก้ จำนวน {amount} ชุด")
        print(f"ราคารวมทั้งหมด: {total_price} บาท")
    elif select_menu == "6":
        total_price = 25 * amount
        print(f"คุณเลือก ชานมเย็น จำนวน {amount} ชุด")
        print(f"ราคารวม: {total_price} บาท")
    else:
        print("ขอโทษครับ/ค่ะ ไม่มีเมนูน้ำนี้ในรายการ")

    # ถามผู้ใช้ว่าต้องการซื้ออีกหรือไม่
    while True:
        buy_more = input("ต้องการซื้อเมนูน้ำเพิ่มหรือไม่ (ใช่/ไม่): ")
        if buy_more == "ใช่":
            break
        elif buy_more == 'ไม่':
            quit()
        else:
            print("โปรดป้อน (ใช่) หรือ (ไม่) เท่านั้น")
