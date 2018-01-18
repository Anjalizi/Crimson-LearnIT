from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import contactpage, skintype, undertone
from .forms import NewTopicForm

def home(request):
	stypes = skintype.objects.all()
	return render(request, 'home.html', {'stypes': stypes})

def about(request):
	return render(request, 'about.html')

def contact(request):
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = NewTopicForm()
	return render(request, 'contact.html', {'form': form})

def choose_skintone(request):
	stypes = skintype.objects.all()
	return render(request, 'choose_skintone.html', {'stypes': stypes})

def choose_undertone(request):
	utypes = undertone.objects.all()
	return render(request, 'choose_undertone.html', {'utypes': utypes})
