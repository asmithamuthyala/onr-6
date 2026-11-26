# HOTEL RESERVATION SYSTEM

rooms = {
    101: {"type": "Single", "price": 1500, "status": "Available"},
    102: {"type": "Single", "price": 1500, "status": "Available"},
    201: {"type": "Double", "price": 2500, "status": "Available"},
    202: {"type": "Double", "price": 2500, "status": "Available"},
    301: {"type": "Deluxe", "price": 4000, "status": "Available"}
}

bookings = {}

def display_rooms():
    print("\n------ ROOM DETAILS ------")
    print("Room No | Type   | Price | Status")
    for room_no, details in rooms.items():
        print(room_no, "|", details["type"], "| Rs.",
              details["price"], "|", details["status"])

def book_room():
    display_rooms()

    room_no = int(input("\nEnter room number: "))

    if room_no in rooms:
        if rooms[room_no]["status"] == "Available":

            name = input("Enter customer name: ")
            phone = input("Enter phone number: ")
            days = int(input("Enter number of days: "))

            if days <= 0:
                print("Please enter a valid number of days.")
                return

            price = rooms[room_no]["price"]
            total = price * days

            bookings[room_no] = {
                "name": name,
                "phone": phone,
                "days": days,
                "total": total
            }

            rooms[room_no]["status"] = "Booked"

            print("\nRoom booked successfully!")
            print("Customer Name:", name)
            print("Room Number:", room_no)
            print("Total Amount: Rs.", total)

        else:
            print("Sorry! This room is already booked.")
    else:
        print("Invalid room number.")

def checkout():
    room_no = int(input("\nEnter room number for checkout: "))

    if room_no in bookings:
        customer = bookings[room_no]

        print("\n------ HOTEL BILL ------")
        print("Customer Name:", customer["name"])
        print("Phone Number:", customer["phone"])
        print("Room Number:", room_no)
        print("Number of Days:", customer["days"])
        print("Total Amount: Rs.", customer["total"])
        print("------------------------")
        print("Thank you for staying with us!")

        rooms[room_no]["status"] = "Available"
        del bookings[room_no]

    else:
        print("No booking found for this room.")

def view_bookings():
    print("\n------ CURRENT BOOKINGS ------")

    if not bookings:
        print("No bookings available.")
    else:
        for room_no, customer in bookings.items():
            print("\nRoom Number:", room_no)
            print("Customer Name:", customer["name"])
            print("Phone:", customer["phone"])
            print("Days:", customer["days"])
            print("Amount: Rs.", customer["total"])

# MAIN PROGRAM

while True:
    print("\n================================")
    print("     HOTEL RESERVATION SYSTEM")
    print("================================")
    print("1. View Rooms")
    print("2. Book a Room")
    print("3. View Bookings")
    print("4. Checkout")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        display_rooms()

    elif choice == "2":
        book_room()

    elif choice == "3":
        view_bookings()

    elif choice == "4":
        checkout()

    elif choice == "5":
        print("Thank you for using Hotel Reservation System!")
        break

    else:
        print("Invalid choice! Please try again.")