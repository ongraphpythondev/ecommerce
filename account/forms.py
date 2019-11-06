from django import forms
from django.contrib.auth.forms import UserCreationForm


from account.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True)
    mobile =forms.CharField(max_length=10)
    # pincode = forms.IntegerField(max_value=7)

    class Meta:
        model=User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'mobile',
            # 'pincode'
        ]


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username =forms.CharField(max_length=20)
    password =forms.CharField(widget=forms.PasswordInput)

