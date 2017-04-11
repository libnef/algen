from django import forms
from .models import Tag

class ProblemForm(forms.Form):
	LEVEL_CHOICES = (('A','A'),
	 	('B','B'),
	 	('C','C'),)
	DONE_CHOICE = ((0,'not done'),
		(1,'really bad'),
		(2,'bad'),
		(3,'mistake'),
		(4,'good'),
		(5,'great'),)
	levels = forms.MultipleChoiceField(
	 	choices=LEVEL_CHOICES, 
	 	widget=forms.CheckboxSelectMultiple,)
	lastest_exam_year = forms.ChoiceField([(15,'15'),(16,'16'),(17,'17')])
	include_assignments_of_score = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=DONE_CHOICE)
	if(Tag.objects.all().count() != 0):
		tags = Tag.objects.all().values('tag')
		tags = list(set([(t['tag'],t['tag']) for t in tags]))
		tags.insert(0,('no tag-filter','no tag-filter') )
		tag = forms.ChoiceField(required=False, choices=tags)

class ScoreForm(forms.Form):
	SCORE_CHOICES = ((1,'really bad'),
		(2,'bad'),
		(3,'mistake'),
		(4,'good'),
		(5,'great'),)
	score_your_solution = forms.ChoiceField(choices=SCORE_CHOICES, widget=forms.RadioSelect())

class TagForm(forms.Form):
	add_a_tag_to_problem = forms.CharField()