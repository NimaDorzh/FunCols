from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# creating a form
class FunsForm(forms.ModelForm):
    email = forms.EmailField()
    # create meta class
    class Meta:
        # specify model to be used
        model = User

        # specify fields to be used
        fields = [
            "username",
            "email",
            "password",
           # "name",
            #"lastname",
            #"phone_number",
            #"role",
            #"user_link"
        ]

# Форма регистрации
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
# Форма аутентификации (built-in Django)
class UserLoginForm(AuthenticationForm):
    pass

