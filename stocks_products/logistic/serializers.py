from rest_framework import serializers
from .models import Stock, Product, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description"]


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ["product", "quantity", "price"]


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ["id", "positions", "address"]

    def create(self, validated_data):
        positions = validated_data.pop("positions")
        stock = super().create(validated_data)
        for pos in positions:
            stock.positions.create(**pos)
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop("positions")
        stock = super().update(instance, validated_data)
        for pos in positions:
            stock.positions.update_or_create(product=pos["product"], defaults={**pos})

        return stock
