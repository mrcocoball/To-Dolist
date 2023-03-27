from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount

def index(request):
    print(request.user)
    return render(request, 'index.html')

@login_required
def withdrawl(request):

    if request.method == 'GET': 
        return render(request, 'account/withdrawl.html')
    
    if request.method == 'POST':
        user = User.objects.get(username = request.user.username)
        is_social = user.social

        if is_social:
            SocialAccount.delete(user) # allAuth의 SocialAccount 로 유저 삭제 (소셜 계정 / 일반 계정 정보 동시 삭제)
            return HttpResponseRedirect("/")
        else:
            user.delete()
            return HttpResponseRedirect("/")