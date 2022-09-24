from django.db import models
from django.contrib.auth.models import User #Userテーブルを参照するため
from django.core.validators import MaxValueValidator, MinValueValidator #最大値・最小値

# Create your models here.
class RankingModel(models.Model):
    #name = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    size = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(26)])
    ranking = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ('-size',)