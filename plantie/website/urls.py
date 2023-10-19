from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('your_plantie/', views.your_plantie, name='your_plantie'),
    path('why_plant/', views.why_plant, name='why_plant'),
    path('logout/', views.logout_user, name='logout'),
    path('signup_user/',views.signup_user, name = 'signup' ),
    path('plantie_images', views.plant_show, name='plant_show'),
    path('post_image/', views.post_image, name='post_image'),
    # path('success/', views.success, name='success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    # urlpatterns += staticfiles_urlpatterns()