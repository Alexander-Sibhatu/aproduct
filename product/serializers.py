from rest_framework import serializers
from .models import Product
from category.serializers import CategorySerializer
from category.models import Category

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),  # Use Category model for querying related instances
        source = 'category',    # Link this field to the 'category' ForeignKey in Product
        write_only = True,      # Hide this field in the serialized output; used for writes only
    )

    class Meta:
        model =  Product
        fields = ['id', 'name', 'description', 'price', 'category', 'category_id']