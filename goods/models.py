from django.db import models
from accounts.models import User


class Goods(models.Model):
    name = models.CharField(max_length=40)
    size = models.CharField(max_length=20)
    category = models.CharField(max_length=20, blank=True)
    bo_prize = models.IntegerField(max_length=20, blank=True, help_text="보증금")
    lent_prize = models.IntegerField(max_length=20, blank=True, help_text="")
    image = models.ImageField(upload_to='goods_image',
                              default="goods_image/default.png")
    intro = models.TextField()
    about = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name='goods', null=True)
    lenter = models.ForeignKey(User, related_name='lent_goods', null=True)

    def __str__(self):
        return '%s' % self.name
