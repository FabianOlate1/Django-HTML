from aplicacion.models import pedidos, producto
from rest_framework import serializers

class ProductoSrlz(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__' #['__all__']
        
class PedidoSrlz(serializers.ModelSerializer):
    class Meta:
        model = pedidos
        fields = '__all__' #['__all__']