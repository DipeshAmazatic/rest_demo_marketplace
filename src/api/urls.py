from django.urls import path,include
urlpatterns = [  # pylint: disable=C0103
    path('1.0.0/',include(('api.v1_0_0.router','api'),namespace='1.0.0')),
]