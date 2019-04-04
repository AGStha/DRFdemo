from django.urls import path,include
from api.views import HelloAPIView,HelloViewset,ProductViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-viewset", HelloViewset, base_name="hello_viewset")
router.register("products", ProductViewset)

urlpatterns= [
    
path("", include(router.urls)),
path("hello/", HelloAPIView.as_view(),name='hello')
]