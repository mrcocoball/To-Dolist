from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["social"]

    def signup(self, request, user):
        user.social = self.cleaned_data["social"]
        user.save()