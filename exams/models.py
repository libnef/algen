from django.db import models
from django.utils import timezone

class Exam(models.Model):
    name = models.CharField(max_length=6,default="")
    date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return ' [' + self.name + '] '

class Problem(models.Model):
	exam = models.ForeignKey(Exam)
	level = models.CharField(max_length=1,default="")
	problem = models.CharField(max_length=2,default="")

	def __str__(self):
		return ' [' + self.exam.name + self.level + self.problem + '] '

class Solution(models.Model):
	name = models.CharField(max_length=4)
	problem = models.ForeignKey(Problem)

class Score(models.Model):
	user = models.ForeignKey(
		'auth.User',
		on_delete=models.CASCADE)
	problem = models.ForeignKey(Problem)
	score = models.IntegerField(default=0)

class Tag(models.Model):
	problem = models.ForeignKey(Problem)
	tag = models.CharField(max_length=20)

	class Meta:
	    unique_together = ('problem', 'tag',)

	def __str__(self):
		return self.tag