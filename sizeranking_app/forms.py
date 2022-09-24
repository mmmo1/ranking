from django import forms
from .models import RankingModel
from django.core.validators import MaxValueValidator, MinValueValidator #最大値・最小値

class registerForm(forms.ModelForm):
    class Meta:
        model = RankingModel
        fields = ['name', 'size']