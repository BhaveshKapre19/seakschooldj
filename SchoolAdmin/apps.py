from django.apps import AppConfig


class SchooladminConfig(AppConfig):
    name = 'SchoolAdmin'

    def ready(self):
        import SchoolAdmin.signal
