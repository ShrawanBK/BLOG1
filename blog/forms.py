from django import forms

class StoryForm(forms.Form):
    your_name = forms.CharField(label='Enter Story', max_length=100)