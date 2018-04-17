from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from django.http import HttpResponse, HttpResponseRedirect

from .models import Question, Choice, Votes

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, authenticate,logout

from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm

from django.contrib.auth.models import User

from django.urls import reverse

def home(request):
    if request.user.is_authenticated:
        return redirect('polls:dashboard')
    
    return render(request, 'polls/home.html')

def log_in(request):
    if request.user.is_authenticated:
        return redirect('polls:dashboard')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('polls:dashboard')
            else:
                return render(request,'polls/login.html',{'form' : form,'user' : user})
    else:
        form = UserLoginForm
    context = { 'form' : form }
    return render(request,'polls/login.html', context)


def log_out(request):
    logout(request)
    return redirect('polls:home')



def register(request):
    if request.user.is_authenticated:
        return redirect('polls:dashboard')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('polls:dashboard')
    else:
        form = UserCreationForm()

    context = { 'form' : form }
    return render(request, 'polls/register.html', context)

@login_required(login_url='/login')
def dashboard(request):
    username = request.user
    latest_question_list = Question.objects.exclude(username = username)
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/dashboard.html',context)

def vote(request,question_id):
    username = request.user
    latest_question_list = Question.objects.exclude(username = username)
    question = get_object_or_404(Question, pk=question_id)
    try:
        voted_question = Votes.objects.get(username = username,question_text = question)
    except Votes.DoesNotExist:
        voted_question = None
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/dashboard.html', {
            'latest_question_list': latest_question_list,
            'error_message': "You didn't select a choice.",
        })
    else:
        if voted_question == None: 
            selected_choice.votes += 1
            selected_choice.save()
            u = Votes(username = username,question_text = question)
            u.save()
            return render(request, 'polls/vote.html',{'choice' : selected_choice})
        else:
            return render(request, 'polls/dashboard.html', {
                'latest_question_list': latest_question_list,
                'error_message': "You cant vote twice",
                })

def mypolls(request):
    username = request.user
    latest_question_list = Question.objects.filter(username = username)
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/mypolls.html',context)