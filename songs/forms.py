from django import forms
from .models import *
# from captcha.fields import CaptchaField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class SongForm(forms.Form):

    vote = forms.IntegerField(label='vote1')
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'class': 'form-control', 'style': 'width:300px'}),
                             label='')
    # class Meta:
    #     model = Song
    #     fields = ['vote']

