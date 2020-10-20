from django import forms 
from .models import ContactModel



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        exclude = ('Date',)
        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control','style':
            "width: 100%;padding-top: 10px;padding-bottom: 10px;background-color: var(--secondaryColor);border-radius: 5px;border: 1px solid var(--borderColor);font-size: 14px;}",'placeholder':"Tell Me What Is You'r Name ?"}),
            'Subject': forms.TextInput(attrs={'class':'form-control','style':
            "width: 100%;padding-top: 10px;padding-bottom: 10px;background-color: var(--secondaryColor);border-radius: 5px;border: 1px solid var(--borderColor);font-size: 14px;}",'placeholder':"Subject Is ?"}),
            'Email': forms.EmailInput(attrs={'class':'form-control','style':
            "width: 100%;padding-top: 10px;padding-bottom: 10px;background-color: var(--secondaryColor);border-radius: 5px;border: 1px solid var(--borderColor);font-size: 14px;}",'placeholder':"Example   -   name@example.com"}),
            'Message': forms.Textarea(attrs={'class':'form-control','style':
            "width: 100%;padding-top: 10px;padding-bottom: 10px;background-color: var(--secondaryColor);border-radius: 5px;border: 1px solid var(--borderColor);font-size: 14px;}",'placeholder':"Last Step..(Sorry) Message Is ?"}),
        }
