from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from api.models import Product
from api.filters import ProductFilter
from api.serializers import ProductSerializer

class HelloAPIView(APIView):
	def get(self,request):
		data={
		"hello":"This is hello"
		}
		return Response(data)
	def post(self,request):
		pass
	def put(self,request):
		pass
	def patch(self,request):
		pass
	def delete(self,request):
		pass
class HelloViewset(ViewSet):
	def list(self, request):
		data = {
			"hello": "This is a hello viewset"
				}
		return Response(data)

class ProductViewset(ModelViewSet):
	serializer_class= ProductSerializer
	queryset = Product.objects.all()
	filter_class = ProductFilter