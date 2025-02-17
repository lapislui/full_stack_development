from django import forms
from django.core import validators
from first_app.models import User
# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)

class FormName(forms.Form):
    
    Topic = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(label='Enter your email')
    verify_email = forms.EmailField(label='Verify Email')
    Password = forms.CharField(widget=forms.PasswordInput)
    Verify_Password = forms.CharField(widget=forms.PasswordInput)

    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(
                                    0
                                )])
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        
        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")
    
class NewUserForm(forms.ModelForm):
    
    all_clean_data = super().clean()
    password = all_clean_data['password']
    verify_password = all_clean_data['verify_password']

    if password != verify_password:
        raise forms.ValidationError("Make sure passwords match!")
    
    class Meta():
        model = User
        fields = '__all__'
    
