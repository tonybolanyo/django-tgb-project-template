"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from tyrispages.views import index, pages

admin.site.site_header = '{{ project_name }} Backoffice'

urlpatterns = [
    path('admin/jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path(
        'admin/jet/dashboard', include('jet.dashboard.urls', 'jet-dashboard')
    ),  # Django JET Dashboard URLS
    path('admin/', admin.site.urls),
    path('health/', include('health_check.urls')),
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', pages, name='pages'),
    # The home page
    path('', index, name='home'),
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [path('rosetta/', include('rosetta.urls'))]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = (
        [path('__debug__/', include(debug_toolbar.urls))]
        + urlpatterns
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
