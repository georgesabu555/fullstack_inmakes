from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name='cricketerapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('cricketer/<int:cricketer_id>/',views.detail,name='detail'),
    path('add/',views.add_cricketer,name='add_cricketer'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root =settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)