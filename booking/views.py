from django.shortcuts import render, redirect
from booking.models import Hotel, City, Reservation
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Sum

def index(request):
	return render(request, 'booking/index.html')

def hotels(request):
	return render(request, 'booking/hotels.html')

def reservation(request):
	if request.method == 'GET'              \
		and 'hotel' in request.GET          \
    	and 'arrival_date' in request.GET   \
    	and 'departure_date' in request.GET \
    	and 'nr_rooms' in request.GET:

		hotelId = request.GET['hotel']
		arrival_date = request.GET['arrival_date']
		departure_date = request.GET['departure_date']
		nr_rooms = request.GET['nr_rooms']
		hotel = Hotel.objects.filter(id=hotelId)[0]

		return render(request, 'booking/reservation.html', {
			'hotel': hotel,
			'arrival_date': arrival_date,
			'departure_date': departure_date,
			'nr_rooms': nr_rooms,
		})
	else:
		hotels = Hotel.objects.all()
		return render(request, 'booking/reservation.html', {
			'hotels': hotels	
		})

def search(request):
	if request.method == 'POST':
		city = request.POST['city']
		arrival_date = request.POST['arrival_date']
		departure_date = request.POST['departure_date']
		nr_rooms = request.POST['nr_rooms']
		max_price = request.POST['max_price']

		cityName = City.objects.filter(id=city)[0]
		hotels = Hotel.objects.filter(city_id=city).order_by('-price')

		# available_rooms = Reservation.objects.raw('''SELECT hotel_id AS id, booking_hotel.city_id, 
		# 													booking_hotel.price, 
		# 													sum(total_rooms) AS total_rooms 
		# 											 FROM booking_reservation 
		# 											 INNER JOIN booking_hotel ON booking_reservation.hotel_id = booking_hotel.id 
		# 											 WHERE departure >= %s 
		# 											 	AND booking_hotel.city_id = %s 
		# 										 	 GROUP BY hotel_id 
		# 										 	 ORDER BY price 
		# 										 	 	ASC''', [departure_date, city])

		# available_rooms = Reservation.objects.filter(departure__gte=departure_date).select_related('hotel_id').aggregate(total_rooms=Sum('total_rooms'))

		return render(request, 'booking/search.html', {
			'hotels': hotels,
			'city': cityName,
			'arrival_date': arrival_date,
			'departure_date': departure_date,
			'nr_rooms': nr_rooms,
			'max_price': max_price
		})
	else:
		return render(request, 'booking/search.html')

def book(request):
	if request.method == 'POST'              \
		and 'hotel' in request.POST          \
		and 'arrival_date' in request.POST   \
		and 'departure_date' in request.POST \
		and 'nr_rooms' in request.POST 		 \
		and 'first_name' in request.POST     \
		and 'last_name' in request.POST 	 \
		and 'phone_nr' in request.POST 		 \
		and 'email' in request.POST 		 \
		and 'totalPrice' in request.POST 	 \
		and 'totalDays' in request.POST:

		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		phone = request.POST['phone_nr']
		email = request.POST['email']
		hotel_id = request.POST['hotel']
		arrival_date = request.POST['arrival_date']
		departure_date = request.POST['departure_date']
		total_rooms = request.POST['nr_rooms']
		total_cost = request.POST['totalPrice']
		total_days = request.POST['totalDays']


		hotel = Hotel.objects.filter(id=hotel_id)[0]
		city = City.objects.filter(id=hotel.city_id)[0]

		reserved_rooms = Reservation.objects.filter(departure__gte=departure_date).filter(arrival__lte=arrival_date).filter(hotel_id=hotel_id).aggregate(total_rooms=Sum('total_rooms'))

		if int(total_rooms) <= int(hotel.nr_rooms):
			Reservation.objects.create(
				first_name = first_name,
				last_name = last_name,
				phone = phone,
				email = email,
				hotel = hotel,
				arrival = arrival_date,
				departure = departure_date,
				total_rooms = total_rooms,
				total_cost = total_cost
			)

			messages.add_message(request, messages.INFO, 'Hotel booked successfully!')

			return render(request, 'booking/booked.html', {
				'arrival_date': arrival_date,
				'departure_date': departure_date,
				'total_price': total_cost,
				'total_days': total_days,
				'first_name': first_name,
				'last_name': last_name,
				'total_rooms': total_rooms,
				'hotel_name': hotel.name,
				'city': city,
				'phone': phone,
				'email': email
			})
		else:
			messages.add_message(request, messages.INFO, "We're so sorry, but the hotel is fully booked!")
			return redirect('reservation')

	else:
		messages.add_message(request, messages.INFO, "Something went horribly wrong. Try again maybe?")
		return redirect('reservation')

def booked(request):
	return render(request, 'booking/booked.html')
