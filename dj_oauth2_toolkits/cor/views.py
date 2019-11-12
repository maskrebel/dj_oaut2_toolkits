from django.contrib.auth import logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

def index(request):
    return HttpResponse('<a href="/login">Login</a>')


def login_view(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                # try:
                #     akun = Akun.objects.get(akun=user.id)
                #     login(request, user)
                #
                #     request.session['karyawan_id'] = akun.karyawan.id
                #     request.session['jenis_akun'] = akun.jenis_akun
                #     request.session['username'] = request.POST['username']
                # except:
                #     messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data karyawan, silahkan hubungi administrator')
                return redirect('/dashboard')
            else:
                messages.add_message(request, messages.INFO, 'User belum terverifikasi')
        else:
            messages.add_message(request, messages.INFO, 'Username atau password Anda salah')

    return render(request, 'login.html')


def login_action(request):
    username = request.POST['username']
    password = request.POST['password']
    request.session= username
    user = authenticate(username=username, password=password)
    if user is not None:
        return redirect(request,'../')
    else:
        return HttpResponse('hdjkshdjkhs')

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):

    response = render(request, 'dashboard.html')
    return response

def logout_view(request):
    logout(request)
    return redirect('../')