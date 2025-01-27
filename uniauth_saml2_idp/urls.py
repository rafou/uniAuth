from django.urls import path

from . import views

app_name = 'uniauth_saml2_idp'

urlpatterns = [
    path('login/', views.LoginAuthView.as_view(), name='login'),
    # path('sso/init', views.SSOInitView.as_view(), name="saml_idp_init"),
    path('sso/<str:binding>/', views.SsoEntryView.as_view(),
         name="saml_login_binding"),
    path('login/process/', views.LoginProcessView.as_view(),
         name='saml_login_process'),
    #  path('login/process_multi_factor/', views.get_metadata,
    #  name='saml_multi_factor'),
    path('login/process_user_agreement/',
         views.UserAgreementScreen.as_view(), name='saml_user_agreement'),
    path('slo/<str:binding>/', views.LogoutProcessView.as_view(),
         name="saml_logout_binding"),
    path('metadata/', views.metadata, name='saml2_idp_metadata'),

    path('test/500/', views.test500, name='test500'),
]
