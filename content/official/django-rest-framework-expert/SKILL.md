        ---
        name: django-rest-framework-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/django-rest-framework-expert/SKILL.md
        description: Build DRF APIs with serializers, viewsets, permissions, and pagination.
        ---

        You build clean Django REST Framework APIs.

## ViewSet Pattern
```python
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['role', 'active']
    ordering_fields = ['created_at', 'name']

    def get_queryset(self):
        return User.objects.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
```

## Serializer Rules
- Use `read_only_fields` for auto-set fields (id, created_at).
- Override `validate_<field>` for field-level validation.
- Override `validate` for cross-field validation.
- Use `to_representation` to transform output, not `SerializerMethodField` for everything.

## Rules
- Use `select_related` / `prefetch_related` in `get_queryset`, not in serializers.
- Pagination must be set globally — never rely on client to request it.
