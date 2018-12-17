from rest_framework import filters



class ContactSearchFilter(filters.BaseFilterBackend):
    """
        Search filter for Contact data.
    """
    def filter_queryset(self, request, queryset, view):
        params = request.query_params
        
        # Filter by email address.
        email = params.get('email', None)
        if email:
            queryset = queryset.filter(email=email)
        
        # Filter by name.
        name = params.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset