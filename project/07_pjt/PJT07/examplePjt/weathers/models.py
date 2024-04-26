from django.db import models


class Weather(models.Model):
    dt_txt = models.DateTimeField()   # 관측 시간
    temp = models.FloatField()        # 온도(기본값: 켈빈온도)
    feels_like = models.FloatField()  # 체감온도(기본값: 켈빈온도)
