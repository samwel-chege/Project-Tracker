<<<<<<< HEAD
#!/home/sammie/Project Tracker/Backend/virtual/bin/python3
=======
#!/home/moringaschool/Documents/Project-Tracker/Backend/virtual/bin/python
>>>>>>> 8d473778c21e38cfcc78b4179635ae862557a600
# When the django-admin.py deprecation ends, remove this script.
import warnings

from django.core import management

try:
    from django.utils.deprecation import RemovedInDjango40Warning
except ImportError:
    raise ImportError(
        'django-admin.py was deprecated in Django 3.1 and removed in Django '
        '4.0. Please manually remove this script from your virtual environment '
        'and use django-admin instead.'
    )

if __name__ == "__main__":
    warnings.warn(
        'django-admin.py is deprecated in favor of django-admin.',
        RemovedInDjango40Warning,
    )
    management.execute_from_command_line()
