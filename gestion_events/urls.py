
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('gestion_des_bn_plan.urls')),
    path('', include('gestion_news.urls')),
    path('', include('gestion_des_evenmnts.urls')),

]


