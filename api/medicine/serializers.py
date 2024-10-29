from rest_framework import serializers

from .models import (
    Generic,
    Manufacturer,
    Medicine
)



class GenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generic
        fields = (
            "id",
            "name"
        )


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = (
            "id",
            "name"
        )


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = (
            "id",
            "manufacturer",
            "generic",
            "generic_unit",
            "name",
            "no_of_tablets",
            "price",
            "batch_number",
            "description",
        )

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context.update({
            "manufacturer": ManufacturerSerializer(instance.manufacturer).data,
            "generic": GenericSerializer(instance.generic).data

        })
        return context