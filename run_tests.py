from django.conf import settings
from django.core.management import call_command
import sys


def main():
    # Dynamically configure the Django settings with the minimum necessary to
    # get Django running tests
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'options',
        ),
        # Django replaces all of this, but it still wants it. *shrugs*
        DATABASE_ENGINE = 'sqlite3',
        DATABASE_NAME = ':memory:',
        USE_L10N = True,
        USE_I18N = True,
        #ROOT_URLCONF = 'options.urls',
        # Put your required settings here
    )

    if len(sys.argv) > 1:
        if sys.argv[1] in ['-v', '--verbosity']:
            options = {'verbosity': int(sys.argv[2])}
    # Fire off the tests
    call_command('test', 'options', **options)


if __name__ == '__main__':
    main()
