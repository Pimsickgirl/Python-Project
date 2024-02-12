print("สมาชิก")
print("ชุติมา เสือสว่าง เลขที่ 17\nบัณฑิตา กตะศิลา เลขที่ 23")
print("ฉลากกินแบ่งรัฐบาล / 1 กุมภาพันธ์ 2567")

while True:
    ticket_number = int(input("กรุณาใส่เลขที่ต้องการตรวจ: "))

    if ticket_number == 607063:
        print(f"ยินดีด้วย! คุณถูกรางวัลที่ 1 ด้วยเลข {ticket_number}")
        print("รางวัล: 6,000,000 บาท")
    elif ticket_number in [808878, 779424, 851911, 166521, 376456]:
        print(f"ยินดีด้วย! คุณได้รับรางวัลที่ 2 ด้วยเลข {ticket_number}")
        print("รางวัลที่ 2: รางวัล 200,000 บาท")
    elif ticket_number in [678876, 831569, 516593, 113069, 53669, 87418,772652, 535443, 697943, 545456]:
        print(f"ยินดีด้วย! คุณได้รับรางวัลที่ 3 ด้วยเลข {ticket_number}")
        print("รางวัลที่ 3: รางวัล 80,000 บาท")
    elif str(ticket_number)[:3] in ['943', '454']:
        print(f"ยินดีด้วย! คุณถูกรางวัลเลขหน้า 3 ตัว ด้วยเลข {ticket_number}")
        print("รางวัล: 4,000 บาท")
    elif str(ticket_number)[-3:] in ['544', '591']:
        print(f"ยินดีด้วย! คุณถูกรางวัลเลขท้าย 3 ตัว ด้วยเลข {ticket_number}")
        print("รางวัล: 4,000 บาท")
    elif str(ticket_number)[-2:] == '09':
        print(f"ยินดีด้วย! คุณถูกรางวัลเลขท้าย 2 ตัว ด้วยเลข {ticket_number}")
        print("รางวัล: 2,000 บาท")
    elif ticket_number in [607064, 607062]:
        print(f"ยินดีด้วย! คุณได้รับรางวัลที่ใกล้เคียงรางวัลที่ 1 ด้วยเลข {ticket_number}")
        print("รางวัลที่ใกล้เคียงรางวัลที่ 1: 100,000 บาท")
    else:
        print("เสียใจด้วย คุณไม่ถูกรางวัล")

    while True:
        check_again = input("ต้องการตรวจหวยอีกหรือไม่ (yes/no): ")
        if check_again == 'yes':
            break
        elif check_again == 'no':
            print("กำลังปิดโปรแกรม...")
            quit()
        else:
            print("โปรดป้อน yes หรือ no เท่านั้น")
        
