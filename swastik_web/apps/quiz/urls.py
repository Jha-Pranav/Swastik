from django.urls import re_path
from apps.quiz import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    re_path(r"^(?P<myid>\d+)/$", views.quiz, name="quiz"),
    re_path(r"^(?P<myid>\d+)/data/$", views.quiz_data_view, name="quiz-data"),
    re_path(r"^(?P<myid>\d+)/save/$", views.save_quiz_view, name="quiz-save"),
    # Add the remaining URLs with or without trailing slash
    re_path(r"^add_quiz/$", views.add_quiz, name="add_quiz"),
    re_path(r"^add_question/$", views.add_question, name="add_question"),
    re_path(r"^add_options/(?P<myid>\d+)/$", views.add_options, name="add_options"),
    re_path(r"^results/$", views.results, name="results"),
    re_path(
        r"^delete_question/(?P<myid>\d+)/$",
        views.delete_question,
        name="delete_question",
    ),
    re_path(
        r"^delete_result/(?P<myid>\d+)/$", views.delete_result, name="delete_result"
    ),
]
