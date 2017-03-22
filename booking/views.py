from django.shortcuts import render, redirect
from booking.models import Hotel, City, Reservation
from django.views.generic import ListView, DetailView
from django.contrib import messages

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

		hotel_name = Hotel.objects.filter(id=hotel_id)[0]
		city = City.objects.filter(id=hotel_name.city_id)[0]

		Reservation.objects.create(
			first_name = first_name,
			last_name = last_name,
			phone = phone,
			email = email,
			hotel_id = hotel_id,
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
			'hotel_name': hotel_name,
			'city': city,
			'phone': phone,
			'email': email
		})

	else:
		messages.add_message(request, messages.INFO, "Something went horribly wrong. Try again maybe?")
		return redirect('reservation')

def booked(request):
	return render(request, 'booking/booked.html')