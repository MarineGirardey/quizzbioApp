# Render to search html in templates
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import *
from django.contrib import messages
from .forms import UserRegistrationForm
from .additional_functions import all_equal
from django.contrib.auth.models import User
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home(request):
    image_source = []

    for x in Image.objects.all():
        pk_image_instance = Image.objects.get(pk=x.pk)
        image_source.append(pk_image_instance)

    img_chosed = random.sample(image_source, 3)
    image = {'image_src': img_chosed}

    return render(request, 'quizzbioApp/home.html', image)  # Return home.html template


def about(request):
    return render(request, 'quizzbioApp/about.html', {'title': 'About'})  # Return home.html template


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to Log In')
            return render(request, 'registration/login.html')
        else:
            messages.warning(request, 'Registration failed')

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def logout_function(request,):
    logout(request)
    return redirect('/')


@login_required
def profile(request,):
    return render(request, 'quizzbioApp/profile.html', {'title': 'Profile'})


def test_type(request,):
    return render(request, 'quizzbioApp/test_type.html')


def all_questions_test(request,):
    return render(request, 'quizzbioApp/test_type.html')


def quick_test(request,):
    return render(request, 'quizzbioApp/test_type.html')


def display_images(nb_image_display, image_num=None, random_num=None):
    image_source, image_pk, type_img = [], [], []
    answer_list = []

    print('img_num', image_num)
    for a in Answer.objects.all():
        if a.question_id == 2:
            answer_list.append(a.answer)

    for x in Image.objects.all():
        pk_image_instance = Image.objects.get(pk=x.pk)

        # QUICK TEST
        if random_num:

            if x.pk == random_num:

                for i in range(0, nb_image_display):
                    pk_image_instance = Image.objects.get(pk=x.pk + i)
                    image_source.append(pk_image_instance)
                    image_pk.append(x.pk + i)

                    if nb_image_display == 3:
                        type_img.append(pk_image_instance.microscopy)

                    if nb_image_display == 2:
                        type_img.append(pk_image_instance.component)

        # BIG TEST
        else:

            # First images
            if not image_num:

                # Prepare display for image 1, 2 and 3
                if x.pk == 1:
                    for i in range(0, nb_image_display):
                        pk_image_instance = Image.objects.get(pk=x.pk + i)
                        image_source.append(pk_image_instance)
                        image_pk.append(x.pk + i)

            # Next images
            else:
                if nb_image_display == 3:
                    # Prepare display of the 3 next images after the previous ones
                    if x.pk == int(image_num)+1 or x.pk == int(image_num)+2 or x.pk == int(image_num)+3:
                        image_source.append(Image.objects.get(pk=x.pk))
                        image_pk.append(x.pk)

                    # GET ANSWER FOR PREVIOUS IMG
                    # Get microscopy type of the previous 3 images
                    if x.pk == int(image_num) or x.pk == int(image_num)-1 or x.pk == int(image_num)-2:
                        type_img.append(pk_image_instance.microscopy)

                if nb_image_display == 2:
                    # Prepare display of the 2 next images after the previous ones
                    if x.pk == int(image_num) + 1 or x.pk == int(image_num) + 2:
                        image_source.append(Image.objects.get(pk=x.pk))
                        image_pk.append(x.pk)

                    # GET ANSWER FOR PREVIOUS IMG
                    # Get microscopy type of the previous 3 images
                    if x.pk == int(image_num) or x.pk == int(image_num)-1:
                        type_img.append(pk_image_instance.component)

    return image_source, image_pk, type_img


def get_response(micro_type_img, score, answer_id=None):
    user_response = 'undetermined'
    good_response = None
    answer_list = []

    if answer_id:
        # Browse objects in the Answer table to get the user response
        for a in Answer.objects.all():
            answer_objects = Answer.objects.get(pk=a.pk)
            answer_list.append(answer_objects.answer)
            if str(answer_objects.pk) == answer_id:
                user_response_id = answer_objects.pk
                user_response = answer_objects.answer

        if len(micro_type_img) != 0:
            # Check if images have the same microscopy mode
            result = all_equal(micro_type_img)

            if result:
                if micro_type_img[0] == 'None':
                    good_response = 'undetermined'
                else:
                    good_response = micro_type_img[0]
                    if good_response not in answer_list:
                        good_response = 'undetermined'

                if user_response == good_response:
                    score += 1

            else:
                good_response = 'undetermined'
                if user_response == good_response:
                    score += 1

    return score, good_response, user_response


def microscopy(request, image_num=None, answer_id=None, nb_quest=None, score=None):
    answer_list = []
    quest = 'Question Error'
    nb_image_display = 3
    end_the_test = None

    if not image_num:
        score = 0
    score = int(score)

    if not nb_quest:
        nb_quest = 0
    if int(nb_quest) == 10:
        end_the_test = 'end_the_test'

    quiz_type = request.path.split('/')[1]

    if quiz_type == 'quick_test':
        random_num = random.randint(1, 118)
        display_images_output = display_images(nb_image_display, image_num, random_num)

    else:
        if image_num:
            display_images_output = display_images(nb_image_display, image_num)
        else:
            display_images_output = display_images(nb_image_display)

    image_source = display_images_output[0]
    image_pk = display_images_output[1]
    type_img = display_images_output[2]

    # Get the form with GET method
    if request.method == 'GET':
        if answer_id:
            get_resp = get_response(type_img, score, answer_id)

        else:
            get_resp = get_response(type_img, score)

    score = get_resp[0]
    good_response = get_resp[1]
    user_response = get_resp[2]

    print('good', good_response)
    print('user', user_response)
    print('ques score', score)

    for q in Question.objects.all():
        if q.pk == 1:
            quest = q
    for a in Answer.objects.all():
        if a.pk < 5:
            answer_list.append(a)

    # if Score.objects.filter(user_id=(username).exists():
    context = {'quiz_type': quiz_type,
                'images': Image.objects.all(),
               'image_src': image_source,
               'image_nb': 3,
               'pk_image': image_pk,
               'quest': quest,
               'answers': answer_list,
               'nb_quest': nb_quest,
               'score': score,
               'end_the_test': end_the_test}

    return render(request, 'questions/questions.html', context)


def component(request, image_num=None, answer_id=None, nb_quest=None, score=None):
    nb_image_display = 2
    image_source, image_pk, type_img, answer_list = [], [], [], []
    user_response, quest = 'undetermined', "Question Error"
    end_the_test = None

    if not image_num:
        score = 0
    score = int(score)

    if not nb_quest:
        nb_quest = 0
    if int(nb_quest) == 10:
        end_the_test = 'end_the_test'

    quiz_type = request.path.split('/')[1]

    if quiz_type == 'quick_test':
        random_num = random.randint(1, 118)
        display_images_output = display_images(nb_image_display, image_num, random_num)
    else:
        if image_num:
            display_images_output = display_images(nb_image_display, image_num)
        else:
            display_images_output = display_images(nb_image_display)

    image_source = display_images_output[0]
    image_pk = display_images_output[1]
    type_img = display_images_output[2]

    # Get the form with GET method
    if request.method == 'GET':
        if answer_id:
            get_resp = get_response(type_img, score, answer_id)

        else:
            get_resp = get_response(type_img, score)

    score = get_resp[0]
    good_response = get_resp[1]
    user_response = get_resp[2]

    print('good', good_response)
    print('user', user_response)
    print('ques score', score)

    for q in Question.objects.all():
        if q.pk == 2:
            quest = q

    for a in Answer.objects.all():
        if a.pk > 4:
            answer_list.append(a)

    # if Score.objects.filter(user_id=(username).exists():
    context = {'images': Image.objects.all(),
               'image_src': image_source,
               'image_nb': 2,
               'pk_image': image_pk,
               'quest': quest,
               'answers': answer_list,
               'nb_quest': nb_quest,
               'score': score,
               'end_the_test': end_the_test}

    return render(request, 'questions/questions.html', context)


def end_the_test(request, score=None):
    if request.user.is_authenticated:
        username = request.user.username

        # for s in Score.objects.all():
            # user_score = Score.objects.create(user_name=username, score=glob_score)
            # user_score.save()
            # print('user score', user_score.score)

    score = {'score': score}
    return render(request, 'questions/end_of_test.html', score)
