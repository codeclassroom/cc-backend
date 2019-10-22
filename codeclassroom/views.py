'''Test views for CodeClassroom. From the index view, list of classrooms can be viewed.
   From the classroom view, it's associated assignments can be viewed. From the assignment view,
   its associated questions can be viewed. Finally, in the question view, the problem statement, its 
   corresponding inputs and expected outputs may be viewed, and solutions may be submitted there.
'''
from django.shortcuts import render
from .models import ClassRoom, Assignment, Question

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
    assigment = Assignment.objects.get(pk=pk)
    questions = Question.objects.filter(assignment=pk)
    # can we filter assignment questions based on classroom, or is classroom an unnecessary parameter?

    context = {
        'title': 'Assignment Questions',
        'classroom': classroom,
        'assignment': assigment,
        'questions': questions
    }

    return render(request, 'assignment.html', context=context)

def question(request, classroom, assignment, pk):
    '''Test question view. Show the question's details, submit solutions.'''
    question = Question.objects.get(pk=pk)

    context = {
        'title': f'Question {pk}',
        'classroom': classroom,
        'assigment': assignment,
        'question': question,
    }

    return render(request, 'question.html', context=context)
