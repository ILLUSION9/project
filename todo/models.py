from django.db import models

# Create your models here.


class Zadacha(models.Model):
	Opisanie = models.CharField(max_length=100)
	Doing = 'Zaplanirovana'
	Done = 'Vypolneno'
	Canceled = 'Otmeneno'
	choice_status = (
			(Doing,'Zaplanirovana'),
			(Done, 'Vypolneno'),
			(Canceled, 'Otmeneno')
		)
	status = models.CharField(max_length=100, choices = choice_status, default=Doing)

	def __str__(self):
		return self.Opisanie