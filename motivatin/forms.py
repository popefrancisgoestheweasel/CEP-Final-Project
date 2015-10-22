from motivatin.models import Task, Tag
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude  = ('user', 'chain', 'chainminusone', 'okayokay',)
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))