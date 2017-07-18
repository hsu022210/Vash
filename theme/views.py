from django.shortcuts import redirect, render_to_response, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from theme.models import UserCreateForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreateForm()
    return render_to_response('registration/register.html', locals())


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
