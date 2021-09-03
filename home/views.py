from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import RegisterForm
# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

def contact(request):
    return render(request,'pages/contact.html')

def error(request, exception):
    exception = 'Đường dẫn không tồn tại!'
    return render(request, 'pages/error.html', {'message': exception})

def user_register(request):
    template = 'pages/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # kiểm tra hợp lệ kh
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists!'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': "Email already exists!"
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not math!'
                })
            else:
                #create the user
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.save()
                return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, template, {'form': form})


