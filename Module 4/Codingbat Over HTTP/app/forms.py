from django import forms

class FontTime(forms.Form):
    string = forms.CharField()
    num = forms.IntegerField()

class TeenSum(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()

class XYZThere(forms.Form):
    Input = forms.CharField()

class CenteredAverage(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()
    d = forms.IntegerField()
    e = forms.IntegerField()