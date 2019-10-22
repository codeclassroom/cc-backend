from django import forms

from .models import Response


class ResponseForm(forms.ModelForm):
    '''Form to accept Responses to Questions.'''

    class Meta:
        model = Response
        fields = ('submission',)
