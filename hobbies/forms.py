from django import forms
from .models import Hobby

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['title', 'content', 'hobby_image']