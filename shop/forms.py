from django import forms
form_control_class = {
    'class':'form-control'
}
class ProductForm(forms.Form):
    name = forms.CharField(label='Nama Produk', 
                            max_length=120, 
                            required=True,
                            widget=forms.TextInput(attrs=form_control_class)
                            )
    slug = forms.SlugField(label='Link produk', 
                            max_length=100, 
                            required=True,
                            widget=forms.TextInput(attrs=form_control_class))
    description = forms.CharField(
                            label='Deskripsi Produk',
                            widget=forms.Textarea(attrs=form_control_class))
    price = forms.IntegerField(label="Harga Produk", 
                            min_value=1000,
                            widget=forms.NumberInput(attrs=form_control_class))
    stock = forms.IntegerField(label="Jumlah Stok", 
                            min_value=0,
                            widget=forms.NumberInput(attrs=form_control_class))
    image = forms.ImageField(label="Foto produk", 
                            required=False,
                            widget=forms.FileInput(attrs=form_control_class))