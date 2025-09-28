from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models import Sum, Max, Avg, Min

# ajax specific

def some_view(request):
    content_type = request.headers.get('Content-Type') -> gives request content type (text/plain, application/json...)
    body = json.loads(reqest.body.decode('utf-8')) -> gives ajax request POST body
    return JsonResponse({}, status=200)

# end


F()
Q()
connection
request.user
request.GET.get()
request.GET
request.POST
request.FILES
order_by()
validate_password()
check_password()
set_password()
render_to_string()
clean_data()
get_host()
update()
validated_data()
OrderDict()
one_day_ago = timezone.now() - timedelta(days=1)
create_user()
    -User.objects.create_user()

request.data
raw() -> allows to perform raw SQL query
only()
defer()
exclude()
distinct()
aggregate()
	-Product.objects.aggregate(max_price=Max('price'), min_price=Min('price'))

annotate()
Count()
    -Topic.objects.annotate(total_post_count = Count('post'))

select_related() and prefetch_related()
	-Model.objects.all().select_related('model', 'model')
	-Model.objects.all().prefetch_related('model', 'model') -> preloads the related objects or an object
union()
reverse()
request.build_absolute_uri(reverse('core:home'))

# Difference between "aggregate()" and "annotate()":
	1. .aggregate() generates calculated summary of entire QuerySet.
	2. annotate() generates calculated summary of indivudual items in the QuerySet.


 # objs = Topic.objects.filter(total_post__lte = 1).annotate(post_count=Count('post')).values('post_count', 'total_post')
    # objs.update(total_post=F('total_post'))
    # print(objs)
    # print(connection.queries)

Model.objects.values_list('name', flat=True) -> without flat, returns tuples in a list - can pass multiple arguments (fields)
Model.objects.values('name') -> can pass multiple arguments and return dict in a list

from django.http import Http404

try:
    obj = Model.objects.get(slug=slug)
except Model.DoesNotExist:
    raise Http404

<!-- get app_names with request -->
<!-- remember that "request" and "resolver_match" both of these are object/instance. -->
<!-- when request.resolver_match is accessed, you get resolver_match properties/attributes -->
<!-- Example:  RESOLVER MATCH: ResolverMatch(func=utils.decorators.wrapper, args=(), kwargs={}, url_name='profile', app_names=['accounts'], namespaces=['accounts'], route='profile/')-->
app_names = request.resolver_match

# Field lookup within models:

    from django.conf import settings

    User = settings.AUTH_USER_MODEL

    class Author(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)

    class BlogPost(models.Model):
        author = models.ForeignKey(Author, on_delete=models.CASCADE)
        title = models.CharField(max_length=20)
        body = models.TextField()


    -traverse up and down lookups:

        -traverse up/forward
        obj = BlogPost.objects.get(author__user__username='admin', related_name="posts")

        -traverse down/reverse

            -without 'related_name'
            obj = Author.objects.get(blogpost__title='intro to python')

            -with 'related_name'
            obj = Author.objects.get(posts__title='intro to python')

    -using _set or related_name to fetch objs:

            obj = Author.objects.get(id=1)
            queryset = obj.blogpost_set.all() - with _set
            queryset = obj.posts.all() - with related_name

