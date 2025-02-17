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
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        
        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")
    
class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
    
