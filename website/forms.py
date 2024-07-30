from django import forms
from website.models import Contact

class Nameform(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    massage = forms.CharField(widget=forms.Textarea)
     
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
