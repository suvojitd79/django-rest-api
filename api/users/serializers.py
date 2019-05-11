from rest_framework import serializers
from .models import User

class user_serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('unique_id','email_id','password_id','timezone_id')