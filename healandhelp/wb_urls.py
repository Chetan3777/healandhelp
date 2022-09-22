from django.urls import path, include 
from healandhelp import views
from rest_framework.routers import DefaultRouter
 
 
router = DefaultRouter()
router.register('registration', views.WebsiteViewSet, basename='registration')
router.register('list', views.Listing, basename='list')


urlpatterns = [
    # path('',include('user.urls'))
    path('registration_api/', include(router.urls)),
]
 

