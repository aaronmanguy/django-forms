from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('warmup/font-times/', font_times, name="warmup"),
    path('logic/no-teen-sum/', no_teen_sum, name="logic"),
    path('string/xyz-there/', xyz_there, name="string"),
    path('list/centered-average/', centered_average, name="list"),
    path('admin/', admin.site.urls),
]
