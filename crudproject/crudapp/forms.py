from django import forms
from .models import Stocks

class StockForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = ['sname', 'sectors', 'holding', 'fname', 'ftype']  # Exclude the 'id' field from the form

        labels = {
            'sname' : 'Stocks Name.',
            'sectors' : 'Sectors.' ,
            'holding' : 'Holding' ,
            'fname' : 'Mutual Fund-Name ',
            'ftype' : 'Mutual Fund-Type' ,
        }

        widgets  ={
            'sname' : forms.TextInput(attrs={'placeholder': 'eg. TCS'}),
            'sectors' : forms.TextInput(attrs={'placeholder': 'eg. energy'}),
            'holding' : forms.NumberInput(attrs={'placeholder': 'eg. 10.02'}),
            'fname' : forms.TextInput(attrs={'placeholder': 'eg. Adia '}),
            'ftype' : forms.TextInput(attrs={'placeholder': 'eg. small cab'}),
        }