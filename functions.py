def hotel_cost(num_nights):
    total_hotel_cost = num_nights * 900
    return total_hotel_cost

def plane_cost(city_flight):
    if city_flight == 1:
        return 2500
    elif city_flight == 2:
        return 1500
    elif city_flight == 3:
        return 2000

def car_rental(rental_days):
    car_cost = rental_days * 1000
    return car_cost

def holiday_cost(hotel_cost, plane_cost, car_rental):
    
    total_holiday_cost = hotel_cost + plane_cost + car_rental
    return total_holiday_cost
