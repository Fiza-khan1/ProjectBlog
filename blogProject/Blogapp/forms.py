from typing import Any
from django import forms
from .models import PostModel,comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class PostmodelForm(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model=PostModel
        fields=('title',  'content', )

class postUpdateForm(forms.ModelForm):
    class Meta:
        model=PostModel
        fields=('title',  'content', )


class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(signupform,self).__init__(*args, **kwargs)
        for field in ['username','email','password1','password2']:
            self.fields[field].help_text=None

class commentform(forms.ModelForm):
    content = forms.CharField(
    label='', 
    widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add Comments here'})
)
    class Meta:
        model=comments
        fields=['content']



