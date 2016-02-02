try:
    from django.conf.urls import url, patterns
except ImportError:
    # for Django version less than 1.4
    from django.conf.urls.defaults import url, patterns

from .views import HomePageView, PostDetailView, TaxView, TestView

urlpatterns = patterns(
        # url(r'^$', HomePageView.as_view(), name='home'),
        url(r'^(?P<tax>[\w-]+)$', TaxView.as_view(), name='page'),
        url(r'^(?P<tax>[\w-]+)$', TaxView.as_view(), name='tags'),
        url(r'^(?P<tax>[\w-]+)/(?P<slug>[-\w\d]+)$', PostDetailView.as_view(), name='post-detail'),
        # url(r'^categories/(?P<tax>[\w-]+)/$', CategoriesView.as_view(), name='categories'),
        # url(r'^test/$', TestView.as_view(), name='test'),
)
