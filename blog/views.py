from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import StoryForm
# Create your views here.
def result(request):
	return render(request, 'result.html',{})


def get_story(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request.POST.get("title"))
        # create a form instance and populate it with data from the request:
        form = StoryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        	tit = form.cleaned_data['body']
        	ttt = tit[::-1]
        	print(ttt)
        	return render(request,'result.html',{'tit': tit})

            # process the data in form.cleaned_data as required
            # ...
           
            #return HttpResponseRedirect(reverse('story',kwargs={'post_id': post.id}))


    # if a GET (or any other method) we'll create a blank form
    else:
    	form = StoryForm()

    return render(request, 'story.html',{'form': form}) 