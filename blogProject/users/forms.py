from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms
class updateuserprofile(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']


class updateuserform(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username",'email']

    def __init__(self, *args: any, **kwargs: any) -> None:
        super(updateuserform,self).__init__(*args, **kwargs)
        for field in ['username','email']:
            self.fields[field].help_text=None
    