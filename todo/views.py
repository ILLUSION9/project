from django.shortcuts import render
from .models import Zadacha


	
def index(request):
	todo_list = Zadacha.objects.all()
	context = {'todo_list' : todo_list}
	return render(request, 'todo/index.html', context)