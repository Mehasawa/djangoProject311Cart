from  django import forms

class FormOrder(forms.Form):
    adres = forms.CharField(label='Адрес доставки')
    tel = forms.CharField(label='Телефон')
    nerobot = forms.BooleanField(label='не робот')