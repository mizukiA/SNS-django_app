from django import forms
from .models import Friend
from .models import Friend, Message

class FriendForm(forms.ModelForm):
  class Meta:
    model = Friend
    fields = ['name', 'mail', 'gender', 'age', 'birthday']

class FindForm(forms.Form):
    find = forms.CharField(label = 'Find', required = False)

class CheckForm(forms.Form):
    str = forms.CharField(label = 'Name')

class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ['title', 'content', 'friend']
