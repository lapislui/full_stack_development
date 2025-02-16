from django import forms

# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)

class FormName(forms.Form):
    
    Topic = forms.CharField(widget=forms.Textarea)
    Email = forms.EmailField(label='Enter your email')
    Vemail = forms.EmailField(label='Verify Email')
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        
        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")
