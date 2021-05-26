from django import forms
from django.forms import fields
from .models import List


class ListForm(forms.ModelForm):
    """
    >Creating forms to submit our task list
    >Process:
        1. creating Meta class to give iputes to the system generated forms
        2. set the value of model
        3. set the which fields of out table we want to display in the form

    """

    class Meta:
        model = List
        fields = ['item', 'completed']
