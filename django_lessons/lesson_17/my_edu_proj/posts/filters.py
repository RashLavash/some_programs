from rest_framework.filters import SearchFilter, BaseFilterBackend


class MyFilter(SearchFilter):
    def get_schema_fields(self, view, request):

        if request.query_params.get('me'):
            return ['text']

        return super().get_schema_fields(view, request)
    

class CustomFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(author=request.user)