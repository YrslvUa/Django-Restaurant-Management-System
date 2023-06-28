from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Menu
        fields = "__all__"