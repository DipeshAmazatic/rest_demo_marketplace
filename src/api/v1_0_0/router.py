"""
Router url
"""
from traceback import print_tb
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from knox import views as knox_views
from .views.user_views import UserViewSet
from .views.product_views import ProductViewSet
from .views.company_views import CompanyViewSet
from .views.variant_views import VariantViewSet
from .views.specification_views import SpecificationViewSet
router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('company', CompanyViewSet, basename='company')
router.register('product', ProductViewSet, basename='product')
router.register('variants', VariantViewSet, basename='variants')
router.register('specification', SpecificationViewSet, basename='specification')
urlpatterns = [
    path('', include(router.urls)),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]

