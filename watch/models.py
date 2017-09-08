# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=250, unique=True)
    des = models.CharField(max_length=500)
    origin =  models.CharField(max_length=100)
    logo =  models.FileField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('watch:detail', kwargs={'pk': self.pk})



class Watch(models.Model):
    watch_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name =  models.CharField(max_length=50, verbose_name="名稱")
    year =  models.CharField(max_length=10, verbose_name="Year")
    price = models.IntegerField()
    code = models.CharField(max_length=20, verbose_name="Code")
    ref_no = models.CharField(max_length=30, verbose_name="Ref. No.")
    type = models.CharField(max_length=50, verbose_name="Type", choices=(('all', '男女款'),('men', "男款"),('women', "女款")))
    movement = models.CharField(max_length=50, verbose_name="機芯", choices=(('automatic', '	自動發條'),('manual', '機械錶')))
    case_material = models.CharField(max_length=30, verbose_name="錶面材料")
    case_size = models.CharField(max_length=50, verbose_name="錶面大小", choices=(('<26', '<26 mm'), ('26-30', '26-30 mm'),('31-35', '31-35 mm'), ('36-39', '36-39 mm'),('40-41', "40-41 mm"),('42-43', "42-43mm"), ('>43', '>43 mm')),blank=True)
    color = models.CharField(max_length=30, verbose_name = "顏色",choices=(("black","黑"),("bronze","銅"),("champagne","香濱金"),("green","綠"),("navy","海軍藍"),("silver","銀"),("white","白"),("beige","米"),("blue","藍"),("brown","啡"),("pink","粉紅"),("black","黑"),("bronze","銅"),("champagne","香濱金"),("green","綠"),("navy","海軍藍"),("silver","銀"),("white","白"),("beige","米"),("blue","藍"),("brown","啡"),("pink","粉紅")), blank=True)
    # bracelet_material = models.CharField(max_length=30, verbose_name="Bracelet Material")
    # bracelet_color = models.CharField(max_length=30, verbose_name="Bracelet Color")
    # bracelet_length = models.CharField(max_length=30, verbose_name="Bracelet Length")
    style = models.CharField(max_length=50, verbose_name="款式", choices=(('casual', '休閒'),('military', "軍事"),('pilot', "機師"),("sport","運動"),("dive","潛水"),("dress","晚宴"),("racing","賽車")), blank=True)
    pic = models.ImageField()
    # Pictures for product detail page
    pic_s = models.ImageField()
    pic2_s = models.ImageField()
    pic3_s = models.ImageField()
    pic4_s = models.ImageField()
    pic_l = models.ImageField()
    pic2_l = models.ImageField()
    pic3_l = models.ImageField()
    pic4_l = models.ImageField()
    featured = models.BooleanField()
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class watch_category(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    bg = models.FileField()
    icon = models.FileField()

class Carousel(models.Model):
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=1000)
    bg = models.FileField()


class Member(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, verbose_name="會員類型", choices=(('commercial', '錶行'),('personal', "個人")))