from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"), #home page urls
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"), #about page urls
    path("support/", TemplateView.as_view(template_name="pages/support.html"), name="support"), #support page urls
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("mytask.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("main/", include("mytask.main.urls", namespace="main")), #main app urls
    path("setup/", include("mytask.setup.urls", namespace="setup")), #setup app urls
    path("employee/", include("mytask.employee.urls", namespace="employee")), #employee urls
    path("clients/", include("mytask.clients.urls", namespace="clients")), #clients urls
    path("task/", include("mytask.task.urls", namespace="task")), #task urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
