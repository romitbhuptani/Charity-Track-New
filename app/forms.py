from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Donor,Volunteer,Donation,DonationArea
from django.contrib.auth import password_validation
class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password again'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email','password1','password2']
        
        widgets = {'first_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First name'}),'last_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last name'}),'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),'email' : forms.TextInput(attrs={'class':'form-control','placeholder':'Email ID'})}

class DonorSignupForm(forms.ModelForm):
    userpic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = Donor
        fields = ['contact','userpic','address']
        widgets = {'contact': forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact Number'}),'address': forms.Textarea(attrs={'class':'form-control','placeholder':'Address'})}
        
class VolunteerSignupForm(forms.ModelForm):
    userpic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    idpic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model =  Volunteer
        fields = ['contact','userpic','idpic','address','aboutme']
        widgets = {'contact': forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact Number'}),'address': forms.Textarea(attrs={'class':'form-control','rows':4,'placeholder':'Address'}),
        'aboutme' : forms.Textarea(attrs={'class':'form-control','rows':4,'placeholder':'About Yourself'}), }

class LoginForm(AuthenticationForm):
    username = UsernameField(required=True,widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control','placeholder':'Username'}))
    password =forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password' , strip=False,widget=forms.PasswordInput(attrs={'auto-complete':'current-password','auto-focus':True,'class':'form-control','placeholder':'Old password'}))
    new_password1 = forms.CharField(label='New Password' ,strip=False, widget=forms.PasswordInput(attrs={'auto-complete':'new-password','class':'form-control','placeholder':'New password'}))
    new_password2 = forms.CharField(label='Confirm New Password' ,strip=False, widget=forms.PasswordInput(attrs={'auto-complete':'new-password','class':'form-control','placeholder':'Confirm password'}))
    
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email',max_length=254,widget=forms.EmailInput(attrs={'auto-complete':'email','class':'form-control'}))
    
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password ',strip=False,widget=forms.PasswordInput(attrs={'auto-complete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label='Confirm New Password ',strip=False,widget=forms.PasswordInput(attrs={'auto-complete':'new-password','class':'form-control'}))
    
Donation_Choices = (
    ('Food Donation','Food Donation'),
    ('Cloth Donation','Cloth Donation'),
    ('Footwear Donation','Footwear Donation'),
    ('Books Donation','Books Donation'),
    ('Furniture Donation','Furniture Donation'),
    ('Vessel Donation','Vessel Donation'),
    ('Other','Other'),
)

class DonateNowForm(forms.ModelForm):
    donationpic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = Donation
        fields = ['donationname','donationpic','collectionloc','description']
        widgets = {
            'donationname':forms.Select(choices=Donation_Choices,attrs={'class':'forn-control'}),
            'collectionloc':forms.TextInput(attrs={'class':'form-control','placeholder':'Donation Collection Address'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),   
        }
        labels = {
            'donationpic' : 'Donation Image (Pic of items you want to donate)',
            'donationname' : 'Donation name',
            'collectionloc' : "Donation Collection Addres"
        }

class DonationAreaForm(forms.ModelForm):
    class Meta:
        model = DonationArea
        fields = ['areaname','description']
        widgets = {
            'areaname' : forms.TextInput(attrs={'class':'form-control','placeholder':'Donation Area'}),
            'description' : forms.Textarea(attrs={'class':'form-control','placeholder':'Desciption'}),
        }
        
        labels = {
            "areaname" : "Donation Area Name",
            "description" : "Description"
        }