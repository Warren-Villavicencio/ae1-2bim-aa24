
from django.urls import path


from copa_america import views


urlpatterns = [
        path('', views.copa_america, name='copa_america'),
        
 ]
