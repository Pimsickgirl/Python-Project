
#ค่าเงินของแต่ละประเทศ
exchange_rate_usd = 35.7175  # อัตราแลกเปลี่ยนเป็นดอลลาร์
exchange_rate_jpy = 0.2391  # อัตราแลกเปลี่ยนเป็นเยน
exchange_rate_cny = 5.0264 # อัตราแลกเปลี่ยนเป็นหยวน

while True:

    print("1. แปลงเงินไทยไปเป็นของต่างชาติ")
    print("2. แปลงเงินต่างชาติเป็นเงินไทย")
    print("3. เพื่อปิดโปรแกรม")
    choice = input("คุณต้องการใช้การแปลงเงินแบบไหน: ")

    if choice == "1":
        print("1. USD (United States Dollar)")
        print("2. JPY (Japanese Yen)")
        print("3. CNY (Chinese Yuan)")
        choice = input("คุณต้องการแปลงเป็นเงินอะไร:")
        thai_baht = float(input("โปรดป้อนจำนวนเงินต่างชาติ: "))

        if choice == "1":
            converted_amount = thai_baht * exchange_rate_usd
            currency_name = "USD"
        elif choice == "2":
            converted_amount = thai_baht * exchange_rate_jpy
            currency_name = "JPY"
        elif choice == "3":
            converted_amount = thai_baht * exchange_rate_cny
            currency_name = "CNY"
        else:
            print("โปรดเลือกตัวเลือกใหม่")
            continue
        print(f"แปลงเป็นเงินไทย: {converted_amount:.2f}")

    elif choice == "2":
        print("1. USD (United States Dollar)")
        print("2. JPY (Japanese Yen)")
        print("3. CNY (Chinese Yuan)")
        choice = input("คุณต้องการแปลงเป็นเงินอะไร:")
        thai_baht = float(input("โปรดป้อนจำนวนเงินบาทไทย: "))

        if choice == "1":
            converted_amount = thai_baht / exchange_rate_usd
            currency_name = "USD"
        elif choice == "2":
            converted_amount = thai_baht / exchange_rate_jpy
            currency_name = "JPY"
        elif choice == "3":
            converted_amount = thai_baht / exchange_rate_cny
            currency_name = "CNY"
        else:
            print("โปรดเลือกตัวเลือกใหม่")
            continue
        print(f"ค่าเงินของ ({currency_name}): {converted_amount:.2f}")
    
    elif choice == "3":
        print("กำลังปิดโปรแกรม")
        break

    else:
        print("กรุณาเลือกตัวเลือกให้ถูกต้อง")
        continue

    while True:
        another_conversion = input("คุณต้องการทำการแปลงเงินอีกครั้งหรือไม่? (yes/no): ")
        if another_conversion == "yes":
            break
        elif another_conversion == "no":
            quit()
        else:
            print("โปรดเลือกตัวเลือกที่ถูกต้องเช่น yes/no")