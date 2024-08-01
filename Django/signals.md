from django.db.models.signals import post_save
from django.contrib.auth.models import User
from users.models import Profile
from django.dispatch import receiver


#Create signals.py
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs ):
    instance.profile.save()
    
  
#Create profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="profile")
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100)
    image = models.ImageField(default="profileImages/defaultImg.jpg", upload_to="profileImages")

#Set this in apps.py
def ready(self):
        import users.signals
