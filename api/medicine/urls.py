from django.urls import path

from .views import (
    ListCreateGeneric,
    ListCreateManufacturer,
    ListMedicine,
    CreateMedicine,
    RetrieveUpdateDestroyMedicine,
    SearchMedicine,
    FetchGenericAndManufactuer,
    Dashboard
)


urlpatterns = [
    path('dashboard/',
         Dashboard.as_view(),
         name='dashboard'
         ),
    path('list-create-generic/',
         ListCreateGeneric.as_view(),
         name='list-create-generic'
         ),
    path('list-create-manufacturer/',
         ListCreateManufacturer.as_view(),
         name='list-create-manufacturer'),
    path('list-medicine/',
         ListMedicine.as_view(),
         name='list-medicine'),
     path('create-medicine/',
         CreateMedicine.as_view(),
         name='create-medicine'),
    path('retrieve-update-destroy-medicine/<int:pk>/',
         RetrieveUpdateDestroyMedicine.as_view(),
         name='retrieve-update-destroy-medicine'),
     path("search-medicine/",
          SearchMedicine.as_view(),
          name='search-medicine'
          ),
     path("fetch-generic-and-manufactuer/",
          FetchGenericAndManufactuer.as_view(),
          name='fetch-generic-and-manufactuer'
          )
]