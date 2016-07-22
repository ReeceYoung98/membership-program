from django.http import Http404
from django.shortcuts import render
from .models import User, UserDetail

def index(request):
	return render(request, 'members/login.html')

def allusers(request):
	all_users = User.objects.all()
	return render(request, 'members/users.html', {'all_users': all_users})

def profile(request, user_id):
	try:
		retrieved_user = User.objects.get(id=user_id)
		retrieved_user_profile = UserDetail.objects.get(id=retrieved_user.id)
		context = {'retrieved_user': retrieved_user, 'retrieved_user_profile': retrieved_user_profile,}
	except User.DoesNotExist:
		raise Http404('User does not exist')
	return render(request, 'members/users.html', context)