from django_filters import filters
from api.models import Product
from django_filters.rest_framework import FilterSet

class ProductFilter(FilterSet):
	name = filters.CharFilter(field_name= "name", lookup_expr= "icontans")

	class Meta:
		model = Product
		fields = ["name"]
