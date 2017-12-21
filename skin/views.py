from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import contactpage, skintype
from .forms import NewTopicForm

def home(request):
	stypes = skintype.objects.all()
	return render(request, 'home.html', {'stypes': stypes})

def about(request):
	return render(request, 'about.html')

def contact(request):
	user = User.objects.first()  # TODO: get the currently logged in user
	if request.method == 'POST':
		form = NewTopicForm(request.POST)

		if form.is_valid():
			cpage = contactpage.objects.create(
				suggestion=form.cleaned_data.get('message'),
				created_by=user
			)
			return redirect('home')  # TODO: redirect to the created topic page
	else:
		form = NewTopicForm()
	return render(request, 'contact.html', {'form': form})