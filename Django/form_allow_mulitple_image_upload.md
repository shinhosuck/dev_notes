class CreateProductImageForm(forms.ModelForm):
    allow_multiple_selected = True
    class Meta:
        model = ProductImage
        fields = ['image']

        labels = {
            'image': 'Product Images'
        }

        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }
