


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    seller_organization = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='product_image')
    description = models.CharField(max_length=100)
    detail = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_str_format = models.CharField(max_length=1000, null=True, blank=True)
    discount_price_str_format = models.CharField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    num_of_times_solid = models.IntegerField(default=0)
    likes = models.DecimalField(max_digits=5, decimal_places=1 ,default=0.0)


    def save(self, *arg, **kwarg):
        self.price_str_format = '{0:,}'.format(price)
        super().save(*arg, **kwarg)
