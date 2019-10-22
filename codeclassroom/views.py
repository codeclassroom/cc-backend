'''Test views for CodeClassroom. From the index view, list of classrooms can be viewed.
   From the classroom view, it's associated assignments can be viewed. From the assignment view,
   its associated questions can be viewed. Finally, in the question view, the problem statement, its 
   corresponding inputs and expected outputs may be viewed, and solutions may be submitted there.
'''
from django.shortcuts import render, redirect
from .models import ClassRoom, Assignment, Question
from .forms import ResponseForm

def index(request):
    '''Test index view. List out the existing classrooms.'''
    classrooms = ClassRoom.objects.all()

    return render(request, 'index.html', context={'classrooms': classrooms})

def classroom(request, pk):
    '''Test classroom view. List out the existing assignments.'''
    classroom = ClassRoom.objects.get(pk=pk)
    assignments = Assignment.objects.filter(classroom__pk=pk)

    context = {
        'title': 'ClassRoom Assignments',
        'classroom': classroom,
        'assignments': assignments,
    }

    return render(request, 'classroom.html', context=context)

def assignment(request, classroom, pk):
    '''Test assigment view. List out the assignment questions.'''
    classroom = ClassRoom.objects.get(pk=classroom)
    assignment = Assignment.objects.get(pk=pk)
    questions = Question.objects.filter(assignment=pk)
    # can we filter assignment questions based on classroom, or is classroom an unnecessary parameter?

    context = {
        'title': 'Assignment Questions',
        'classroom': classroom,
        'assignment': assignment,
        'questions': questions
    }

    return render(request, 'assignment.html', context=context)

def question(request, classroom, assignment, pk):
    '''Test question view. Show the question's details, submit solutions.'''
    classroom = ClassRoom.objects.get(pk=classroom)
    assignment = Assignment.objects.get(pk=assignment)
    question = Question.objects.get(pk=pk)

    # if request.method == 'POST':
    #     form = ResponseForm(request.POST)

    #     if form.is_valid():
    #         response = form.save(commit=False)
    #         response.question = question

    #         # auth stuff needed?
    #         # coderunner stuff

    #         response.save()
    #         return redirect('submission_result.html', ) # status as argument

    # else:
    #     form = ResponseForm()

    form = ResponseForm()

    context = {
        'title': f'Question {pk}',
        'classroom': classroom,
        'assignment': assignment,
        'question': question,
        'form': form,
    }

    return render(request, 'question.html', context=context)
