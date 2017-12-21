from django import forms
from .models import contactpage

class NewTopicForm(forms.ModelForm):
    suggestion = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3, 'placeholder': 'Any suggestions?'}
        ),
        max_length=200,
        help_text='The maximum length of this text can be 200 characters.'
    )

    class Meta:
        model = contactpage
        fields = ['created_by','phone', 'suggestion']

