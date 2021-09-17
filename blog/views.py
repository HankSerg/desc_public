from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from django.views.generic import ListView
from taggit.models import Tag
from django.db.models import Count
from django.utils import timezone
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm, SearchForm

# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    # в posts будет храниться список объектов
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list ,3) # по 3 шт на странице
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # если номер страницы больше, чем общее количество страниц, возвращаем последнюю
        posts = paginator.page(paginator.num_pages)
        #posts = Post.published.all()
    return render(request,
                'blog/post/list.html',
                {'page': page,
                'posts': posts,
                 'tag': tag} )

    # ниже код, который когда-то был
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    """
    Это обработчик страницы статьи. Он принимает на вход аргумент year, month,day и
    post и для получения по указанным слагу и дате
    :param request:
    :param year:
    :param month:
    :param day:
    :param post:
    :return:
    """
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # List of active comments for this post
    # список активных комментариев для записи
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        # отправили коммент
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # create comment object but don't save to database yet
            # создаём коммент, но пока не сохраняем
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            # привязываем комментарий к текущей статье
            new_comment.post = post
            # save the comment to the database
            # сохраняем комментарий в базе данных
            new_comment.save()
    else:
        # Если это GET запрос
         comment_form = CommentForm()

    # список похожих статей
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    """
    1. получает id тегов текущей статьи. Возвращает кортежи со значениями поля.
    2. получает все статьи, содержащие хотя бы один тег из полученных ранее, исключая текущую статью
    3. аггрегация
    4. сортирует список опубликованных статей в убывающем порядке
    """

    return render(request,'blog/post/detail.html', {'post':post,
                                                    'comments': comments,
                                                    'new_comment':new_comment,
                                                    'comment_form': comment_form,
                                                    'similar_posts': similar_posts})

def post_share(request, post_id):
    # получение статьи по идентификатору
    post = get_object_or_404(Post, id=post_id,status = 'published')
    sent = False
    if request.method == 'POST':
        # форма отправлена на сохранение
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # все поля формы прошли валидацию
            cd = form.cleaned_data
            # отправка электронной почты
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) рекомендует вам прочитать "{}"'.format(cd['name'],
                                                                   cd['email'], post.title)
            message = 'Прочитайте "{}" на {}\n\n{}\' комментарий: {}'.format(post.title,
                                                                     post_url, cd['name'], cd['comments'])
            send_mail(subject,message,'snorov@compeg.ru', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})

def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A')+ SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            results = Post.objects.annotate(search=search_vector,
                                            rank=SearchRank(search_vector, search_query)).filter(rank__gte=0.3).order_by('-rank')
    return render(request, 'blog/post/search.html', {'form': form,
                                                         'query': query,
                                                         'results': results})
# старый вариант
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})


# def post_new(request):
#     # form задать
#     form = PostForm()
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#         else:
#             form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})

#
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})
