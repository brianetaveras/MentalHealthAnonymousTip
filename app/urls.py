from django.urls import include, path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="health/index.html")),
    path('article/', views.article, name="article-view"),
]