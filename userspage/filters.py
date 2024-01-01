import django_filters
from demo_app.models import *
from django_filters import CharFilter


class FoodFilter(django_filters.FilterSet):
	foodname_contains=CharFilter(field_name='food_name',lookup_expr='icontains')

	class Meta:
		model=Food
		fields=''
		exclude=['food_price','food_description','Food_image','category','hotel']




class HotelFilter(django_filters.FilterSet):
	hotel=CharFilter(field_name='hotel',lookup_expr='icontains')

	class Meta:
		model=Food
		fields=''
		exclude=['food_price','food_description','Food_image','category','food_name']




