from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'name',
                                           'placeholder': 'Your Name',
                                           'data-error': "Please enter your name", }),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'id': 'email',
                                             'placeholder': 'Your Email',
                                             'data-error': "Please enter your email", }),
            'comment': forms.Textarea(attrs={'class': 'form-control',
                                             'id': 'comment',
                                             'placeholder': 'Your Comment',
                                             'data-error': "Write your Comment", }),

        }