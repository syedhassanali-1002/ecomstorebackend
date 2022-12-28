from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # What tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #  if we add product and make its forign key that means our app is dependend upon store app's model product
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Define Generic Relationship we need two informations 
    # 1 Type (Product, Video, Picture etc) for table identification
    # 2 Id, of object to identify the specific record from database
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = models.GenericIPAddressField()