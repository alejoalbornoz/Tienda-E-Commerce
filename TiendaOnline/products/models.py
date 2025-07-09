from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0) #12345678.12
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to="products/", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    # def save(self,*args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Product, self).save(*args, **kwargs)



    def __str__(self):
        return self.title
    

#este código asegura que antes de que se guarde una instancia del modelo Product, se llame a la función set_slug, que asigna un valor al campo slug basado en el título de la instancia. Esto es útil para automatizar la generación de slugs cuando se crean o modifican objetos del modelo Product.
def set_slug(sender, instance, *args, **kwargs): #callback
    if instance.title and not instance.slug:
        slug = slugify(instance.title)
#y esto hace qye se forme un slug unico en nuestra base de datos, ya que sino se generaria un error
        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                "{}-{}".format(instance.title, str(uuid.uuid4())[:8])
            )
        instance.slug = slug

pre_save.connect(set_slug, sender=Product)