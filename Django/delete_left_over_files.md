```python

@receiver(post_delete, sender=Candidate)
def delete_files(sender, instance, **kwargs):
    # Access the deleted instance's fields to clean up
    if instance.resume:
        if os.path.isfile(instance.resume.path):
            os.remove(instance.resume.path)
    
    if instance.avatar and instance.avatar.name != 'avatars/default.png':
        if os.path.isfile(instance.avatar.path):
            os.remove(instance.avatar.path)
            
import os

def delete(self, *arg, **kwargs):
	super().delete(*args, **kwargs)
	
	if self.resume:
		if os.path.isfile(self.resume.path):
			os.remove(self.resume.path)
	
	if self.avatar and self.avartar.url != 'media/avatars/default.png':
		os.remove(self.avatar.path)

```
