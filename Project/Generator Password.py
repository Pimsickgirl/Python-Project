import random
import string

while True:

    print("1. ง่าย")
    print("2. ปานกลาง")
    print("3. ยาก")
    difficulty = input("เลือกระดับความยาก (1, 2, 3): ")
    if difficulty not in ['1', '2', '3']:
        print("กรุณาเลือกระดับความยากให้ถูกต้อง")
        continue
    
    length = int(input("ป้อนความยาวของรหัสผ่าน: "))
    if length < 6 or length > 16:
        print("ความยาวของรหัสผ่านต้องอยู่ระหว่าง 6 ถึง 16 ตัวอักษร")
        continue
    
    if difficulty == '1':
        characters = string.ascii_letters + string.digits
    elif difficulty == '2':
        characters = string.ascii_letters + string.digits + string.punctuation.replace("'", "") # ไม่รวมอัญประกาศ
    elif difficulty == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("กรุณาเลือกระดับความยากให้ถูกต้อง")

    password = ''.join(random.choice(characters) for i in range(length))
    print("รหัสผ่านของคุณคือ:", password)
    
    while True:
        again = input("ต้องการสร้างรหัสผ่านอีกครั้งหรือไม่? (ใช่/ไม่): ")
        if again == 'ใช่':
            break
        elif again == 'ไม่':
            quit()
        else:
            print("กรุณาป้อน ใช่/ไม่ เท่านั้น")
