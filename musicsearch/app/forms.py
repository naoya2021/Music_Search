from django import forms
from django.contrib.auth.forms import AuthenticationForm 


class SearchForm(forms.Form):
    title = forms.CharField(label='タイトル',max_length=200,required=True)



# class LoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'
#             field.widget.attrs['placeholder'] = field.label   