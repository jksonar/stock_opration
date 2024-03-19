from django import forms
from .models import Stocks

class StockForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = '__all__'

        labels = {
            'id': 'ID',
            'sname' : 'Stocks Name.',
            'sectors' : 'Sectors.' ,
            'holding' : 'Holding' ,
            'fname' : 'Mutual Fund-Name ',
            'ftype' : 'Mutual Fund-Type' ,
        }

        widgets  ={
            'id' : forms.NumberInput(attrs={'placeholder': 'eg. 101'}),
            'sname' : forms.TextInput(attrs={'placeholder': 'eg. TCS'}),
            'sectors' : forms.TextInput(attrs={'placeholder': 'eg. energy'}),
            'holding' : forms.NumberInput(attrs={'placeholder': 'eg. 10000'}),
            'fname' : forms.TextInput(attrs={'placeholder': 'eg. Adia '}),
            'ftype' : forms.TextInput(attrs={'placeholder': 'eg. small cab'}),
        }