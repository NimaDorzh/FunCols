from django import forms
from .models import User


# creating a form
class FunsForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = User

        # specify fields to be used
        fields = [
            "name",
            "lastname",
            "email",
            "phone_number",
            "role_level",
            "user_link"
        ]