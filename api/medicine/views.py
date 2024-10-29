from django.db.models import Q

from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from user_account.permissions import IsAdmin

from .models import (
    Generic,
    Manufacturer,
    Medicine
)
from .serializers import (
    GenericSerializer,
    ManufacturerSerializer,
    MedicineSerializer
)


class ListCreateGeneric(generics.ListCreateAPIView):
    model = Generic
    serializer_class = GenericSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin, ]
    queryset = Generic.objects.all()


class ListCreateManufacturer(generics.ListCreateAPIView):
    model = Manufacturer
    serializer_class = ManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin, ]
    queryset = Manufacturer.objects.all()


class ListMedicine(generics.ListAPIView):
    model = Medicine
    serializer_class = MedicineSerializer
    permission_classes = [permissions.AllowAny, ]
    queryset = Medicine.objects.all()


class CreateMedicine(generics.CreateAPIView):
    model = Medicine
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin, ]
    queryset = Medicine.objects.all()


class RetrieveUpdateDestroyMedicine(generics.RetrieveUpdateDestroyAPIView):
    model = Medicine
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin, ]
    queryset = Medicine.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"success": True}, status=status.HTTP_200_OK)


class SearchMedicine(APIView):
    def get(self, *args, **kwargs):
        search_key = self.request.GET.get("q", None)
        result = {
            "q": search_key,
            "data": []
        }
        if search_key:
            qs = Medicine.objects.filter(
                Q(name__icontains=search_key) |
                Q(generic__name__icontains=search_key)
            )
            serializer = MedicineSerializer(qs, many=True)
            result['data'] = serializer.data

            return Response(result, status=status.HTTP_200_OK)
        
        return Response(result, status=status.HTTP_200_OK)
    

class FetchGenericAndManufactuer(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin, ]

    def get(self, *args, **kwargs):
        data = {
            "generics": GenericSerializer(Generic.objects.all(), many=True).data,
            "manufacturers": ManufacturerSerializer(Manufacturer.objects.all(), many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)
    

class Dashboard(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin, ]

    def get(self, *args, **kwargs):
        data = {
            "generics": Generic.objects.count(),
            "manufacturers": Manufacturer.objects.count(),
            "medicines": Medicine.objects.count()
        }
        return Response(data, status=status.HTTP_200_OK)