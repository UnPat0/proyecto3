from django import forms
from app_mercado import Productos







class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
        cantidad_a_comprar = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 21)],
        )