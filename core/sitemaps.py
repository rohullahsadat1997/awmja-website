from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Article


class StaticPagesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return [
            "home",
            "about",
            "mission_vision",
            "goals",
            "activities",
            "achievements",
            "leadership",
            "news",
            "events",
            "gallery",
            "articles",
            "contact",
        ]

    def location(self, item):
        return reverse(item)


class ArticleSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Article.objects.filter(
            is_active=True
        ).order_by("-published_at", "order")

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse(
            "article_detail",
            kwargs={"slug": obj.slug}
        )