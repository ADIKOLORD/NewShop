from django import forms
from django.contrib.auth.models import User  # import model User


class UserRegisterForm(forms.ModelForm):
    '''
    class for Register User.
    '''

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password_confirmation = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        exclude = ('email.help_text',)
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_password_confirmation(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_confirmation']:
            raise forms.ValidationError('Password is not matching!')
        else:
            return cd['password_confirmation']


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
        exclude = ('password.help_text',)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'{username} is not defined')

        user = User.objects.get(username=username)
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Password is not correct')
            return self.cleaned_data
