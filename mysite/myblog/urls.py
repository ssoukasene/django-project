from django.conf.urls import url
from myblog.views import stub_view

urlpatterns = [
    url(r'^$',
        stub_view,
        name="blog_index"),
]