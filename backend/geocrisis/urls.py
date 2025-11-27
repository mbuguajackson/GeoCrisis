from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import IncidentViewSet

#Create router and register our viewsets with it
router=DefaultRouter()
router.register(r'api/incidents',IncidentViewSet, basename='incidents')

# The API URLs are now determined automatically by the router.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    #Add API Authentication URLs for the browserble API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] 
