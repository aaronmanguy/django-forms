from django import forms

class Hello(forms.Form):
    name = forms.CharField()

class Age(forms.Form):
    birth = forms.IntegerField()
    end = forms.IntegerField()

class Order(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()