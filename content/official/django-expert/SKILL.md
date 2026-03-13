        ---
        name: django-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/django-expert/SKILL.md
        description: Build Django apps with clean views, ORM patterns, and proper settings structure.
        ---

        You build clean, maintainable Django applications.

## View Patterns
```python
# Class-based views for CRUD
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['name', 'email']
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        return super().get_queryset().filter(pk=self.request.user.pk)

# Form validation
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Email already in use.")
        return email
```

## Rules
- Use `select_related` and `prefetch_related` aggressively to prevent N+1.
- Custom managers for common query patterns.
- `get_object_or_404` instead of `.get()` in views.
- Settings: split into `base.py`, `local.py`, `production.py`.
