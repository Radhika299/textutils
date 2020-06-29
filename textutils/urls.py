
from django.contrib import admin
from django.urls import path
from textutilapp import views as v1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.index),
    path('analyze/',v1.analyze),

    # path('capitalize',v1.capitalize),
    # path('spaceremove',v1.spaceremove),
    # path('newlineremove',v1.newlineremove),
    # path('charcount',v1.charcount),



]
