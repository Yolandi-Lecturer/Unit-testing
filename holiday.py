from functions import hotel_cost, plane_cost, car_rental, holiday_cost

city_flight = int(input('''Which city do you want to visit? 
1. Cape Town\n
2. Durban\n
3. Port Elizabeth'''))
num_nights = int(input("How many nights? "))
rental_days = int(input("For how many days do you want to rent a car for?"))

hotel = hotel_cost(num_nights)
plane = plane_cost(city_flight)
car = car_rental(rental_days)
total_cost = holiday_cost(hotel, plane, car)

print(f"The hotel cost for {num_nights} nights is R {hotel}")
print(f"The plane ticket to {city_flight} is R {plane}") 
print(f"The rental cost for {rental_days} days is R {car}")
print(f"The total holiday cost is R {total_cost}") 

