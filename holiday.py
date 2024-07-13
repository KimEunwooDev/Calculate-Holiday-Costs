#This program will calculate a user's total holiday cost,
#which includes the plane cost, hotel cost, and car-rental cost.


#This function calculate total cost for the flight by cities.
def plane_cost(city_flight) : 
    while True :   #ask for input until the user enters the value in parentheses.
        city_flight = input("Choose one city you will be flying to : (seoul,paris,london,newyork,la) ").lower()
        if city_flight == "seoul":
            flight_cost = 1000
            break
        elif city_flight == "paris":
            flight_cost = 300
            break
        elif city_flight == "london":
            flight_cost = 450
            break  
        elif city_flight == "newyork":
            flight_cost = 650
            break
        elif city_flight == "la":
            flight_cost = 500
            break
        else :
            flight_cost = print("Choose one of city in parentheses.")
    return flight_cost


#This function calculate total cost for the hotel stay.
def hotel_cost(num_nights,night_charge=150) :
    total_hotel_cost = num_nights*night_charge
    return total_hotel_cost

#This function calculate the total cost of the car rental.
def car_rental(rental_days,rental_cost=80) :
    total_car_rental_cost = rental_days*rental_cost
    return total_car_rental_cost



city_flight = ""
flight_cost = plane_cost(city_flight)
print(f"Your plane cost is ￡{flight_cost}")     #Print out the total cost for the flight cost.


#get input from user the number of nights they will be staying at a hotel, 
num_nights = int(input("The number of nights you will be staying at a hotel : "))
#Print out the total cost for the hotel stay.
print("Your total hotel cost is ￡",int(hotel_cost(num_nights)))


#get input from user the number of days for which they will be hiring a car. 
rental_days = int(input("The number of days you will be hiring a car : "))
print(f"Your total rental cost is ￡{car_rental(rental_days)}") #Print out the total cost for the car rental.
   


#Function to calculate a user's total holiday cost.
def holiday_cost(hotel_cost,flight_cost,car_rental) :
    total_holiday_cost = hotel_cost+flight_cost+car_rental
    return total_holiday_cost

hotel_cost = hotel_cost(num_nights)
car_rental = car_rental(rental_days)    

total_holiday_cost = holiday_cost(hotel_cost,flight_cost,car_rental)
print(f"Your total holiday cost is ￡{total_holiday_cost}")

