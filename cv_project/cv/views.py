from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView, CreateView
from django.views.generic import DetailView, UpdateView

from .models import Person, Skills
from .forms import PersonForm, SkillsForm

from django import forms

from multi_form_view import MultiModelFormView



# Create your views here.
def index(request):
    return render(request, 'index.html')


def edit(request):
    return render(request, 'edit_view/index.html')

def home(request):

    persons = Person.objects.all()

    context = {
        'persons': persons,
    }

    return render(request, 'cv/home.html', context)

# def detail(request, person_id):
#     person = Person.objects.get(id=person_id)
#     skills = person.skills_set.all()

#     context = {
#         'person': person,
#         'skills': skills,
#     }

#     return render(request, 'cv/detail.html', context)


# class ContactFormView(FormView):
#     template_name = 'test_form.html'
#     form_class = ContactForm
#     success_url = '/thanks/'

#     def form_valid(self, form):
#         form.send_contact()
#         return super().form_valid(form)
    

class PersonCreateView(CreateView):
    model = Person
    fields = ['username', 'fullname', 'role', 'address', 'email', 'phone', 'website', 'github', 'linkedin', 'facebook']


class PersonUpdateView(UpdateView):
    template_name = 'cv/update.html'
    model = Person
    slug_field = 'id'
    slug_url_kwarg = 'id'
    fields = ['username', 'fullname', 'role', 'address', 'email', 'phone', 'website', 'github', 'linkedin', 'facebook']

class SkillUpdateView(UpdateView):
    template_name = 'cv/update.html'
    model = Skills
    slug_field = 'id'
    slug_url_kwarg = 'id'
    fields = ['person','skill', 'level']


class DataUpdateView(MultiModelFormView):
    slug_field = 'id'
    slug_url_kwarg = 'id'
    form_classes = {
        'person_form': PersonForm,
        'skills_form': SkillsForm,
    }
    template_name = 'cv/update.html'
    def get_success_url(self) -> str:
        return reverse('home')
    def forms_valid(self, forms) -> str:
        person = forms['person_form'].save()
        skill = forms['skills_form'].save(commit=False)
        skill.person = person
        skill.save()
        return super(DataUpdateView, self).forms_valid(forms)

class PersonDetailView(DetailView):
    template_name = 'cv/detail.html'
    model = Person
    slug_field = 'id'
    slug_url_kwarg = 'id'