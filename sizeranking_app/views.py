from django.shortcuts import render, redirect
from django.contrib.auth.models import User #ユーザテーブル
from django.db import IntegrityError #ユーザ名の重複エラー
from django.contrib.auth import authenticate, login, logout  #ユーザ認証, ログイン, ログアウト
from django.urls import reverse_lazy #登録後の遷移先指定
from django.contrib.auth.decorators import login_required #ログイン必須
from .models import RankingModel #ランキングモデル
from .forms import registerForm #登録フォーム




###ユーザ登録###
def signupview(request):
    if request.method == "POST":
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            User.objects.create_user(username_data, '', password_data)#新しくユーザ作成
        except IntegrityError:
            return render(request, 'signup.html', {'error' : 'このユーザ名は既に登録されています。'})
    else:
        return render(request, 'signup.html', {})
    return render(request, 'login.html', {})

###ログイン###
def loginview(request):
    if request.method == "POST":
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None: #userがNoneでなければ
            login(request, user)
            return redirect('show') #ランキングページへリダイレクト
        else:
            return redirect('login')
    return render(request, 'login.html')


###ログアウト###
@login_required
def logoutview(request):
    logout(request)
    return redirect('login')

###ランキング表示画面(テーブル二つ並べて実装)###
@login_required
def showview(request):
    object_list = RankingModel.objects.all() #ランキングモデルのテーブル全て取得
    ranking = range(1, len(object_list)+1)
    params = {
        'object_list' : object_list,
        'ranking_list' : ranking,
    }
    return render(request, 'show.html', params) #{}内の左がhtmlでの変数名：右が中身



###ランキング登録画面###
@login_required
def registerview(request):
    if request.method == 'POST':
        try:
            obj = RankingModel()
            ranking = registerForm(request.POST, instance=obj)
            ranking.save()
            return redirect(to='/show')
        except ValueError:
            return render(request, 'register.html', {'error' : '不正な入力がされました'})
    params = {
        'form': registerForm(),
    }
    return render(request, 'register.html', params)