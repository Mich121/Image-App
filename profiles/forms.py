from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import CustomUser

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=25,widget=forms.TextInput(attrs={"class":"form-control","id":"username"}))
    password = forms.CharField(max_length=25,widget=forms.PasswordInput(attrs={"class":"form-control","id":"password"}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = CustomUser.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This user does not exist.")
        return username

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user_qs = CustomUser.objects.filter(username__iexact=username)
        if user_qs.exists():
            user_a = user_qs.first()
            if not user_a.check_password(password):
                raise forms.ValidationError("Given password is not correct")
        return password