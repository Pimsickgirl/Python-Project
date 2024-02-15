movies = ["Jurassic Park III", "Jirassic Park", "Jurassic World"]
ticket_prices = [100, 120, 90]

while True:
    print("Welcome to Movie Ticket Booking System!")
    print("Available movies:")
    print("1. ", movies[0], " - ", ticket_prices[0], " Baht")
    print("2. ", movies[1], " - ", ticket_prices[1], " Baht")
    print("3. ", movies[2], " - ", ticket_prices[2], " Baht")

    selected_movie = (input("Enter the number of the movie you want to watch: "))
    money = int(input("Enter money do you have: "))

    if selected_movie == '1':
        if money < ticket_price[0]:
            print("คุณมีเงินไม่เพียงพอ")
            break
        else:
            result_money = money - ticket_prices
            print(f"You have selected '{selected_movie}'. The ticket price is {result_money} Baht.")
    elif selected_movie == '2':
        if money < ticket_prices[2]:
            print("คุณมีเงินไม่เพียงพอ")
            break
        else:
            result_money = money - ticket_prices
            print(f"You have selected '{selected_movie}'. The ticket price is {result_money} Baht.")
    elif selected_movie == '3':
        if money < ticket_prices[3]:
            print("คุณมีเงินไม่เพียงพอ")
            break
        else:
            result_money = money - ticket_prices
            print(f"You have selected {selected_movie} The ticket price is {result_money} Baht")
    else:
        print("Invalid movie selection.")
        continue

    while True:
        buy_again = input("Do you want to buy another ticket? (yes/no): ")
        if buy_again.lower() == 'y':
            break
        elif buy_again.lower() == 'n':
            print("Thank you for using buy ticket systems 🙏🏻")
            quit()
        else:
            print("กรุณาป้อน (y/n) เท่านั้น")