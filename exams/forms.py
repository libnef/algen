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
	YEAR_CHOICES = ((15,'15'),
	 	(16,'16'),
	 	(17,'17'),)
	levels = forms.MultipleChoiceField(
	 	choices=LEVEL_CHOICES, 
	 	widget=forms.CheckboxSelectMultiple,)
	exam_years = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=YEAR_CHOICES)
	include_assignments_of_score = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=DONE_CHOICE, required=False)
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

class SolutionPictureForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class CommentForm(forms.Form):
    write_a_comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':40}))