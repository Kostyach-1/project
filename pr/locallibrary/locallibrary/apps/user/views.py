from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from user.models import user
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from user.forms import create_user_form


def home_page(request):
    user_i = user.objects.all()
    return render(request, 'users/list.html', {'user_i' : user_i})




def user_page(request, user_id):
    try:
        a = user.objects.get( id = user_id )
    except:
        raise Http404("Пользователь не найден!")
    return render(request, 'users/user_page.html', {'user': a})

def create_user(requset):
    if requset.method == "POST":
        form = create_user_form(requset.POST)

        if form.is_valid():
            form.save()
            return redirect('/success/')
        return render(requset, 'users/create_user.html', {'form': form})
    else:
        form = create_user_form()
        return render(requset, 'users/create_user.html', {'form': form})


class SearchResultsView(ListView):
    model = user
    template_name = 'users/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = user.objects.filter(
            Q(job_title=query)
        )
        return object_list
'''
def SearchResultsView(self, request):
    query = self.request.GET.get('q')
    object_list = user.objects.filter(
            Q(job_title=query)
        )
    return render(request, 'users/search_results.html', {'object_list': object_list})
'''
