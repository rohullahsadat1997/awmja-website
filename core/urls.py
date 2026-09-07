from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("mission-vision/", views.mission_vision, name="mission_vision"),
    path("goals/", views.goals, name="goals"),
    path("activities/", views.activities, name="activities"),
    path("achievements/", views.achievements, name="achievements"),
    path("leadership/", views.leadership, name="leadership"),
    path("news/", views.news, name="news"),
    path("events/", views.events, name="events"),
    path("gallery/", views.gallery, name="gallery"),
    path("articles/", views.articles, name="articles"),
   path("contact/", views.contact, name="contact"),
path("contact/success/", views.contact_success, name="contact_success"),
    path(
    "articles/<slug:slug>/",
    views.article_detail,
    name="article_detail"
),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]