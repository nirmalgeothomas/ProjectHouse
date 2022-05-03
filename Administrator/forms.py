from django import forms
from django.forms import fields
from django.forms.widgets import TextInput, Widget
from .models import Postcomment

class PostCommentForm(forms.ModelForm):
    class Meta:
        model=Postcomment
        fields="__all__"
        Widget={'comment':TextInput(attrs={'class':'form-control'})}