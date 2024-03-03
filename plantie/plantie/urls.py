
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('gsheets.urls')),
    path('', include('website.urls')),
    # all OAuth operations are hnagled by allauth
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view()),  # deafult Django look at logout


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
