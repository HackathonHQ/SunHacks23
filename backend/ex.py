from django.apps import apps
app_config = apps.get_app_config('allauth')
print(app_config.name)