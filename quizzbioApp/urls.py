from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="quizzbio-home"),
    path('about/', views.about, name="quizzbio-about"),  # View.about take the function about in the view.py file
    path("profile/", views.profile, name='quizzbio-profile'),
    path('register/', views.register, name='quizzbio-register'),
    path("login/", auth_views.LoginView.as_view(template_name='registration/login.html'), name='quizzbio-login'),
    path("logout/", views.logout_function, name='quizzbio-logout'),
    path("learn/", views.learn, name='quizzbio-learn'),

    path('test_type/', views.test_type, name="quizzbio-test_type"),
    path("all_questions_test/", views.all_questions_test, name='quizzbio-all_questions_test'),
    path("quick_test/", views.quick_test, name='quizzbio-quick_test'),

    path("all_questions_test/microscopy/", views.microscopy, name='quizzbio-all_microscopy'),
    path("all_questions_test/microscopy/<str:image_num>/<str:answer_id>/", views.microscopy, name='quizzbio-all_microscopy2'),
    path("all_questions_test/component/", views.component, name='quizzbio-all_component'),
    path("all_questions_test/component/<str:image_num>/<str:answer_id>/", views.component, name='quizzbio-all_component2'),

    path("quick_test/microscopy/", views.microscopy, name='quizzbio-quick_microscopy'),
    path("quick_test/microscopy/<str:image_num>/<str:answer_id>/<str:nb_quest>/<str:score>", views.microscopy, name='quizzbio-quick_microscopy2'),
    path("quick_test/component/", views.component, name='quizzbio-quick_component'),
    path("quick_test/component/<str:image_num>/<str:answer_id>/<str:nb_quest>/<str:score>", views.component, name='quizzbio-quick_component2'),

    path("end_of_test/<str:score>", views.end_the_test, name='quizzbio-end_of_test'),
    path("end_of_test/", views.end_the_test, name='quizzbio-end_of_test'),

]
