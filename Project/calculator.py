print("โปรแกรมเครื่องคิดเลข")

while True:
    print("เลือกการคำนวณ")
    print("1. การบวก")
    print("2. การลบ")
    print("3. การคุณ")
    print("4. การหาร")

    choice = input("เลือกการคำนวณ (1, 2, 3, 4): ")
    if choice not in ['1', '2', '3', '4']:
        print("กรุณาเลือก choice ให้ถูกต้อง")
        continue

    num1 = float(input("ป้อนตัวเลชแรก: "))
    num2 = float(input("ป้อนตัวเลขที่สอง: "))

    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        if num2 == 0:
            print("ไม่สามารถหารด้วย 0 ลงตัว")
        else:
            result = num1 / num2
    else:
        print("รายการที่เลือกไม่ถูกต้อง")
    
    print("ผลลัพธ์:", result)

    while True:
        again = input("คุณต้องการทำการคำนวณเครื่องคิดเลขต่อหรือไม่? (y/n): ")
        if again == 'y':
            break
        elif again == 'n':
            quit()
        else:
            print("โปรดป้อนให้ถูกต้อง y/n")
