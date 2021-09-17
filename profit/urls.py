from django.conf.urls import url


from .views import (
    ProfitListView,
    JoinFormView
)


urlpatterns = [
    # url(r'^$', ProfitListView.as_view(), name='list'),
    url(r'^join/', JoinFormView.as_view()),
    # url(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(), name='edit'),
    # url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='detail'),
    # url(r'^$', RestaurantListView.as_view(), name='list'),
]
