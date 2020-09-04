from django import forms
from .models import *

class SchoolForm(forms.ModelForm):
	name = forms.CharField(
		label = 'name',
		widget = forms.TextInput(
			attrs={
				'placeholder' : 'schoolname',
				'class' : 'form-control'


				}

			))

	class Meta:

		model = School
		fields = '__all__'


class ClasseForm(forms.ModelForm):
	school = forms.ModelChoiceField(
		label = 'School',
		queryset = School.objects.all(),
		widget = forms.Select(
			attrs={
				
				'class' : 'form-control',

				}

			))
	name = forms.CharField(
		label = 'ClasseName',
		widget = forms.TextInput(
			attrs = {
				'placeholder' : 'Saisir votre School',
				'class' : 'form-control'

				}
			)
		)

	class Meta:

		model = Classe
		fields = '__all__'
																		
class RegisterStudentForm(forms.ModelForm):
	
	nom = forms.CharField(
		label = 'Nom',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre nom',
				'class':'form-control'
				}
			)

		)
	prenom = forms.CharField(
		label = 'Prenom',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre prenom',
				'class':'form-control'
				}
			)

		)
	age = forms.IntegerField(
		label = 'Age',
		widget = forms.NumberInput(
			attrs ={ 
				'placeholder':'Votre Age',
				'class':'form-control'
				}
			)

		)
	classe = forms.ModelChoiceField(
		label = 'Classe',
		queryset = Classe.objects.all(),
		widget = forms.Select(
			attrs = {
				'placeholder' : 'Saisir votre classe',
				'class' : 'form-control'

				}
			)
		)

	pictures = forms.ImageField(
		label = 'Pictures',
		widget = forms.FileInput(
			attrs ={ 
				'placeholder':'Votre Picture',
				'class':'form-control'
				}
			)

		)
	
	class Meta:
		model = RegisterStudent
		fields = '__all__'

class profileForm(forms.Form):
	
	username = forms.CharField(
		label = 'Username',
		widget = forms.TextInput(
			attrs = {
				'placeholder':'username',
				'class':'form-control'


				}


			)
		)
	password = forms.CharField(
		label = 'Password',
		widget = forms.PasswordInput(
			attrs ={ 
				'placeholder':'password',
				'type':'password',
				'class':'form-control'
				}
			)

		)
	password1 = forms.CharField(
		label = 'Password1',
		widget = forms.PasswordInput(
			attrs ={ 
				'placeholder':'password1',
				'type':'password',
				'class':'form-control'
				}
			)

		)
	nom = forms.CharField(
		label = 'Nom',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre nom',
				'class':'form-control'
				}
			)

		)
	prenom = forms.CharField(
		label = 'Prenom',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre prenom',
				'class':'form-control'
				}
			)

		)
	age = forms.IntegerField(
		label = 'Age',
		widget = forms.NumberInput(
			attrs ={ 
				'placeholder':'Votre Age',
				'class':'form-control'
				}
			)

		)
	matricule = forms.CharField(
		label = 'Matricule',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre Matricule',
				'class':'form-control'
				}
			)

		)
	pictures = forms.CharField(
		label = 'Pictures',
		widget = forms.FileInput(
			attrs ={ 
				'placeholder':'Votre Picture',
				'class':'form-control'
				}
			)

		)
class ConnexionForm(forms.Form):
	username = forms.CharField(
		label = 'Username',
		widget=forms.TextInput(
			attrs={
				'placeholder':'username',
				'type':'username',
				'class':'form-control'
			}

		))

	password = forms.CharField(
		label = 'Password',
		widget = forms.PasswordInput(
			attrs ={ 
				'placeholder':'password',
				'type':'password',
				'class':'form-control'
				}
			)

		)

	


