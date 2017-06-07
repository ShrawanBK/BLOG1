from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import StoryForm
# Create your views here.
def index(request):
	return render(request, 'index.html',{})


def get_story(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StoryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StoryForm()

    return render(request, 'story.html', {'form': form})