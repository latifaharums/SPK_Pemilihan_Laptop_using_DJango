from django import forms
from .models import alternatif
class formtabel(forms.ModelForm):
    class Meta:
        model = alternatif
        fields = ['kodealternatif', 'namaalternatif', 'c1','c2','c3','c4','c5','c6','c7']
        widgets = {
            'kodealternatif': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Merk Laptop'}),
            'namaalternatif': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Seri Laptop'}),
            'c1': forms.Select(attrs={'class':'form-control', 'placeholder':'JUTA'}),
            'c2': forms.Select(attrs={'class':'form-control', 'placeholder':'GB'}),
            'c3': forms.Select(attrs={'class':'form-control', 'placeholder':'GB'}),
            'c4': forms.Select(attrs={'class':'form-control', 'placeholder':'prosesor'}),
            'c5': forms.Select(attrs={'class':'form-control', 'placeholder':'Inchi'}), 
            'c6': forms.Select(attrs={'class':'form-control', 'placeholder':'VGA'}), 
            'c7': forms.Select(attrs={'class':'form-control', 'placeholder':'Garansi'})          
        }
        labels ={
            'kodealernatif':'Merk Laptop',
            'namaalternatif':'Seri Laptop',
            'c1':'Harga',
            'c2':'RAM',
            'c3':'SSD',
            'c4':'Prosesor',
            'c5':'Ukuran Layar',
            'c6':'VGA',
            'c7':'Garansi'
        }
    