from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    """
    Здесь представлен новый свой менеджер, который при запросе будет выводить данные по статусу
    published
    """
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250) # Заголовок статьи.
    slug = models.SlugField(max_length=250, unique_for_date='publish') # Для формирования url-ов
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')

    body = models.TextField() # основное содержание статьи
    publish = models.DateTimeField(default=timezone.now) # дата публикации статьи
    created = models.DateTimeField(auto_now_add=True) # когда статья была создана
    updated = models.DateTimeField(auto_now=True) # когда статья была отредактирована
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    objects = models.Manager() # Менеджер по умолчанию
    published = PublishedManager() # Новый менеджер
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.month, self.publish.day, self.slug])

class Comment(models.Model):
    """
    post для привязки к посту один ко многим, одна статья может иметь множество комментариев,
    но каждый комментарий может быть только для одной статьи

    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    def __str__(self):
        return 'Comments by {} on {}'.format(self.name, self.post)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

# from wagtail.wagtailcore.models import Page
# from wagtail.wagtailcore.fields import RichTextField
# from wagtail.wagtailadmin.edit_handlers import FieldPanel
# from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
# from wagtail.wagtailsearch import index
#
#
#
# class BlogPage(Page):
#     main_image = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )
#     date = models.DateField("Post date")
#     intro = models.CharField(max_length=250)
#     body = RichTextField(blank=True)
#
#     search_fields = Page.search_fields + [
#         index.SearchField('intro'),
#         index.SearchField('body'),
#     ]
#
#     content_panels = Page.content_panels + [
#         FieldPanel('date'),
#         ImageChooserPanel('main_image'),
#         FieldPanel('intro'),
#         FieldPanel('body'),
#     ]
