
# Parse form.errors
def profile_form_view(request):
    form = ProfileForm(request.POST or None)
    
    context = {
        'form': form,
        'errors': []
    }
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            for key, errors in form.errors.items():
                for error in errors:
                    context['errors'].append(error)
                    
    return render(request, 'profile.html', context)
                    
# Difference between add_error() and ValidationError()
'''
add_error() is used with field name level validation:
    example:
        def clean_name(self):
            name = self.clean_data.get('name')
            
            if len(name) > 10:
                raise forms.ValidationError('Name is too long')
        return name
        
        del clean(self):
            name = self.cleaned_data.get('name')
            
            if len(name) > 10:
                self.add_error('name', 'Name is too long.')
                
        return None
    
'''
