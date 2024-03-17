from django import forms
from django.urls import reverse_lazy

# from django.views.generic.edit import UpdateView

from .models import Person, Skills

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

    
class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = "__all__"
        exclude = ['person']