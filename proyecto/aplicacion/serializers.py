from aplicacion.models import producto
from rest_framework import serializers

class ProductoSrlz(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__' #['__all__']