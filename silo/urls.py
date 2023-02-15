from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
    # path('', views.login_user,name='login_user'),
    # path('register/',views.register_user,name='register'),
    # path('logout/',views.logout_user,name='logout'),
    path('register/',views.register, name='register'),
    path('',views.login_user,name='login'),
    path('home/',views.home,name='home')
    # path('post-message/',views.post_message,name='post_message'),
    # path('profile/<int:id>',views.my_profile,name='profile'),
    # path('search_business/',views.search_for_business,name='search_business'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)