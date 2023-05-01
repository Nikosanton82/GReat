# from django.db import models
# from django.template.defaultfilters import slugify

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     classification = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name_plural = "Categories"

# class MenuItem(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     slug = models.CharField(max_length=1000, null=True, blank=True)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     image = models.ImageField(upload_to='menu_images/')
#     ingredients = models.TextField()
#     sauce = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return self.name
    
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(str(self.category) + "-" + str(self.name))
#         return super().save(*args, **kwargs)