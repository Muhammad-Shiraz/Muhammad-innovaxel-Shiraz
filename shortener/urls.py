from django.urls import path
from . import views

urlpatterns = [
    path('shorten', views.create_short_url),
    path('shorten/<str:code>', views.retrieve_original_url),
    path('shorten/<str:code>/update', views.update_short_url),
    path('shorten/<str:code>/delete', views.delete_short_url),
    path('shorten/<str:code>/stats', views.get_stats),
    path('s/<str:code>/', views.redirect_to_original_url),
    path('', views.html_shortener_view, name='shortener_html'),

]
