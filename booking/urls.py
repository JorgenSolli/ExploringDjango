from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from booking.models import Hotel, Reservation, City
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hotels/$', 
    	ListView.as_view(
    		queryset=City.objects.all(),
    		template_name="booking/hotels.html")
    	),

    url(r'^hotels/search/$', views.search, name='search'),
    url(r'^reservation/$', views.reservation, name='reservation'),
    url(r'^reservation/book$', views.book, name='book'),
    url(r'^booked/$', views.booked, name='booked')
]
