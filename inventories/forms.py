from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm

from inventories.models import Inventory


class InventoryForm(forms.ModelForm):
    # confirm_email = forms.EmailField(
    #     label="Confirm email",
    #     required=True,
    # )

    class Meta:
        model = Inventory
        fields = ('resume', 'date')

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)


class UserForm(UserCreationForm):
	pass