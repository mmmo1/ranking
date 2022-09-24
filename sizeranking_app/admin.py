from django.contrib import admin
from .models import RankingModel  #ランキングに使用するモデル

# Register your models here.
admin.site.register(RankingModel) #管理者ページにモデルの登録