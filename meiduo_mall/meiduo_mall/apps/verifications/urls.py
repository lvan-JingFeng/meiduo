from django.conf.urls import url,re_path
from . import views

urlpatterns = (
    re_path(r'image_codes/(?P<image_code_id>\d+)/$', views.ImageCodeView.as_view()),
)