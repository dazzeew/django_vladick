from django.http import HttpResponse, Http404

# from .forms import LoginForm, UserRegistrationForm
from django.shortcuts import render

def home(request):
	return render(request, 'risk/home.html')
	
# def register(request):
# 	if request.method == 'POST':
# 		user_form = UserRegistrationForm(request.POST)
# 		if user_form.is_valid():
# 			new_user = user_form.save(commit=False)
# 			new_user.set_password(user_form.cleaned_data['password'])
# 			new_user.save()
# 			return render(request, 'account/register_done.html', {'new_user': new_user})
# 	else:
# 		user_form = UserRegistrationForm()
# 	return render(request, 'account/register.html', {'user_form': user_form})
