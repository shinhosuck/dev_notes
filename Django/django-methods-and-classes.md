from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models import Sum, Max, Avg, Min

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
only()
defer()
exclude()
distinct()
aggregate()
	-Product.objects.aggregate(max_price=Max('price'), min_price=Min('price'))

annotate()
Count()
    -Topic.objects.annotate(total_post_count = Count('post'))

select_related() &&
prefetch_related()
	-Model.objects.all().select_related('model', 'model')
	-Model.objects.all().prefetch_related('model', 'model') -> preloads the related objects or an object


# Difference between "aggregate()" and "annotate()":
	1. .aggregate() generates calculated summary of entire QuerySet.
	2. annotate() generates calculated summary of indivudual items in the QuerySet.


 # objs = Topic.objects.filter(total_post__lte = 1).annotate(post_count=Count('post')).values('post_count', 'total_post')
    # objs.update(total_post=F('total_post'))
    # print(objs)
    # print(connection.queries)


from django.http import Http404

try:
    obj = Model.objects.get(slug=slug)
except Model.DoesNotExist:
    raise Http404
