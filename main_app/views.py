from django.shortcuts import render, redirect
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})


def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    # instantiate FeedingForm to be rendered within the detail.html
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form
    })


def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)
    # check if the form is valid
    if form.is_valid():
        # does not commit it yet to the database
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id  # first cat_id came from the foreign key
        new_feeding.save()
    return redirect('detail', cat_id=cat_id)


class CatCreate(CreateView):
    model = Cat
    fields = '__all__'


class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']


class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'
