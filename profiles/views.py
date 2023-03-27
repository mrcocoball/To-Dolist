from django.shortcuts import render
from django.http import HttpResponseRedirect
from accounts.models import User

def main(request):

    # 인증 여부 체크
    if request.user.is_authenticated:
    
        profile = User.objects.get(username = request.user.username)
        data = {'profile' : profile}

        return render(request, 'profile.html', data)
    else:
        # 로그인 페이지로 리다이렉션
        return HttpResponseRedirect('../accounts/login')

def detail(request, pk):

    profile = User.objects.get(id = pk)
    data = {'profile' : profile}

    return render(request, 'profile_share.html', data)
