from django import forms

from main.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'name',
                                           'placeholder': 'Your Name',
                                           'data-error': "Please enter your name", }),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'id': 'email',
                                             'placeholder': 'Your Email',
                                             'data-error': "Please enter your email", }),
            'subject': forms.TextInput(attrs={'class': 'form-control',
                                              'id': 'subject',
                                              'placeholder': 'Your Subject',
                                              'data-error': "Please enter your subject", }),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'id': 'message',
                                             'placeholder': 'Your Message',
                                             'data-error': "Write your message", })

        }
