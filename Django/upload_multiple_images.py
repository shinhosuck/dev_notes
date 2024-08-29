class PostImageForm(forms.Form):
    allow_multiple_selected = True
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':True,'class':'image'}))
