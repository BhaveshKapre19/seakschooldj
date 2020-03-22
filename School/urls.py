from django.urls import path
from .views import testView
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',testView,name="Test"),
]
