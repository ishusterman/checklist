from django import forms
from django.forms import Textarea, DateInput
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django.forms.models import inlineformset_factory, modelformset_factory

from django.forms import ModelForm
from db_checklist.models import *

class ChecklistForm(ModelForm):
    class Meta:
        model = CheckList
        #fields = '__all__'
        exclude = ('implant','equip','resorption_mat', 'no_resorption_mat',)
        widgets = {
            'date': AdminDateWidget(),
            'time': AdminTimeWidget(),
        }

fs1 = inlineformset_factory(CheckList, implant_detail, fields=('__all__'), extra=2)
fs2 = inlineformset_factory(CheckList, equip_detail, fields=('__all__'), extra=2)
fs3 = inlineformset_factory(CheckList, resorption_mat_count, fields=('__all__'), extra=2)
fs4 = inlineformset_factory(CheckList, no_resorption_mat_count, fields=('__all__'), extra=2)

