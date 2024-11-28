from django import forms

class FormulaForm(forms.Form):
    formula = forms.CharField(label='Enter your formula', max_length=100)