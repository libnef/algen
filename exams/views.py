from django.shortcuts import render, redirect
from .models import Exam, Problem, Solution, Score, Tag
from django.core import serializers
from .forms import ProblemForm, ScoreForm, TagForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import glob, datetime

score_parser = ['not done','really bad','bad','mistake','good','great']

# Create your views here.
def index(request):
	exams = Exam.objects.all()
	return render(request, 'exams/index.html', {'exams':exams})

def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            new_user = User.objects.create_user(username=username, password=password)
            new_user = authenticate(username=username, password=password)
            problems = Problem.objects.all()
            for problem in problems:
            	score = Score(user=new_user,problem=problem,score=0)
            	score.save()
            if new_user:
                auth_login(request, new_user)
            return redirect('index')
    else:
        form = UserCreationForm()
 
    return render(request, 'exams/create_user.html', {'form': form})

def exam(request,date):
	exam = Exam.objects.get(name=date)
	problems = Problem.objects.filter(exam=exam).values('pk','level','problem')
	data = list(problems)
	pk = problems[0]['pk']
	request.session['current_problems'] = data
	return redirect('problem', pk=pk)	

def problem(request, pk):
	if(pk=='-1'):
		return render(request, 'exams/no_hits.html', {})
	
	problems = request.session['current_problems']
	index_list = [ p['pk'] for p in problems ]
	this = index_list.index(int(pk))
	if (this == 0 ):
		last_i = len(index_list)-1
	else:
		last_i = this-1
	if (this == len(index_list)-1):
		next_i = 0
	else:
		next_i = this+1
	problem = Problem.objects.get(pk=pk)

	if request.method == 'POST':
		form = ScoreForm(request.POST)
		if form.is_valid():
			score = Score.objects.get(problem__pk=pk,user=request.user)
			score.score = int(form.cleaned_data['score_your_solution'])
			score.save()
			return redirect('problem', pk=index_list[next_i])
		tag_form = TagForm(request.POST)
		if tag_form.is_valid():
			tag_to_add = tag_form.cleaned_data['add_a_tag_to_problem']
			tag_to_add = tag_to_add.lower().strip()
			tag,created = Tag.objects.get_or_create(problem=problem,tag=tag_to_add)
			print(tag)
			print(created)
			tag.save()
			return redirect('problem', pk=pk)

	last_problem = problems[last_i]
	next_problem = problems[next_i]

	current_score = Score.objects.get(problem=problem,user=request.user)
	current_score = score_parser[current_score.score]
	problem_string = problem.exam.name + problem.level + problem.problem
	problem_name = problem.level + problem.problem
	problem_file = "problems/" + problem_string + ".png"
	solutions = Solution.objects.filter(problem=problem)
	solution_files = [ "problems/" + problem_string + "L" +  s.name + ".png" for s in solutions]
	
	form = ScoreForm()
	tag_form = TagForm()
	tags = Tag.objects.filter(problem=problem)
	return render(request, 'exams/problem.html', {'tags':tags,'tag_form':tag_form,'current_score':current_score,'problem_name':problem_name,'form':form,'problem_file':problem_file,'solution_files':solution_files, 'problems':problems, 'last_problem':last_problem, 'next_problem':next_problem})


def advanced_search(request):
	if request.method == 'POST':
		form = ProblemForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			levels = form.cleaned_data.get('levels') #exam_year, done
			tag = form.cleaned_data.get('tag')
			print()
			print(tag)
			tagged_problems = Tag.objects.filter(tag=tag).values('problem')
			if(len(tagged_problems)==0):
				tagged_problems = Problem.objects.all().values('pk')
				tagged_problems = [t['pk'] for t in tagged_problems]
			else:
				tagged_problems = [t['problem'] for t in tagged_problems]
			print(tagged_problems)
			print()
			exam_year = form.cleaned_data.get('lastest_exam_year')
			latest_date = datetime.datetime.strptime(exam_year, "%y")
			include_scores = form.cleaned_data.get('include_assignments_of_score')
			scores = Score.objects.filter(user=request.user, score__in=include_scores).values('problem')
			scores = [s['problem'] for s in scores]
			print(levels)
			print(latest_date)
			print(scores)
			pk_to_get = list(set(tagged_problems) & set(scores))
			problems = Problem.objects.filter(level__in=levels,exam__date__gte=latest_date,pk__in=pk_to_get).order_by('exam__date').values('pk','level','problem')
			request.session['current_problems'] = list(problems)
			if (len(problems)!=0):
				pk = problems[0]['pk']
			else:
				pk = -1
			done = form.cleaned_data.get('done')
		else:
			pk = -1
		form = ProblemForm()
		return redirect('problem', pk=pk)
	else:
		form = ProblemForm()
		not_done = Score.objects.filter(user=request.user, score=0).count()
		really_bad = Score.objects.filter(user=request.user, score=1).count()
		bad = Score.objects.filter(user=request.user, score=2).count()
		mistake = Score.objects.filter(user=request.user, score=3).count()
		good = Score.objects.filter(user=request.user, score=4).count()
		great = Score.objects.filter(user=request.user, score=5).count()
		current_scores = [('not done',not_done),('really bad',really_bad),('bad',bad),('mistake',mistake),('good',good),('great',great)]

	return render(request, 'exams/search.html', {'form':form,'current_scores':current_scores})	

# Create your views here.
def populate(request):
	Solution.objects.all().delete()
	Problem.objects.all().delete()
	Solution.objects.all().delete()	
	problems_dir = "./exams/static/problems/"
	cut = len(problems_dir)
	files = [ p[cut:] for p in glob.iglob(problems_dir+'*.png')]
	dates = set([ p[:6] for p in files])
	exams = Exam.objects.all().values('date')
	files.sort()
	exam = ""
	problem = ""
	for file in files:

		# check if new exam
		if file[:6]!=exam:
			exam = file[:6]
			date = datetime.datetime.strptime(exam, "%d%m%y")
			exm, created = Exam.objects.get_or_create(name=exam,date=date)
			exm.save()
			print("new exam = " + file[:6])

		# check if new problem
		if file[6:9]!=problem:
			problem = file[6:9]
			prb, created = Problem.objects.get_or_create(
				exam=exm,
				level=file[6:7],
				problem=file[7:9])
			prb.save()
			print("\tnew problem = " + file[6:9])

		# check if it's a solution
		if file[9:10]=="L":
			solution, created = Solution.objects.get_or_create(
				name=file[10:-4],
				problem=prb)
			solution.save()
			print("\t\tsolution: " + file[10:-4])
	return redirect(index)