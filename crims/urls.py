from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from skin import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static
from media_handling import views as media_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^choose_skintone/$', views.choose_skintone, name='choose_skintone'),
    url(r'^choose_undertone/$', views.choose_undertone, name='choose_undertone'),
    url(r'^signup/$', accounts_views.signup, name='signup'),

    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^admin/', admin.site.urls),

    url(r'^uploads/$', media_views.uhome, name='uhome'),
    url(r'^form/$', media_views.model_form_upload, name='model_form_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
