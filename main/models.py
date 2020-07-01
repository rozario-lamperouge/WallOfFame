from django.db import models
from datetime import datetime

# Create your models here.
class College(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'College'

	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=200)
	college = models.ForeignKey(College, verbose_name='College', on_delete=models.CASCADE, blank=True)
	date = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name_plural = 'Student'

	def __str__(self):
		return self.name

class Review(models.Model):
	stu_name = models.ForeignKey(Student, verbose_name='Student', on_delete=models.CASCADE, blank=True)
	review = models.TextField()
	pic = models.CharField(max_length=200)
	date = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.stu_name