from email.policy import default
from random import choices
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from app.models import TarjetaCredito


# Create your forms here.
class FormularioTajerta(forms.Form):
	model = TarjetaCredito
	TIPOS_TARJETA = (
		('MasterCard', 'Mastercard'),
		('VISA', 'VISA'),
	)
	tarjeta_credito = forms.ChoiceField(required=True, choices=TIPOS_TARJETA)
	num_tarjeta = forms.CharField(required=True)
	fecha_caducidad = forms.CharField(required=True)
	codigo_seguridad = forms.CharField(required=True, max_length=3)



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user