from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.views import View
from stores.models import RetailStores, Employees
from .forms import SignupForm, UpdateProfileForm
from .models import User


def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user_account = auth.authenticate(email=username, password=password)

            if user_account is not None:
                if user_account.is_businessaccount is False:
                    auth.login(request, user_account)
                
                else:
                    try:
                        store = RetailStores.objects.get(name=user_account)

                        if user_account.is_businessaccount is True and store is not None:
                            auth.login(request, user_account)
                            return redirect('dashboard', user_account.username)                                                                   
                    
                    except RetailStores.DoesNotExist:
                        auth.login(request, user_account)
                        return redirect('registration')
                        
    context = {'LoginForm': form}
    return render(request, 'accounts/login.html', context)


def signup_view(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()

            messages.success(request, 'User account successfully created!')
            return redirect('profile', new_user.username)
    
    context = {'SignupForm': form}
    return render(request, 'accounts/signup.html', context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False)
class UpdateProfileView(View):
    def get(self, request, user):
        user_obj = User.objects.get(username=user)
        form = UpdateProfileForm(request.POST, instance=user_obj)

        context = {'UpdateProfileForm': form}
        return render(request, 'accounts/profile.html', context)
    
    def post(self, request, user):
        user_obj = User.objects.get(username=user)
        form = UpdateProfileForm(instance=user_obj)

        if form.is_valid():
            form.save()

            messages.success(request, 'Profile successfully updated!')
        return redirect('profile', user)

class LogoutUsersView(LogoutView):
    template_name = 'accounts/logout.html'