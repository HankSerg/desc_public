"""desc URL Configuration
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.views.generic import RedirectView

from django.conf.urls.static import static

from django.views.generic import TemplateView
from django.urls import path, re_path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from desc.apps.finance.api.views import ExpendViewSet
# import debug_toolbar

from desc.apps.finance.views import (
    finance_listview,
    all_finance_listview,
    finance_listview_date,
    # finance_detailview,
    # finance_createview,
    FinanceCreateView,
    FinanceDetailView,
    FinanceUpdateView,
    FinanceDeleteView,
    ArifmView, Arifm2View, Arifm2classView, RussView, TrudView, DetsadView, GirlsView,
    HomeView,
    get_data, ChartData,

    # AllFinanceListView
)

# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#       url(r'^__debug__/', include(debug_toolbar.urls)),
#         ] + urlpatterns

from profit.views import ProfitListView

# TODO переписать по возможности на path

sitemaps = {'posts': PostSitemap,}


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^auto/', include('desc.apps.auto.urls')),

    path('arifmetika/', ArifmView.as_view(), name='arifmetika'),
    path('russ/', RussView.as_view(), name='russ'),
    path('girls/', GirlsView.as_view(), name='russ'),
    path('учебники/арифметика/', ArifmView.as_view(), name='arifmetika'),
    path('учебники/арифметика2/', Arifm2View.as_view(), name='arifmetika2'),
    path('учебники/арифметика2класс/', Arifm2classView.as_view(), name='arifmetika2class'),
    path('учебники/русский/', RussView.as_view(), name='russ'),
    path('учебники/труд-школьника/', TrudView.as_view(), name='trud1'),
    path('учебники/детсад/', DetsadView.as_view(), name='detsad'),
    path('api/data/', get_data, name='api-data'),
    path('api/chart/data/', ChartData.as_view()),

    path('finance/', include('desc.apps.finance.urls')),

    url(r'^profit/', include('profit.urls')),

    path('catalog/', include('catalog.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    path('api/', include('desc.apps.finance.api.urls', namespace='api')),

    re_path(r'', include(wagtail_urls)),
    # url(r'^__debug__/', include(debug_toolbar.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns = [
#        url(r'^__debug__/', include(debug_toolbar.urls)),
#    ] + urlpatterns
