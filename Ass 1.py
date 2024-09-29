from datetime import datetime  # Importing datetime module to handle dates and times


class Guest:
    def __init__(self, guestID, name, email, password, phoneNumber):
        # Constructor method initializing guest details
        self.__guestID = guestID  # Private attribute for guest ID
        self.__name = name  # Private attribute for guest name
        self.__email = email  # Private attribute for guest email
        self.__password = password  # Private attribute for guest password
        self.__phoneNumber = phoneNumber  # Private attribute for guest phone number

    # Getter and Setter Methods
    def getGuestID(self):
        return self.__guestID  # Returns guest ID
    def setGuestID(self, id):
        self.__guestID = id  # Sets guest ID

    def getName(self):
        return self.__name  # Returns guest name
    def setName(self, name):
        self.__name = name  # Sets guest name

    def getEmail(self):
        return self.__email  # Returns guest email
    def setEmail(self, email):
        self.__email = email  # Sets guest email

    def getPassword(self):
        return self.__password  # Returns guest password
    def setPassword(self, password):
        self.__password = password  # Sets guest password

    def getPhoneNumber(self):
        return self.__phoneNumber  # Returns guest phone number
    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber  # Sets guest phone number

    def makeReservation(self, room, dateIn, dateOut):
        # Method to create a reservation for a guest
        return Reservation(self, room, dateIn, dateOut)

    def cancelReservation(self, reservationID):
        # Method to cancel a reservation
        print(f"Reservation {reservationID} canceled.")

    def viewConfirmation(self, reservation):
        # Method to view reservation confirmation
        print(f"Reservation ID: {reservation.getReservationID()}")

    def modifyReservation(self, reservation):
        # Method to modify a reservation
        print("Modify your reservation here.")


class Reservation:
    def __init__(self, guest, room, checkInDate, checkOutDate):
        # Constructor method initializing reservation details
        self.__reservationID = id(self)  # Generate unique reservation ID
        self.__guest = guest  # Private attribute for guest
        self.__room = room  # Private attribute for room
        self.__checkInDate = checkInDate  # Private attribute for check-in date
        self.__checkOutDate = checkOutDate  # Private attribute for check-out date
        self.__totalCost = self.calculateCost()  # Calculate total cost for the stay
        self.__numberOfGuests = 1  # Default number of guests set to 1

    # Getter and Setter Methods
    def getReservationID(self):
        return self.__reservationID  # Returns reservation ID
    def setReservationID(self, id):
        self.__reservationID = id  # Sets reservation ID

    def getGuest(self):
        return self.__guest  # Returns guest object
    def setGuest(self, guest):
        self.__guest = guest  # Sets guest object

    def getRoom(self):
        return self.__room  # Returns room object
    def setRoom(self, room):
        self.__room = room  # Sets room object

    def getCheckInDate(self):
        return self.__checkInDate  # Returns check-in date
    def setCheckInDate(self, date):
        self.__checkInDate = date  # Sets check-in date

    def getCheckOutDate(self):
        return self.__checkOutDate  # Returns check-out date
    def setCheckOutDate(self, date):
        self.__checkOutDate = date  # Sets check-out date

    def getTotalCost(self):
        return self.__totalCost  # Returns total cost of reservation
    def setTotalCost(self, cost):
        self.__totalCost = cost  # Sets total cost of reservation

    def getNumberOfGuests(self):
        return self.__numberOfGuests  # Returns number of guests
    def setNumberOfGuests(self, numberGuest):
        self.__numberOfGuests = numberGuest  # Sets number of guests

    def confirmReservation(self):
        # Method to confirm the reservation
        return True

    def cancelReservation(self):
        # Method to cancel the reservation
        print("Reservation canceled.")

    def calculateCost(self):
        # Method to calculate the cost of stay based on room price and nights
        nights = (self.__checkOutDate - self.__checkInDate).days  # Calculate number of nights
        return nights * self.__room.getPricePerNight()  # Multiply by price per night


class Room:
    def __init__(self, roomID, roomType, pricePerNight, bedCount):
        # Constructor method initializing room details
        self.__roomID = roomID  # Private attribute for room ID
        self.__roomType = roomType  # Private attribute for room type
        self.__availability = True  # Set room availability to True by default
        self.__pricePerNight = pricePerNight  # Private attribute for price per night
        self.__bedCount = bedCount  # Private attribute for number of beds

    # Getter and Setter Methods
    def getRoomID(self):
        return self.__roomID  # Returns room ID
    def setRoomID(self, id):
        self.__roomID = id  # Sets room ID

    def getRoomType(self):
        return self.__roomType  # Returns room type
    def setRoomType(self, type):
        self.__roomType = type  # Sets room type

    def getAvailable(self):
        return self.__availability  # Returns room availability status
    def setAvailability(self, isAvailable):
        self.__availability = isAvailable  # Sets room availability status

    def getPricePerNight(self):
        return self.__pricePerNight  # Returns room price per night
    def setPricePerNight(self, price):
        self.__pricePerNight = price  # Sets room price per night

    def getBedCount(self):
        return self.__bedCount  # Returns number of beds in the room
    def setBedCount(self, count):
        self.__bedCount = count  # Sets number of beds in the room

    def checkAvailability(self, dateIn, dateOut):
        # Check if the room is available for the given dates
        return self.__availability

    def reserveRoom(self):
        # Reserve the room by setting availability to False
        self.__availability = False

    def releaseRoom(self):
        # Release the room by setting availability to True
        self.__availability = True


class Payment:
    def __init__(self, paymentID, amount, paymentMethod, status, transactionDate):
        # Constructor method initializing payment details
        self.__paymentID = paymentID  # Private attribute for payment ID
        self.__amount = amount  # Private attribute for payment amount
        self.__paymentMethod = paymentMethod  # Private attribute for payment method
        self.__status = status  # Private attribute for payment status
        self.__transactionDate = transactionDate  # Private attribute for transaction date

    # Getter and Setter Methods
    def getPaymentID(self):
        return self.__paymentID  # Returns payment ID
    def setPaymentID(self, id):
        self.__paymentID = id  # Sets payment ID

    def getAmount(self):
        return self.__amount  # Returns payment amount
    def setAmount(self, amount):
        self.__amount = amount  # Sets payment amount

    def getPaymentMethod(self):
        return self.__paymentMethod  # Returns payment method
    def setPaymentMethod(self, method):
        self.__paymentMethod = method  # Sets payment method

    def getStatus(self):
        return self.__status  # Returns payment status
    def setStatus(self, status):
        self.__status = status  # Sets payment status

    def getTransactionDate(self):
        return self.__transactionDate  # Returns transaction date
    def setTransactionDate(self, date):
        self.__transactionDate = date  # Sets transaction date

    def processPayment(self):
        # Process the payment and set the status to confirmed
        self.__status = 'confirmed'
        print(f"Payment processed for {self.__amount}")

    def refundPayment(self):
        # Refund the payment and set the status to refunded
        self.__status = 'refunded'
        return True


class Hotel:
    def __init__(self, hotelName, address, rating):
        # Constructor method initializing hotel details
        self.__hotelName = hotelName  # Private attribute for hotel name
        self.__address = address  # Private attribute for hotel address
        self.__rooms = []  # Initialize empty list for hotel rooms
        self.__reservations = []  # Initialize empty list for reservations
        self.__rating = rating  # Private attribute for hotel rating

    # Getter and Setter Methods
    def getHotelName(self):
        return self.__hotelName  # Returns hotel name
    def setHotelName(self, name):
        self.__hotelName = name  # Sets hotel name

    def getAddress(self):
        return self.__address  # Returns hotel address
    def setAddress(self, address):
        self.__address = address  # Sets hotel address

    def getRooms(self):
        return self.__rooms  # Returns list of rooms
    def setRooms(self, rooms):
        self.__rooms = rooms  # Sets list of rooms

    def getReservations(self):
        return self.__reservations  # Returns list of reservations
    def setReservations(self, reservations):
        self.__reservations = reservations  # Sets list of reservations

    def getRating(self):
        return self.__rating  # Returns hotel rating
    def setRating(self, rating):
        self.__rating = rating  # Sets hotel rating

    def addRoom(self, room):
        # Add a room to the hotel's list of rooms
        self.__rooms.append(room)

    def availableRooms(self):
        # Returns list of available rooms
        return [room for room in self.__rooms if room.getAvailable()]

    def reservationByID(self, reservationID):
        # Find a reservation by its ID
        for reservation in self.__reservations:
            if reservation.getReservationID() == reservationID:
                return reservation
        return None


# Example scenario demonstrating the classes
hotel = Hotel("Comfort Inn & Suites Los Alamo", "2455 Trinity Drive, Los Alamos, NM", 3.5)  # Create a hotel instance
hotel.addRoom(Room(1, "2 Queen Beds", 89.95, 2))  # Add room 1 to the hotel
hotel.addRoom(Room(2, "King Bed", 99.95, 1))  # Add room 2 to the hotel

guest = Guest(1, "Ted Vera", "tedvera@mac.com", "securePassword", "505-661-1110")  # Create a guest instance

checkIn = datetime(2023, 8, 22, 15, 0)  # Set check-in date
checkOut = datetime(2023, 8, 24, 12, 0)  # Set check-out date
reservation = guest.makeReservation(hotel.getRooms()[0], checkIn, checkOut)  # Make a reservation

payment = Payment(1, reservation.getTotalCost(), "Mastercard", "pending", datetime.now())  # Process payment
payment.processPayment()  # Mark payment as processed

# Print reservation confirmation
print("***************** Reservation Confirmation *****************")
print("Thank you for your reservation. Please print your hotel receipt and show it at check-in.")
print(f"Your Name: {guest.getName()}")  # Print guest name
print(f"Your Email: {guest.getEmail()}")  # Print guest email
print(f"Hotel Confirmation Number: {reservation.getReservationID()}")  # Print reservation ID
print("─────────────────────────────────────────────────────────────")
print(f"***************** {hotel.getHotelName()} *****************")  # Print hotel name
print(f"Address: {hotel.getAddress()}")  # Print hotel address
print(f"Rating: {hotel.getRating()}")  # Print hotel rating
print(f"Phone: {guest.getPhoneNumber()}")  # Print guest phone number
print("-------------------------------------------------------------")
print(f"Check-In: {reservation.getCheckInDate().strftime('%A, %b %d, %Y - %I:%M %p')}")  # Print formatted check-in date
print(f"Check-Out: {reservation.getCheckOutDate().strftime('%A, %b %d, %Y - %I:%M %p')}")  # Print formatted check-out date
print(f"Number of Nights: {(checkOut - checkIn).days}")  # Print number of nights
print(f"Number of beds: {hotel.getRooms()[0].getBedCount()}")  # Print number of beds
print("-------------------------------------------------------------")
print(f"Room: {hotel.getRooms()[0].getRoomID()} - {guest.getName()}")  # Print room ID and guest name
print("-------------------------------------------------------------")
print(f"Room Type: {hotel.getRooms()[0].getRoomType()}")  # Print room type
print("─────────────────────────────────────────────────────────────")
print("***************** Summary of Charges *****************")
print(f"Billing Name: {guest.getName()}")  # Print billing name
print(f"Credit Card: {payment.getPaymentMethod()} (ending in 9904)")  # Print payment method
print("-------------------------------------------------------------")
print(f"Room Cost: ${hotel.getRooms()[0].getPricePerNight():.2f}")  # Print room cost per night
print(f"Number of Rooms: 1")  # Print number of rooms
print(f"Room Subtotal: ${reservation.getTotalCost():.2f}")  # Print room subtotal
print(f"Taxes and Fees: $21.58")  # Print taxes and fees
print("-------------------------------------------------------------")
print(f"Total Charges: ${reservation.getTotalCost() + 21.58:.2f}")  # Print total charges
print("*************************************************************")