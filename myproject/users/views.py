from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CandidateSignUpForm, RecruiterSignUpForm
# from . import views

def signup(request):
    if request.method == 'POST':
        form = CandidateSignUpForm(request.POST) if 'candidate' in request.POST else RecruiterSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request,'welcome.html')
    else:
        candidate_form = CandidateSignUpForm()
        recruiter_form = RecruiterSignUpForm()
        return render(request, 'signup.html', {'candidate_form': candidate_form, 'recruiter_form': recruiter_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'profile.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')