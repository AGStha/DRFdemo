from django.db import models
from django.contrib.auth.models import User

class Creation(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	class Meta:
		abstract = True
# Create your models here.
class Product(Creation):
	user = models.ForeignKey(User, related_name="products", on_delete= models.CASCADE, null=True)
	name = models.CharField(max_length=100)
	price = models.PositiveSmallIntegerField()

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return self.name
