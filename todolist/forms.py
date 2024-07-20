from django import forms

from todolist.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs = {
            'placeholder': 'Digite o nome da task'
        }
