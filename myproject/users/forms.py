from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, CandidateProfile, RecruiterProfile

class CandidateSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_candidate = True
        if commit:
            user.save()
            CandidateProfile.objects.create(user=user)
        return user

class RecruiterSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_recruiter = True
        if commit:
            user.save()
            RecruiterProfile.objects.create(user=user)
        return user
    
    