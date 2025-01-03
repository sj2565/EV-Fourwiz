from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from graph.fields import ThumbnailImageField


# Create your models here.
class Data(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True)
    content = models.TextField('CONTENT')
    image = ThumbnailImageField('IMAGE', upload_to='athumb/%Y/%m', null=True)

    class Meta :
        verbose_name="data"
        verbose_name_plural = 'datas'
        db_table = 'graph_datas'
        ordering = ('id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # graph 앱 중 url 이름이 data_detail인 항목을 찾음 / args는 매개변수
        return reverse('graph:data_detail', args=(self.id,))



    # 모델 객체를 데이터베이스에 저장(영상보고 복습)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
