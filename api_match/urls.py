from django.urls import include, path
from .views import VehicleCreate, VehicleList, VehicleDetail, VehicleUpdate, VehicleDelete


urlpatterns = [
    path('create/', VehicleCreate.as_view(), name='create-vehicle'),
    path('', VehicleList.as_view()),
    path('<int:pk>/', VehicleDetail.as_view(), name='retrieve-vehicle'),
    path('update/<int:pk>/', VehicleUpdate.as_view(), name='update-vehicle'),
    path('delete/<int:pk>/', VehicleDelete.as_view(), name='delete-vehicle')
]