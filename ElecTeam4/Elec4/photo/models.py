from django.db import models
from django.urls import reverse
from photo.fields import ThumbnailImageField

# Create your models here.
class Album(models.Model):
    name = models.CharField('NAME', max_length=30)
    # 10-08 섬네일 - 사용자 정의 커스텀 필드
    image = ThumbnailImageField('IMAGE', upload_to='athumb/%Y/%m', null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                              verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('name',)    #튜플 형식

    # 객체를 문자열로 표현할 때 사용하는 함수
    def __str__(self):  #tostring()과 유사
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))    #접두사 photo


# #국산/외제
# class Country(models.Model):
#     docount = models.CharField('DOCOUNT', max_length=30)
#
#     class Meta:
#         ordering = ('DOCOUNT',)
#
#     def __str__(self):
#         return self.docount
#
#     def get_absolute_url(self):
#         return reverse('photo:country_detail', args=(self.id,))
#
# #차종(규격)
# class Standard(models.Model):
#     carsize = models.CharField('CARSIZE', max_length=30)
#
#     class Meta:
#         ordering = ('CARSIZE',)
#
#     def __str__(self):
#         return self.carsize
#
#
# #충전타입(급속)
# class Chargingrap(models.Model):
#     ratype = models.CharField('RATYPE', max_length=30)
#
#     class Meta:
#         ordering = ('RATYPE',)
#
#     def __str__(self):
#         return self.ratype
#
#
# #충전타입(완속)
# class Chargingsl(models.Model):
#     sltype = models.CharField('SLTYPE', max_length=30)
#
#     class Meta:
#         ordering = ('SLTYPE',)
#
#     def __str__(self):
#         return self.sltype
#
##### 아래 항목들은 foreignkey 사용해보려다 클래스 생성부터 실패. nonexistent field

    # country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)    #국산/외제
    # standard = models.ForeignKey(Standard, on_delete=models.CASCADE, blank=True, null=True) #차종(규격)
    # chargingrap = models.ForeignKey(Chargingrap, on_delete=models.CASCADE, blank=True, null=True)  #충전타입:급속
    # chargingsl = models.ForeignKey(Chargingsl, on_delete=models.CASCADE, blank=True, null=True)    #충전타입:완속

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  #제조사
    title = models.CharField('TITLE', max_length=50)        #모델명
    country = models.CharField('COUNTRY', max_length=50, null=True)       #국산/외제
    standard = models.CharField('STANDARD', max_length=50, null=True)     #차종(규격)
    raptype = models.CharField('RAPTYPE', max_length=50, null=True)       #충전타입:급속
    sltype = models.CharField('SLTYPE', max_length=50, null=True)         #충전타입:완속
    price = models.CharField('PRICE', max_length=50, blank=True, null=True)  #출시가(단위:만원)
    efficiency = models.CharField('EFFICIENCY', max_length=100, blank=True, null=True) #연비
    description = models.TextField('DESCRIPTION', blank=True, null=True) #비고

    image = ThumbnailImageField('IMAGE', upload_to='photo/%Y/%m')   #사용자 정의 커스텀 필드
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                              verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('album',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))