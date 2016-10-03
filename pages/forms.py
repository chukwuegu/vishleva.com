from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxLengthValidator


class ContactForm(forms.Form):
    """
    Contact form
    """
    name = forms.CharField(label=_('name'), validators=[MaxLengthValidator(500)],
                           widget=forms.TextInput(attrs={'placeholder': _('your name')}))
    contacts = forms.CharField(label=_('contacts'), validators=[MaxLengthValidator(500)],
                               widget=forms.TextInput(attrs={'placeholder': _('phone or email')}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('message')}),
                              validators=[MaxLengthValidator(4000)], label=_('message'))
