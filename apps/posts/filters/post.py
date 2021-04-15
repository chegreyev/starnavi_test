import django_filters

from posts.models import Post


class PostFilterSet(django_filters.FilterSet):

    date_from = django_filters.IsoDateTimeFilter(field_name='created_at', lookup_expr='gte')
    date_to = django_filters.IsoDateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Post
        fields = [
            'uuid',
        ]
