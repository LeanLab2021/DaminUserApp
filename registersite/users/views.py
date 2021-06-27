from django.shortcuts import get_object_or_404, render, redirect

from .forms import UserForm
from .models import User


def new(request):
    context = {
        'form': None,
        'err_msg': ''
    }
    print('new called')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context['err_msg'] = '再入力してください'
            context['form'] = form
    else:
        context['form'] = UserForm()

    return render(request, 'users/new.html', context)


def index(request):
    users = User.objects.all()
    return render(request, 'users/index.html',
                  {
                      'users': users
                  })


def detail(request, pk):
    return render(request, 'users/detail.html', {
        'user': get_object_or_404(User, pk=pk)
    })


def delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('index')
