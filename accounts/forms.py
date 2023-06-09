from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class SignupForm(UserCreationForm):
    """
        New users use this form to create an account.
    """
    SELECT_GENDER = (
        (None, '-- Select your gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mt-2 mb-2', 'autofocus': True}),
        label='Surname',
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'autofocus': True}),
        label='Other name',
        help_text='Enter your first name and middle name'
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'type': 'email', 'class': 'mb-2'}),
    )
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_GENDER,
    )
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date' , 'class': 'mb-2'}),
    )
    national_id = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mt-2 mb-2'}),
    )
    phone_no = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel'}),
        help_text='Enter your phone number without your country code'
    )
    is_businessaccount = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'mt-2'}),
        label="I'm creating a business account",
        required=False,
        help_text='<br><b>Uncheck the box if you are creating a personal account. If you are creating a business account then chack the box.</b>',
    )

    class Meta:
        model = User
        fields = [
            'last_name', 'first_name', 'username', 'email', 'gender', 'dob', 'phone_no',
            'national_id', 'password1', 'password2', 'is_businessaccount',
            ]

class UpdateProfileForm(forms.ModelForm):
    """ This form is used to edit and update a user's profile. """
    phone_no = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel'}),
        help_text='Enter your phone number without your country code'
    )
    country = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
    )

    class Meta:
        model = User
        fields = ['country', 'city', 'phone_no', 'profile_pic']

