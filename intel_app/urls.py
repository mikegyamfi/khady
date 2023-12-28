from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from .auth import authViews


urlpatterns = [
    path('', views.home, name="home"),
    path('services', views.services, name='services'),
    path('services/mtn', views.mtn, name='mtn'),
    path('services/airtel-tigo/', views.airtel_tigo, name='airtel-tigo'),
    path('services/mtn/', views.mtn, name='mtn'),
    path('history/airtel-tigo', views.history, name='history'),
    path('history/mtn', views.mtn_history, name="mtn-history"),
    path('verify_transaction/<str:reference>/', views.verify_transaction, name="verify_transaction"),
    path('import_thing', views.import_users, name="import_users"),

    path('pay_with_wallet/', views.pay_with_wallet, name='pay_with_wallet'),
    path('credit_user', views.credit_user, name='credit_user'),
    path('mtn_pay_with_wallet/', views.mtn_pay_with_wallet, name='mtn_pay_with_wallet'),
    path('topup-info', views.topup_info, name='topup-info'),
    path("request_successful/<str:reference>", views.request_successful, name='request_successful'),
    path('elevated/topup-list', views.topup_list, name="topup_list"),
    path('credit/<str:reference>', views.credit_user_from_list, name='credit'),

    path('login', authViews.login_page, name='login'),
    path('signup', authViews.sign_up, name='signup'),
    path('logout', authViews.logout_user, name="logout")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
