import hashlib

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from .models import CustomUser, Messages


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, label="Pseudo", required=True)
    email = forms.EmailField(label="Adresse e-mail", required=True)
    profile_picture = forms.ImageField(label="Photo de profil", required=True)

    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"})
    )
    password2 = forms.CharField(
        label="Confirmation du mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"})
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "profile_picture", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet e-mail est déjà utilisé.")
        return email
    

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['message']
        widgets = {
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Ecrivez un message.',
                    'class': 'mess_input'
                }
            ),
        }