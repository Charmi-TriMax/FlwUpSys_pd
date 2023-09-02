from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm, ResetPasswordForm
from .models import UserLogin, Staff, CustomUser
from django.contrib.auth import get_user_model
from accounts.models import Staff  # Update with your actual model import
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from datetime import datetime


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                if user.is_superuser:  # Check if the user is a superuser
                    login(request, user)
                    # Redirect superusers to admin dashboard
                    return redirect('/')
                elif user.staff.ForceReset:  # Check if the user needs to reset the password
                    # Redirect users to reset password page
                    return redirect('/accounts/reset_password/')
                else:
                    login(request, user)
                    return redirect('/')  # Redirect users to their dashboard

    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_new_password = form.cleaned_data['confirm_new_password']

            if new_password == confirm_new_password:
                # Assuming the user is identified by email
                # Replace 'user_email' with your identifier
                username = request.POST.get('username')
                # Replace 'User' with your actual User model
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = None

                if user and check_password(old_password, user.password):
                    print("Old password matched")
                    user.set_password(new_password)
                    user.save()
                    # Redirect to login page
                    return redirect('/accounts/login/')
                else:
                    print("Invalid user or incorrect old password")
                    form.add_error(
                        'old_password', 'Invalid user or incorrect old password')
            else:
                # Handle mismatched new passwords
                form.add_error('confirm_new_password',
                               'New passwords do not match')

    else:
        form = ResetPasswordForm()

    context = {'form': form}
    return render(request, 'accounts/reset_password.html', context)

# def reset_password(request):
#     if request.method == 'POST':
#         form = ResetPasswordForm(request.POST)
#         if form.is_valid():
#             user_identifier = form.cleaned_data['user']  # Use the correct field name
#             old_password = form.cleaned_data['old_password']
#             reset_password = form.cleaned_data['reset_password']

#             try:
#                 staff_member = Staff.objects.get(user__username=user_identifier)  # Use the correct field for username
#             except Staff.DoesNotExist:
#                 staff_member = None

#             if staff_member and staff_member.user.check_password(old_password):  # Check password on User object
#                 staff_member.user.set_password(reset_password)  # Set password on User object
#                 staff_member.random_password = reset_password  # Update the random_password field if needed
#                 staff_member.save()

#                 staff_user = authenticate(username=user_identifier, password=reset_password)
#                 if staff_user is not None:
#                     login(request, staff_user)

#                 return redirect('/')
#             else:
#                 form.add_error('old_password', "Invalid old password.")
#     else:
#         form = ResetPasswordForm()

#     context = {'form': form}
#     return render(request, 'accounts/reset_password.html', context)


def registration(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            # Check if the username already exists
            if not get_user_model().objects.filter(username=username).exists():
                first_name = user_form.cleaned_data['first_name']
                last_name = user_form.cleaned_data['last_name']
                dob = user_form.cleaned_data['dob']
                user_type = user_form.cleaned_data['user_type']
                code = user_form.cleaned_data['code']
                Designation = user_form.cleaned_data['Designation']
                mobile = user_form.cleaned_data['mobile']
                Phone = user_form.cleaned_data['Phone']
                Other1 = user_form.cleaned_data['Other1']
                Other2 = user_form.cleaned_data['Other2']
                CrBy = user_form.cleaned_data['CrBy']
                CrFrom = user_form.cleaned_data['CrFrom']
                UpdBy = user_form.cleaned_data['UpdBy']
                UpdFrom = user_form.cleaned_data['UpdFrom']
                isActive = user_form.cleaned_data['isActive']
                ForceReset = user_form.cleaned_data['ForceReset']
                CrDtTm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                UpdDtTm = CrDtTm

                # Generate password based on dob (format: DDMM)
                dob_password = dob.strftime('%d%m%Y')
                user = get_user_model().objects.create_user(
                    username=username, password=dob_password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                user_profile = Staff.objects.create(
                    user=user,
                    dob=dob,
                    user_type=user_type,
                    code=code,
                    Designation=Designation,
                    mobile=mobile,
                    Phone=Phone,
                    Other1=Other1,
                    Other2=Other2,
                    CrBy=CrBy,
                    CrFrom=CrFrom,
                    UpdBy=UpdBy,
                    UpdFrom=UpdFrom,
                    isActive=isActive,
                    ForceReset=ForceReset,
                    UpdDtTm=UpdDtTm,
                    CrDtTm=CrDtTm,
                )

                # Redirect to home page or any desired URL
                # Get the referring URL or default to '/'
                return redirect('/')
            else:
                # Handle the case when the username already exists
                user_form.add_error('username', 'Username already exists')
    else:
        user_form = RegistrationForm()

    context = {'user_form': user_form}
    return render(request, 'accounts/registration.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
