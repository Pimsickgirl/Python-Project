while True:
    # แสดงรายการเมนูอาหาร
    print("รายการอาหาร:")
    print("1: ข้าวผัด - ราคา 50 บาท")
    print("2: ผัดซีอิ๊ว - ราคา 60 บาท")
    print("3: ข้าวมันไก่ - ราคา 40 บาท")
    print("4: ส้มตำ - ราคา 30 บาท")
    print("5: ต้มยำกุ้ง - ราคา 80 บาท")

    # รับเลือกเมนูอาหารและจำนวน
    selected_menu = input("โปรดเลือกหมายเลขเมนูอาหาร: ")
    quantity = int(input("โปรดระบุจำนวนที่ต้องการ: "))

    # ตรวจสอบเมนูที่เลือกและคำนวณราคารวม
    if selected_menu == "1":
        total_price = 50 * quantity
        print(f"คุณเลือก ข้าวผัด จำนวน {quantity} ชุด")
        print(f"ราคารวมทั้งหมด: {total_price} บาท")
    elif selected_menu == "2":
        total_price = 60 * quantity
        print(f"คุณเลือก ผัดซีอิ๊ว จำนวน {quantity} ชุด")
        print(f"ราคารวมทั้งหมด: {total_price} บาท")
    elif selected_menu == "3":
        total_price = 40 * quantity
        print(f"คุณเลือก ข้าวมันไก่ จำนวน {quantity} ชุด")
        print(f"ราคารวมทั้งหมด: {total_price} บาท")
    elif selected_menu == "4":
        total_price = 30 * quantity
        print(f"คุณเลือก ส้มตำ จำนวน {quantity} ชุด")
        print(f"ราคารวมทั้งหมด: {total_price} บาท")
    elif selected_menu == "5":
        total_price = 80 * quantity
        print(f"คุณเลือก ต้มยำกุ้ง จำนวน {quantity} ชุด")
        print(f"ราคารวมทั้งหมด: {total_price} บาท")
    else:
        print("ขอโทษครับ/ค่ะ ไม่มีเมนูอาหารนี้ในรายการ")

    # ถามผู้ใช้ว่าต้องการซื้ออีกหรือไม่
    while True:
        buy_more = input("ต้องการซื้อเมนูอาหารเพิ่มหรือไม่ (yes/no): ")
        if buy_more == "yes":
            break
        elif buy_more == 'no':
            quit()
        else:
            print("โปรดป้อน yes หรือ no เท่านั้น")
