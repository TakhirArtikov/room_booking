from django_filters import rest_framework as filters
from .models import Room


class RoomFilter(filters.FilterSet):
    start_date = filters.DateFilter(method="filter_start_date")
    end_date = filters.DateFilter(method="filter_end_date")

    class Meta:
        model = Room
        fields = ["start_date", "end_date", "room_price", "room_capacity"]

    @staticmethod
    def filter_start_date(queryset, name, value):  # pylint: disable=unused-argument
        return queryset.exclude(
            orders__order_start_date__lte=value, orders__order_end_date__gte=value
        )

    @staticmethod
    def filter_end_date(queryset, name, value):  # pylint: disable=unused-argument
        return queryset.exclude(
            orders__order_start_date__lte=value, orders__order_end_date__gte=value
        )
