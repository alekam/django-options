
django-options
=============


Overview
~~~~~~~~

Easy and simple way to configure your django app


Installation
~~~~~~~~~~~~

Install developer version using PIP::

    pip install -e git+https://github.com/alekam/django-options#egg=options

Change ``settings.py`` of your project. Add ``options`` to
``INSTALLED_APPS``. Add required options (see: Settings).

Run ``manage.py syncdb`` or ``manage.py migrate options`` if you use South
and restart your project server.


Settings
~~~~~~~~

It has no any specific settings.


Usage
~~~~~

Simply install it and plug-in to your project. Have fun!
You can use it in your applications like this::

	from options import get_option
	my_opt = get_option('MY_OPTION', 3, store=False)

It'll be equivivalent to::

	from django.conf import settings
	my_opt = getattr(settings, 'MY_OPTION', 3)

Byt now you can change this option in the admin area.


Provided template tags and libraries
~~~~~~~~~~~~~~~~~~~~~~~

No any template tags and libraries provided


Provided management commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No any management commands provided


Testing
~~~~~~~

If this application is installed in your project you can run this inside your
project::

    python manage.py test options

or instead run inside this package::

    python run_tests.py

