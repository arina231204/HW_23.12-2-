from django.contrib import admin
from django.urls import path, include
from company import views
from rest_framework import routers
from django.contrib import admin
from django.urls import path

# router = routers.DefaultRouter()
# router.register('positions', views.PositionsViewSet)
# router.register('message', views.EmployeesViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('api/employees/', views.create_employees),
    path('api/positions/', views.create_Positions),

]
