class Customer:
    def __init__(self, id, name, address, email, password, phone_number, card_number):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.card_number = card_number

    def show_customer(self):
        print()
        print("CUSTOMER INFORMATION REQUESTED:")
        print("Customer ID: " + self.id)
        print("Customer Name: " + self.name)
        print("Customer Address: " + self.address)
        print("Customer Email: " + self.email)
        print("Customer Phone Number: " + self.phone_number)
        print("Customer Card Number: " + self.card_number)
        back_to_menu()


class TaxiDriver:
    def __init__(self, id, driver_name, license_plate, password) -> None:
        self.id = id
        self.driver_name = driver_name
        self.license_plate = license_plate
        self.password = password

    def show_taxi_driver(self):
        print()
        print("TAXI DRIVER INFORMATION REQUESTED:")
        print("Taxi Driver ID: "+ self.id)
        print("Taxi Driver Name: " + self.driver_name)
        print("Taxi License Plate: " + self.license_plate)
        back_to_menu()


class TripBooking(Customer, TaxiDriver):
    def __init__(self, customer, taxi_driver, id, pick_up_time, date, drop_off_address) -> None:
        self.id =id
        self.pick_up_time = pick_up_time
        self.date = date
        self.drop_off_address = drop_off_address
        self.customer = customer
        self.taxi_driver = taxi_driver
    
    def show_booking(self, b_id):
        print()
        print("BOOKING INFORMATION REQUESTED:")
        print("Booking Number: " + self.id)
        print("Customer Name: " + self.customer.name)
        print("Customer Address: " + self.customer.address)
        print("Customer Email: " + self.customer.email)
        print("Customer Phone Number: " + self.customer.phone_number)
        print("Taxi Driver Name: " + self.taxi_driver.driver_name)
        print("Taxi License Plate: " + self.taxi_driver.license_plate)
        print("Pick Up Time: " + self.pick_up_time)
        print("Pick Up Date: " + self.date)
        print("Drop Off Address: " + self.drop_off_address)
        back_to_menu()


def add_c():
    print()
    customer_id = len(c_list)
    for x in range (0,len(c_list)-1):
        if customer_id == c_list[x].id:
            customer_id += 1
    name = input("Enter Customer Name: ")
    address = input("Enter Customer Address: ")
    email = input("Enter Customer Email: ")
    for x in range (len(c_list)):
        if email == c_list[x].email:
            print()
            print("EMAIL already in use! Use a DIFFERENT EMAIL! Press ENTER key to continue...")
            admin_main()
            return
        else:
            password = input("Enter Customer Password: ")
            phone_number = input("Enter Customer Phone Number: ")
            if phone_number.isdigit():
                if len(phone_number) != 11:
                    not_phone_no()
                    admin_main()
                else:
                    card_number = input("Please, enter your Card Number: ")
                    if card_number.isdigit():
                        if len(card_number) != 16 and validate_luhn10(card_number) == True:
                            c = Customer(customer_id, name, address, email, password, phone_number, card_number)
                            c_list.append(c)
                            update_database()
                            input("Customer added! Press ENTER key to continue...")
                            admin_main()
                            return c_list
                        else:
                            not_card_no()
                            admin_main()    
                    else:
                        not_card_no()
                        admin_main()
            else:
                not_phone_no()
                admin_main()


def register_c():
    print()
    customer_id = len(c_list)
    for x in range (0,len(c_list)-1):
        if customer_id == c_list[x].id:
            customer_id += 1
    name = input("Please, enter your Name: ")
    address = input("Please, enter your Address: ")
    email = input("Please, enter your Email: ")
    for x in range (len(c_list)):
        if email == c_list[x].email:
            print()
            print("EMAIL already in use! Use a DIFFERENT EMAIL! Press ENTER key to continue...")
            register_c()
            return
        else:
            password = input("Please, enter your Password: ")
            phone_number = input("Please, enter your Phone Number: ")
            if phone_number.isdigit():
                if len(phone_number) != 11:
                    not_phone_no()
                    register_c()
                else:
                    card_number = input("Please, enter your Card Number: ")
                    if card_number.isdigit():
                        if len(card_number) != 16 and validate_luhn10(card_number) == True:
                            c = Customer(customer_id, name, address, email, password, phone_number, card_number)
                            c_list.append(c)
                            update_database()
                            input("Thank you for registering with us! Press ENTER key to continue...")
                            main()
                            return c_list
                        else:
                            not_card_no()
                            register_c()
                    else:
                        not_card_no()
                        register_c()
            else:
                not_phone_no()
                register_c()


def not_card_no():
    print()
    print("Not a card number! Please try another one! Press ENTER key to continue...")


def not_phone_no():
    print()
    print("Not a phone number! Please try another one! Press ENTER key to continue...")


def validate_luhn10(text: str) -> bool:
    number_of_digits = len(text)
    number_sum = 0
    second_number = False
    for i in range(number_of_digits - 1, -1, -1):
        d = ord(text[i]) - ord('0')
        if second_number:
            d = d * 2
        # We add two digits to handle
        # cases that make two digits after
        # doubling
        number_sum += d // 10
        number_sum += d % 10
        second_number = not second_number
    if number_sum % 10 == 0:
        return True
    else:
        return False


def add_td():
    print()
    taxi_id = len(td_list)
    for x in range (0,len(td_list)-1):
        if taxi_id == td_list[x].id:
            taxi_id += 1
    name = input("Enter Taxi Driver Name: ")
    plate = input("Enter License Plate Number: ")
    for x in range (len(td_list)):
        if plate == td_list[x].license_plate:
            print()
            print("PLATE already exist! Press ENTER key to continue...")
            admin_main()
            return
        else:
            password = input("Enter password: ")
            td = TaxiDriver(taxi_id, name, plate, password)
            td_list.append(td)
            update_database()
            input("Taxi driver added! Press ENTER key to continue...")
            admin_main()
            return td_list


def make_b(user_id):
    print()
    booking_no = len(b_list)
    for x in range (0,len(b_list)-1):
        if booking_no == b_list[x].id:
            booking_no += 1
    time = input("Please, enter your Pick Up Time: ")
    date = input("Please, enter your Pick Up Date: ")
    address = input("Please, enter your Drop Off Address: ")
    customer = c_list[user_id]
    td_id = input("Please, enter your Taxi Driver ID number: ")
    if td_id.isdigit():
        td_id = int(td_id)
        if td_id in range(0, len(td_list)):
            for x in range (0, len(td_list)):
                if td_list[x].license_plate == td_list[td_id].license_plate:
                    wrong_id()
                    user_main(user_id)
                else:
                    taxi_driver = td_list[td_id]
                    b = TripBooking(customer, taxi_driver, booking_no, time, date, address)
                    b_list.append(b)
                    update_database()
                    input("Booking added! Press ENTER key to continue...")
                    user_main(user_id)
                    return b_list
        else:
            wrong_id()
            user_main(user_id)
    else:
        wrong_id()
        user_main(user_id)
    

def cancel_b(user_id):
    print()
    b_id = input("Please, enter your Booking Number: ")
    if b_id.isdigit():
        b_id = int(b_id)
        if not b_list:
            no_bookings()
            user_main(user_id)
        else:
            for x in range (0, len(b_list)):
                if b_id == int(b_list[x].id) and str(c_list[user_id].email) == str(b_list[x].customer.email):
                    b_list.remove(b_list[x])
                    update_database()
                    print()
                    input("Booking cancelled! Press ENTER key to continue...")
                    user_main(user_id)
                elif x == len(b_list)-1:
                    wrong_id()
                    user_main(user_id)
    else:
        wrong_id() 
        user_main(user_id)   


def finish_b(td_id):
    if not b_list:
        no_bookings()
        td_main(td_id)
    else:
        for x in range (0, len(b_list)):
            if td_list[td_id].license_plate == b_list[x].taxi_driver.license_plate:
                b_list.remove(b_list[x])
                update_database()
                print()
                input("Booking completed! Press ENTER key to continue...")
                td_main(td_id) 
            elif x == len(b_list)-1:
                no_bookings()
                td_main(td_id)
                

def no_bookings():
    print()
    input("NO BOOKINGS! Press ENTER to return to main menu...")


def add_b():
    print()
    booking_no = len(b_list)
    for x in range (0,len(b_list)-1):
        if booking_no == b_list[x].id:
            booking_no += 1
    time = input("Enter Pick Up Time: ")
    date = input("Enter Pick Up Date: ")
    address = input("Enter Drop Off Address: ")
    c_id = input("Enter Customer ID number: ")
    if c_id.isdigit():
        c_id = int(c_id)
        if c_id in range(0, len(c_list)):
            customer = c_list[c_id]
            td_id = input("Enter Taxi Driver ID number: ")
            if td_id.isdigit():
                td_id = int(td_id)
                if td_id in range(0, len(td_list)):
                    for x in range (0, len(td_list)):
                        if td_list[x].license_plate == td_list[td_id].license_plate:
                            wrong_id()
                            admin_main()
                        else:
                            taxi_driver = td_list[td_id]
                            b = TripBooking(customer, taxi_driver, booking_no, time, date, address)
                            b_list.append(b)
                            update_database()
                            input("Booking added! Press ENTER key to continue...")
                            admin_main()
                            return b_list
                else:
                    wrong_id()
                    admin_main()
            else:
                wrong_id()
                admin_main()
        else:
            wrong_id()
            admin_main()
    else:
        wrong_id()
        admin_main()


def remove_b():
    print()
    b_id = input("Please, enter your Booking Number: ")
    if b_id.isdigit():
        b_id = int(b_id)
        if not b_list:
            no_bookings()
            admin_main()
        else:
            for x in range (0, len(b_list)):
                if b_id == int(b_list[x].id):
                    b_list.remove(b_list[b_id])
                    update_database()
                    print()
                    input("Booking cancelled! Press ENTER key to continue...")
                    admin_main()
                elif x == len(b_list)-1 and b_id != int(b_list[x].id):
                    wrong_id()
                    admin_main()         
    else:
        wrong_id() 
        admin_main()


def show_c():
    print()
    c_id = input("Enter Customer ID Number: ")
    if c_id.isdigit():
        c_id = int(c_id)
        if c_id in range(0, len(c_list)):
            c_list[c_id].show_customer()
        else:
            wrong_id()
            admin_main()
    else:
        wrong_id()
        admin_main()


def show_td():
    print()
    td_id = input("Enter Taxi Driver ID Number: ")
    if td_id.isdigit():
        td_id = int(td_id)
        if td_id in range(0, len(td_list)):
            td_list[td_id].show_taxi_driver()
        else:
            wrong_id()
            admin_main()
    else:
        wrong_id()
        admin_main()


def show_b():
    print()
    b_id = input("Enter Booking Number: ")
    if b_id.isdigit():
        b_id = int(b_id)
        if not b_list:
            no_bookings()
            admin_main()
        else:
            for x in range (0, len(b_list)):
                if b_id == int(b_list[x].id):
                    b_list[x].show_booking(x)
                elif x == len(b_list)-1 and b_id != int(b_list[x].id):
                    wrong_id()
                    admin_main()
    else:
        wrong_id()
        admin_main()


def user_show_booking(user_id):
    b_id = input("Enter Booking Number: ")
    if b_id.isdigit():
        b_id = int(b_id)
        if not b_list:
            no_bookings()
            user_main(user_id)
        else:
            for x in range(0, len(b_list)):
                if c_list[user_id].email == b_list[x].customer.email and c_list[user_id].password == b_list[
                    x].customer.password and b_id == int(b_list[x].id):
                    print()
                    print("BOOKING INFORMATION REQUESTED:")
                    print("Booking Number: " + b_list[x].id)
                    print("Customer Name: " + b_list[x].customer.name)
                    print("Customer Address: " + b_list[x].customer.address)
                    print("Customer Email: " + b_list[x].customer.email)
                    print("Customer Phone Number: " + b_list[x].customer.phone_number)
                    print("Taxi Driver Name: " + b_list[x].taxi_driver.driver_name)
                    print("Taxi License Plate: " + b_list[x].taxi_driver.license_plate)
                    print("Pick Up Time: " + b_list[x].pick_up_time)
                    print("Pick Up Date: " + b_list[x].date)
                    print("Drop Off Address: " + b_list[x].drop_off_address)
                    print()
                    input("Press ENTER to go back to main menu...")
                    user_main(user_id)
                elif x == len(b_list)-1:
                    wrong_id()
                    user_main(user_id)
    else:
        wrong_id()
        user_main(user_id)


def taxi_show_booking(td_id):
    if not b_list:
        no_bookings()
        td_main(td_id)
    else:
        for b_id in range (0, len(b_list)):
            if td_list[td_id].license_plate == b_list[b_id].taxi_driver.license_plate:
                print()
                print("BOOKING INFORMATION REQUESTED:")
                print("Booking Number: " + b_list[b_id].id)
                print("Customer Name: " + b_list[b_id].customer.name)
                print("Customer Address: " + b_list[b_id].customer.address)
                print("Customer Email: " + b_list[b_id].customer.email)
                print("Customer Phone Number: " + b_list[b_id].customer.phone_number)
                print("Taxi Driver Name: " + b_list[b_id].taxi_driver.driver_name)
                print("Taxi License Plate: " + b_list[b_id].taxi_driver.license_plate)
                print("Pick Up Time: " + b_list[b_id].pick_up_time)
                print("Pick Up Date: " + b_list[b_id].date)
                print("Drop Off Address: " + b_list[b_id].drop_off_address)
                print()
                input("Press ENTER to go back to main menu...")
                td_main(td_id)
            else:
                no_bookings()
                td_main(td_id)


def back_to_menu():
    print()
    input("Press ENTER to go back to admin main menu...")
    admin_main()
    

def wrong_id():
    print()
    input("WRONG ID! Please input the correct ID! Press ENTER to continue...")


def load_database():
    pass


def update_database():
    pass


def admin_main():
    print()
    print("This is the Admin menu")
    print("'c' to add a Customer")
    print("'show c' to show Customer details")
    print("'td' to add a Taxi Driver")
    print("'show td' to show Taxi Driver details")
    print("'b' to add a Booking")
    print("'r' to remove a Booking")
    print("'show b' to show Booking details")
    print("'q' to quit to main menu")
    menu = input("What you want to do? ").lower()
    if menu == "c":
        add_c()
    elif menu == "show c":
        show_c()
    elif menu == "td":
        add_td()
    elif menu == "show td":
        show_td()
    elif menu == "b":
        add_b()
    elif menu =="r":
        remove_b()
    elif menu == "show b":
        show_b()
    elif menu == "q":
        print()
        input("Press ENTER to quit...")
        main()
    else:
        print()
        input("WRONG COMMAND! Please input correct command! Press ENTER to continue...")
        admin_main()


def user_main(user_id):
    print()
    print("Welcome, " + c_list[user_id].name)
    print("'show c' to show Customer details")
    print("'b' to make a Booking")
    print("'c' to cancel a booking")
    print("'show b' to show Booking details")
    print("'q' to quit to main menu")
    menu = input("What you want to do? ").lower()
    if menu == "show c":
        c_list[user_id].show_customer()
    elif menu == "b":
        make_b(user_id)
    elif menu == "show b":
        user_show_booking(user_id)
    elif menu == "c":
        cancel_b(user_id)
    elif menu == "q":
        print()
        input("Press ENTER to quit...")
        main()
    else:
        print()
        input("WRONG COMMAND! Please input correct command! Press ENTER to continue...")
        user_main(user_id)


def td_main(td_id):
    print()
    print("Welcome, " + td_list[td_id].driver_name)
    print("'show td' to show Taxi driver details")
    print("'f' to complete a booking")
    print("'show b' to show Booking details")
    print("'q' to quit to main menu")
    menu = input("What you want to do? ").lower()
    if menu == "show td":
        print()
        print("TAXI DRIVER INFORMATION REQUESTED:")
        print("Taxi Driver Name: " + td_list[td_id].driver_name)
        print("Taxi License Plate: " + td_list[td_id].license_plate)
        print()
        input("Press ENTER to continue...")
        td_main(td_id)
    elif menu == "show b":
        taxi_show_booking(td_id)
    elif menu == "f":
        finish_b(td_id)
    elif menu == "q":
        print()
        input("Press ENTER to quit...")
        main()
    else:
        print()
        input("WRONG COMMAND! Please input correct command! Press ENTER to continue...")
        td_main(td_id)


def main():
    print()
    print("This is the Main menu")
    print("'l' to log into Customer account")
    print("'c' to register new customer")
    print("'t' to log into taxi driver")
    print("'a' to log into Admin account")
    print("'q' to exit program")
    action = input("What you want to do? ").lower()
    if action == "l":
        user_email = input("Enter User Email: ")
        user_password = input("Enter User Password: ")
        for x in range (len(c_list)):
            if user_email == c_list[x].email and user_password == c_list[x].password:
                user_id = x
                # get index number
                user_main(user_id)
            elif x == len(c_list)-1:
                print()
                input("WRONG EMAIL OR PASSWORD! Press ENTER to continue...")
                main()
                return
    elif action == "c":
        register_c()
    elif action== "t":
        no_plate = input("Enter Taxi Number Plate: ")
        taxi_password = input("Enter User Password: ")
        for x in range (len(td_list)):
            if no_plate == td_list[x].license_plate and taxi_password == td_list[x].password:
                td_id = x
                # get index number
                td_main(td_id)
            elif x == len(td_list)-1:
                print()
                input("WRONG PLATE NUMBER OR PASSWORD! Press ENTER to continue...")
                main()
                return
    elif action == "a":
        admin_main()
    elif action == "q":
        print()
        input("Press ENTER to exit program, BYE!")
    else:
        print()
        input("WRONG COMMAND! Please input correct command! Press ENTER to continue...")
        main()


if __name__ == '__main__':
    c_list = [Customer("0", "Demo", "Demo address", "a", "a", "12341234123","1234123412341234")]
    td_list = [TaxiDriver("0", "Demo driver", "ABC 123","1234"),TaxiDriver("1", "Demo driver 2", "ABC 456", "1234")]
    b_list = [TripBooking(c_list[0], td_list[0], "0", "9.00am", "01/01/2021", "Demo address 2"), TripBooking(c_list[0
    ], td_list[1], "1", "9.00am", "01/01/2021", "Demo address 3")]
    load_database()
    main()