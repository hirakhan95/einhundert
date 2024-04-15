import threading

from django.apps import AppConfig

from .tasks import background_task


class SensorApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sensor_application'

    def ready(self):
        if threading.current_thread() is threading.main_thread():
            thread = threading.Thread(target=background_task)
            thread.daemon = True
            thread.start()
