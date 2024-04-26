from rest_framework import serializers
from .models import Weather

# serializers.Serializer
#   - 모델 필드에는 없어도 추가로 변환
# serailizers.ModelSerializer
#   - 모델 필드에 정의된 데이터만 변환
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
