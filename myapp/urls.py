from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^images/$', views.ImageListView.as_view(), name='images'),
    url(r'^image/(?P<pk>\d+)$', views.ImageDetailView.as_view(), name='image-detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^classifier/$', views.classifier, name='classifier'),
    url(r'^notes/$', views.notes, name='notes'),
    url(r'^classify/$', views.classify, name='classify'),
]