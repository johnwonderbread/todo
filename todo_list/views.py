from django.shortcuts import render

def home(request): 
    return render(request, 'home.html', {})

def about(request):
	context = {'first_name': 'John', 'last_name': 'Tyler'}
	return render(request, 'about.html', context)