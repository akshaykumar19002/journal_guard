from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *
from .token import user_tokenizer_generate
from journal.utils import *


class Register(View):
    
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'user/registration/register.html', {'form': form})
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'User Verification Email'
            message = render_to_string('user/registration/email-verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': user_tokenizer_generate.make_token(user),
            })
            user.email_user(mail_subject, message)

            return redirect('email-verification-sent')
        return render(request, 'user/registration/register.html', {'form': form})
        

class Login(View):
    
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                next_url = request.GET.get('next', reverse('dashboard:home'))
                return HttpResponseRedirect(next_url)
        return render(request, 'user/login.html', {'form': form})


def email_verification(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)

    if user is not None and user_tokenizer_generate.check_token(user, token):
        user.is_active = True
        user.hash_salt = generate_hash()
        user.encryption_required = True
        user.save()
        return redirect('email-verification-success')
    else:
        return redirect('email-verification-failed')


def email_verification_sent(request):
    return render(request, 'user/registration/email-verification-sent.html')


def email_verification_success(request):
    return render(request, 'user/registration/email-verification-success.html')


def email_verification_failed(request):
    return render(request, 'user/registration/email-verification-failed.html')


def user_logout(request):
    try:
        for key in list(request.session.keys()):
            if key == 'session_key':
                continue
            del request.session[key]
    except KeyError:
        pass
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


def registration_options(request):
    return render(request, 'user/registration/registration-options.html')
