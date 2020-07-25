from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from user.models import user


def home_page(request):
    user_i = user.objects.all()
    return render(request, 'users/list.html', {'user_i' : user_i})
def user_page(request, user_id):
    try:
        a = user.objects.get( id = user_id )
    except:
        raise Http404("Пользователь не найден!")
    return render(request, 'users/user_page.html', {'user': a})
def create_user():
    pass
