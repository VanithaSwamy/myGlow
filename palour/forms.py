from django import forms
from .models import userdetail,clientdetail,parlour,service
from django.contrib.auth.password_validation import validate_password

class user_registration(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password])
    class Meta:
        model = userdetail
        fields='__all__'
        widgets = {
        'confirmpassword':forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super(user_registration, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirmpassword')
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('Password does not match')

    
class client_reg(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password])
    status_choice=(
        ("pending","pending"),
        ("accepted","accepted"),
        ("rejected","rejected"),
    )
    status=forms.ChoiceField(choices=status_choice,disabled=True,required=False)
    class Meta:
        model = clientdetail
        fields ='__all__'
        widgets = {
        'confirm_password':forms.PasswordInput(),
        }
        labels={'regno':'registration no.'}
        
    def clean(self):
        cleaned_data = super(client_reg, self).clean()
        password = cleaned_data.get('password')
        confirmpassword = cleaned_data.get('confirm_password')
        if password and confirmpassword:
            if password != confirmpassword:
                raise forms.ValidationError('Password does not match')


class userloginform(forms.Form):
    username=forms.CharField(max_length=10)
    password=forms.CharField(widget=forms.PasswordInput())
    signup_choice=(
        ('user','user'),
        ('client','client'),
    )
    signup_as=forms.ChoiceField(choices=signup_choice)

class pardetails(forms.ModelForm):
    class Meta:
       model = parlour
       fields =['address','rating','description','parlour_image']
       widgets = {
            'description': forms.Textarea(attrs={'cols': 6, 'rows': 3}),
        }


class serv(forms.ModelForm):
    class Meta:
        model=service
        fields=['servicename','images','description','charges','discounted_charges']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 6, 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['servicename'].disabled = True

    # def clean_servicename(self):
    #         servicename = self.cleaned_data['servicename']
    #         existing_service = service.objects.filter(servicename=servicename)
    #         if existing_service.exists():
    #             raise forms.ValidationError("Already this service exists")
    #         return servicename
