from django.db import models


class Creation(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	class Meta:
		abstract = True
# Create your models here.
class Product(Creation):
	name = models.CharField(max_length=100)
	price = models.PositiveSmallIntegerField()

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return self.name
