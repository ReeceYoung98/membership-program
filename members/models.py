from django.db import models

class User(models.Model):
	email_address = models.TextField()
	password = models.TextField()
	salt = models.TextField()

	def __str__(self):
		return self.email_address

class UserDetail(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	forename = models.CharField(max_length=25)
	surname = models.CharField(max_length=25)
	birth_date = models.DateTimeField()

	def __str__(self):
		return self.forename + ' ' + self.surname + ' - ' + self.birth_date.strftime("%B %d, %Y")