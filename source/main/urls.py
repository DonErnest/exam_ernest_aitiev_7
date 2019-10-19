"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import PollListRedirect, PollListView, PollDetailedView, PollCreateView, PollDeleteView, \
    PollUpdateView, ChoiceUpdateView, ChoiceDeleteView, ChoiceCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollListRedirect.as_view(), name='index'),
    path('polls/', PollListView.as_view(), name='list polls'),
    path('poll/<int:pk>/', PollDetailedView.as_view(), name='view poll'),
    path('poll/create/', PollCreateView.as_view(), name='create poll'),
    path('poll/<int:pk>/update', PollUpdateView.as_view(), name='update poll'),
    path('poll/<int:pk>/delete', PollDeleteView.as_view(), name='delete poll'),
    path('choice/<int:pk>/update', ChoiceUpdateView.as_view(), name='update choice'),
    path('choice/<int:pk>/delete', ChoiceDeleteView.as_view(), name='delete choice'),
    path('poll/<int:pk>/choice/add', ChoiceCreateView.as_view(), name='add choice')
]
