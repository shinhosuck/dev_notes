
pip install django-resized
pip install pillow


from django_resized import ResizedImageField

class Product(models.Model):
	name = models.ChartField(max_length=50)
    image = ResizedImageField(size=[300, 300], quality=75, upload_to="profiles/", force_format='WEBP', blank=True)
    # Replace "ImageField" with "ResizedImageField"
