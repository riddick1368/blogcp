from django import forms
from .models import Post


class Form_post(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            "title",
            "subject",
            "content",
        ]