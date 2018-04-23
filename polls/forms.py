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

class SurveyForm(forms.Form):
    question = forms.CharField(widget=forms.TextInput(attrs={'required' : 'required'}),max_length =200)
    answer = forms.CharField(widget=forms.Textarea(),required=False)

class SurveyResponseForm(forms.Form):
    question = forms.CharField(widget=forms.TextInput(attrs={'required' : 'required','readonly' : 'readonly'}),max_length =200)
    answer = forms.CharField(widget=forms.Textarea(attrs={'required' : 'required'}))