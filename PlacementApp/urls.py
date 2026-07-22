from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path("", views.index, name="home"),
    path("index.html", views.index, name="index"),

    # Login & Registration
    path("CompanyLogin.html", views.CompanyLogin, name="CompanyLogin"),
    path("CompanyLoginAction", views.CompanyLoginAction, name="CompanyLoginAction"),

    path("Register.html", views.Register, name="Register"),
    path("RegisterAction", views.RegisterAction, name="RegisterAction"),

    path("TPOLogin.html", views.TPOLogin, name="TPOLogin"),
    path("TPOLoginAction", views.TPOLoginAction, name="TPOLoginAction"),

    path("StudentLogin.html", views.StudentLogin, name="StudentLogin"),
    path("StudentLoginAction", views.StudentLoginAction, name="StudentLoginAction"),

    # Company
    path("PostJob", views.PostJob, name="PostJob"),
    path("PostJobAction", views.PostJobAction, name="PostJobAction"),

    path("AddQuestion", views.AddQuestion, name="AddQuestion"),
    path("AddQuestionAction", views.AddQuestionAction, name="AddQuestionAction"),

    # TPO
    path("ViewPerformance", views.ViewPerformance, name="ViewPerformance"),
    path("ViewFeedback", views.ViewFeedback, name="ViewFeedback"),

    # Student
    path("UpdateProfile", views.UpdateProfile, name="UpdateProfile"),
    path("UpdateProfileAction", views.UpdateProfileAction, name="UpdateProfileAction"),
    path("ModifyProfileAction", views.ModifyProfileAction, name="ModifyProfileAction"),

    path("Recommendation", views.Recommendation, name="Recommendation"),
    path("JobStatus", views.JobStatus, name="JobStatus"),

    path("ApplyJob", views.ApplyJob, name="ApplyJob"),

    path("Feedback", views.Feedback, name="Feedback"),
    path("FeedbackAction", views.FeedbackAction, name="FeedbackAction"),

    path("ExamTestAction", views.ExamTestAction, name="ExamTestAction"),
]
	       path("ExamTestAction", views.ExamTestAction, name="ExamTestAction"),
]
