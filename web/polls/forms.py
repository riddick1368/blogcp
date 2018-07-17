from django import forms
from .models import Poll,Choice


class Form_poll(forms.ModelForm):


    class Meta:
        model = Poll

        fields = [
            "text"
        ]


class Form_choice(forms.ModelForm):

    class Meta:
        model = Choice

        fields =[
            "answer"
        ]