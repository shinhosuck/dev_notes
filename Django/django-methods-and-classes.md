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
only()
defer()
exclude()
render_to_string()
clean_data()
get_host()
distinct()

set_password()
create_user()
    -User.objects.create_user()

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
