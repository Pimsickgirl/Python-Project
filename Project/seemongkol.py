print("สีมงคลประจำวันเกิด")

while True:
    # รับวันเกิดจากผู้ใช้
    day_of_birth = input("โปรดระบุวันเกิดของคุณ (เช่น: วันจันทร์): ")

    if day_of_birth.lower() == 'วันอาทิตย์' or day_of_birth.lower() == 'อาทิตย์':
        print("สีที่นิยมนำมาใช้ประยุกต์เรื่องของการแต่งกาย ได้แก่ สีส้ม สีแดง สีชมพู สีเขียว สีขาว")
        print("สีที่ไม่นิยมนำมาใช้เพราะจะทำให้เสื่อมโชคลาภ ได้แก่ สีฟ้า สีน้ำเงิน")
    elif day_of_birth.lower() == 'วันจันทร์' or day_of_birth.lower() == 'จันทร์':
        print("สีที่นิยมนำมาใช้ประยุกต์เรื่องของการแต่งกาย ได้แก่ สีเขียวสด สีดำ สีขาว สีม่วง")
        print("สีที่ไม่นิยมนำมาใช้เพราะจะทำให้เสื่อมโชคลาภ ได้แก่ สีแดง สีส้ม")
    elif day_of_birth.lower() == 'วันอังคาร' or day_of_birth.lower() == 'อังคาร':
        print("สีที่นิยมนำมาใช้ประยุกต์เรื่องของการแต่งกาย ได้แก่ สีดำ สีเหลือง สีชมพู สีม่วง สีแดง สีแสด")
        print("สีที่ไม่นิยมนำมาใช้เพราะจะทำให้เสื่อมโชคลาภ ได้แก่ สีครีม สีขาว")
    elif day_of_birth.lower() == 'วันพุธ' or day_of_birth.lower() == 'พุธ':
        print("สีที่นิยมนำมาใช้ประยุกต์เรื่องของการแต่งกาย ได้แก่ สีเขียว สีเหลืองอ่อน สีเหลืองแก่")
        print("สีที่ไม่นิยมนำมาใช้เพราะจะทำให้เสื่อมโชคลาภ ได้แก่ สีชมพู สีแสด")
    elif day_of_birth.lower() == 'วันพฤหัสบดี' or day_of_birth.lower() == 'พฤหัสบดี':
        print("สีที่นิยมนำมาใช้ประยุกต์เรื่องของการแต่งกาย ได้แก่ สีส้ม สีเหลือง สีฟ้า สีน้ำเงิน สีเขียวสด สีแดง")
        print("สีที่ไม่นิยมนำมาใช้เพราะจะทำให้เสื่อมโชคลาภได้แก่ สีดำ สีม่วง")
    elif day_of_birth.lower() == 'วันศุกร์' or day_of_birth.lower() == 'ศุกร์':
        print("สีที่นิยมนำมาใช้ประยุกต์เรื่องของการแต่งกาย ได้แก่ สีฟ้า สีน้ำเงิน สีขาว สีเหลือง สีชมพู สีแสด")
        print("สีที่ไม่นิยมนำมาใช้เพราะจะทำให้เสื่อมโชคลาภได้แก่ สีเขียวแก่ สีน้ำตาล สีเทา สีทึมๆ")
    elif day_of_birth.lower() == 'วันเสาร์' or day_of_birth.lower() == 'เสาร์':
        print("สีที่นิยมนำมาใช้ประยุกต์เรื่องของการแต่งกาย ได้แก่ สีแดง สีเหลือง สีฟ้า สีน้ำเงิน สีชมพู สีน้ำตาล")
        print("สีที่ไม่นิยมนำมาใช้เพราะจะทำให้เสื่อมโชคลาภได้แก่ สีเขียว สีแสด")
    else:
        print("ขออภัยคุณใส่วันไม่ถูกต้อง")

    # ถามผู้ใช้ว่าต้องการทำอีกครั้งหรือไม่
    while True:
        check_more = input("ต้องการจะระบุวันเกิดเพิ่มเติมหรือไม่? (yes/no): ")
        if check_more == "yes":
            break
        elif check_more == 'no':
            quit()
        else:
            print("โปรดป้อน yes หรือ no เท่านั้น")