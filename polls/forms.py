from django import forms
import datetime

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PollForm(forms.Form):
    question_text = forms.CharField(max_length =200)
    pub_date = forms.DateTimeField(initial=datetime.datetime.now())

class PollChoiceForm(forms.Form):
    choice_text = forms.CharField(max_length=200)
