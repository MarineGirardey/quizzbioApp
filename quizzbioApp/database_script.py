from quizzbioApp.models import Question, Image, Answer
import csv
import sys


def questions():
    list_question_data = []

    if Question.objects.all():
        print('Questions already have data')

    else:
        csv_file = '/Users/marinegirardey/Documents/m2/prog_web/m2_web_project/quizzbioApp/questions/table_question.csv'

        with open(csv_file, newline='') as csv_file:
            spam_reader = csv.reader(csv_file, delimiter=',')
            for row in spam_reader:
                list_question_data.append(row)
        list_question_data.pop(0)

        for line_to_add in list_question_data:
            foo_instance = Question.objects.create(question=line_to_add[1],
                                                   type=line_to_add[2],
                                                   category=line_to_add[3],
                                                   imageField=line_to_add[4],
                                                   points=line_to_add[5],
                                                   nb_answer=line_to_add[6],
                                                   nb_image=line_to_add[7], )
            foo_instance.save()


def images():
    list_image_data = []

    if Image.objects.all():
        print('Image already have data')

    else:
        csv_file = 'quizzbioApp/static/images/images_new.csv'

        with open(csv_file, newline='') as csv_file:
            csv.field_size_limit(sys.maxsize)
            spam_reader = csv.reader(csv_file, delimiter=';')
            for row in spam_reader:
                list_image_data.append(row)
        list_image_data.pop(0)

        for line_to_add in list_image_data:

            foo_instance = Image.objects.create(image_name="images/" + line_to_add[1] + ".jpg",
                                                description=line_to_add[2],
                                                microscopy=line_to_add[3],
                                                cell_type=line_to_add[4],
                                                component=line_to_add[5],
                                                doi=line_to_add[6],
                                                organism=line_to_add[7])
            foo_instance.save()


def answer():
    list_answer_data = []

    if Answer.objects.all():
        print('Answer already have data')

    else:
        csv_file = 'quizzbioApp/answer/table_answer.csv'

        with open(csv_file, newline='') as csv_file:
            spam_reader = csv.reader(csv_file, delimiter=',')
            for row in spam_reader:
                list_answer_data.append(row)
        list_answer_data.pop(0)

        for line_to_add in list_answer_data:

            foo_instance = Answer.objects.create(id=line_to_add[0],
                                                 question_id=line_to_add[1],
                                                 answer=line_to_add[2],
                                                 definition=line_to_add[3])
            foo_instance.save()
            print(Answer.objects.all())
