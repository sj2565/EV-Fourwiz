from django.db import models
from django.urls import reverse


# 211007 추가
class CarCharger(models.Model):
    area = models.CharField(max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title allas.')
    address = models.CharField(max_length=50)
    spCharger = models.CharField(max_length=50)
    charger = models.CharField(max_length=50)
    spCar = models.CharField(max_length=100)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)

    class Meta:
        ordering = ['-lat']

    def __str__(self):
        return self.area

    def get_absolute_url(self):
        # blog 앱 중에서 url 이름이 post_detail인 항목을 찾아 줍니다.
        # args는 매개 변수를 의미합니다.
        return reverse('blog:map_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()
