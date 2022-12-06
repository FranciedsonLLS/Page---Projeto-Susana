from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required


from django.urls import reverse_lazy





from customauth.models import MyUser
from customauth.forms import UserChangeForm
# Create your views here.

def Equipe(request):
    return render(request, "nossotime.html")
    


def index (request):
    return render(request,'index.html')


@login_required(login_url='auth.login')
def edit_profile(request, pk):
    user = MyUser.objects.get(pk=pk)
    if user.id == request.user.id:
        form = UserChangeForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        return render(request, 'edit_profile.html', {'form': form})
    return redirect('index')
    
        
