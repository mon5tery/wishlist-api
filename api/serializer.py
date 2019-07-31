from rest_framework import serializers
from django.contrib.auth.models import User
from items.models import Item, FavoriteItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]

class ItemListSerializer(serializers.ModelSerializer):
    added_by = UserSerializer()
    favs = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
    view_name='api-detail',
    read_only=True,
    lookup_field = 'id',
    lookup_url_kwarg = 'item_id'
    )
    class Meta:
        model = Item
        fields = ['image', 'name', 'url', 'favs', 'added_by']

    def get_favs(self, obj):
        return obj.favs.count()

class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Item
        fields = ["id", 'user']

class ItemDetailSerializer(serializers.ModelSerializer):
    favs = FavoriteSerializer(many=True)
    class Meta:
        model = Item
        fields = '__all__'
