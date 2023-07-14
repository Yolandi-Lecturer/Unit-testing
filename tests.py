# import the function
from functions import hotel_cost, plane_cost, car_rental, holiday_cost


def test_hotel_cost():
    #arrange
    num_nights = 2

    #act
    result = hotel_cost(num_nights)

    #assert
    assert result == 1800

def test_plane_cost():

    #assert
    city_flight = 1

    #act
    result = plane_cost(city_flight)

    #assert 
    assert result == 2500


def test_car_rental():

    #assert
    rental_days = 1

    #act
    result = car_rental(rental_days)

    #assert 
    assert result == 1000

def test_holiday_cost():
    "Test to verify the length of the name entered"

    #assert
    hotel_cost = 1800
    plane_cost = 2500
    car_rental = 1000

    #act
    result = holiday_cost(hotel_cost, plane_cost, car_rental)

    #assert 
    assert result == 5300