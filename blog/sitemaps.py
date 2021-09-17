from django.contrib.sitemaps import Sitemap
from .models import Post
"""
Подробности, как работает карта сайта в Django
https://docs.djangoproject.com/en/2.0/ref/contrib/sitemaps/
"""

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated
