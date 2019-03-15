from django import forms

class contactForm(forms.Form):
    name = forms.CharField(required = False , max_length = 100, help_text = '100 characters maximum.')
    email = forms.EmailField(required = True)
    comment = forms.CharField(required = True, widget = forms.Textarea)