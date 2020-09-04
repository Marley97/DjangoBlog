from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required(login_url='login')
def index(request):
	text = "Bonjour le monde"
	text2 = "Aymar"
	nummber = 42510

	return render(request, "index.html", locals())

def profile(request):
	text = "Mon Profil"

	return render(request, "profil.html", locals())

def registerSchool(request):
	school_form = SchoolForm(request.POST or None)
	if(request.method == 'POST'):
		if(school_form.is_valid()):
			school_form.save()
	school_form = SchoolForm()

	return render(request, "forms.html", locals())


def registerClass(request):
	classe_form = ClasseForm(request.POST or None)
	if(request.method == 'POST'):
		if(classe_form.is_valid()):
			classe_form.save()
	classe_form = ClasseForm()
	return render(request, "forms.html", locals())


def register(request):

	register_form = RegisterStudentForm(request.POST or None,request.FILES)

	if(request.method == 'POST'):

		if(register_form.is_valid()):
			register_form.save()
	register_form = RegisterStudentForm()
	return render(request, "forms.html", locals())


def ListStudent(request):
	students = RegisterStudent.objects.all()

	return render(request, "lists.html", locals())
def modifier(request,student_id):
	student = RegisterStudent.objects.get(id=student_id)
	modifier_form = RegisterStudentForm(request.POST or None,request.FILES,instance = student)
	if(request.method == 'POST'):

		if(modifier_form.is_valid()):
			modifier_form.save()
			return redirect(ListStudent)
	modifier_form = RegisterStudentForm(instance=student)
	return render(request, "forms.html", locals())
def delete(request,student_id):
	student = RegisterStudent.objects.get(id=student_id)
	student.delete()
	return redirect(ListStudent)

def registerProfile(request):
	profile_form = profileForm(request.POST or None,request.FILES)
	if(request.method == 'POST'):
		if(profile_form.is_valid()):
			username=profile_form.cleaned_data['username']
			password=profile_form.cleaned_data['password'] 
			password1=profile_form.cleaned_data['password1']
			nom=profile_form.cleaned_data['nom']
			prenom=profile_form.cleaned_data['prenom']
			age=profile_form.cleaned_data['age']
			matricule=profile_form.cleaned_data['matricule']
			pictures=profile_form.cleaned_data['pictures']
			
			if(password == password1):
				user = User.objects.create_user(username = username,password = password)
				user.first_name = nom
				user.last_name = prenom
				user.save()

				profile=Profile(user = user ,age = age ,matricule = matricule,pictures = pictures).save()
				if user:
					login(request,user)
					return redirect(index)
				else:
					return redirect(connexion)
			else:
				profil_form =profileForm(request.FILES)
	profil_form = profileForm(request.FILES)
	return render(request,'forms.html',locals())

def connexion(request):
	connexion = ConnexionForm(request.POST)
	if(request.method == 'POST'):
		if(connexion.is_valid()):
			username=connexion.cleaned_data['username']
			password=connexion.cleaned_data['password']

			user=authenticate(username = username,password = password)
			if user:
				login(request,user)
				return redirect(index)
			else:
				connexion = ConnexionForm()
	connexion = ConnexionForm()
	return render(request,'forms.html',locals())

def deconnexion(request):
	logout(request)
	return redirect(connexion)
	

