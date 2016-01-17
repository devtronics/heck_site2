from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from heck_site import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^$', views.home),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
