balance = 10000

while True:
    print("------ โปรดเลือกรายการ ------")
    print("1. ฝากเงิน")
    print("2. ถอนเงิน")
    print("3. ดูยอดเงิน")
    print("4. ปิดโปรแกรม")

    choice = input("โปรดเลือกรายการที่ต้องการ: ")

    if choice == '1':
        deposit_amount = int(input("โปรดใส่จำนวนเงินที่ต้องการฝาก: "))
        balance += deposit_amount
        print(f"ฝากเงิน {deposit_amount} บาทเรียบร้อย!")

        while True:
            more_deposit = input("ต้องการทำธุรกรรมเพิ่มหรือไม่ (y/n): ")
            if more_deposit == 'y':
                deposit_amount = int(input("โปรดใส่จำนวนเงินที่ต้องการฝาก: "))
                balance += deposit_amount
                print(f"ฝากเงิน {deposit_amount} บาทเรียบร้อย")
            elif more_deposit == 'n':
                break
            else:
                print("โปรดป้อน y หรือ n เท่านั้น")

    elif choice == '2':
        withdraw_amount = int(input("โปรดใส่จำนวนเงินที่ต้องการถอน: "))
        if balance >= withdraw_amount:
            balance -= withdraw_amount
            print(f"ถอนเงินจำนวน {withdraw_amount} บาทเรียบร้อย")
        else:
            print("ยอดเงินในบัญชีไม่เพียงพอ")

        while True:
            more_withdraw = input("ต้องการทำธุรกรรมเพิ่มหรือไม่ (y/n): ")
            if more_withdraw == 'y':
                withdraw_amount = int(input("โปรดป้อนจำนวนเงินที่ต้องการถอน: "))
                if balance >= withdraw_amount:
                    balance -= withdraw_amount
                    print(f"ถอนเงินจำนวน {withdraw_amount} บาทเรียงร้อย")
                else:
                    print("ยอดเงินในบัญชีไม่เพียงพอ")
            elif more_withdraw == 'n':
                break
            else:
                print("โปรดป้อน y หรือ n เท่านั้น")

    elif choice == '3':
        print(f"ยอดเงินในบัญชีคุณคือ {balance} บาท")
         
        while True:
            more_balance = input("ต้องการทำธุรกรรมเพิ่มเติมหรือไม่ (y/n): ")
            if more_balance == 'y':
                break
            elif more_balance == 'n':
                quit()
            else:
                print("โปรดป้อน y หรือ n เท่านั้น")

    elif choice == '4':
        print("ปิดโปรแกรม")
        break
    else:
        print("โปรดเลือกรายการใหม่")