from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 3
    limit_query_param = "custom_limit"
    offset_query_param = "custom_offset"
