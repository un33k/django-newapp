Django NewApp
====================

**A Sample Django application**

Overview
====================

A template for a new Django application.


How to install
====================

    1. easy_install django-newapp
    2. pip install django-newapp
    3. git clone http://github.com/un33k/django-newapp
        a. cd django-newapp
        b. run python setup.py
    4. wget https://github.com/un33k/django-newapp/zipball/master
        a. unzip the downloaded file
        b. cd into django-newapp-* directory
        c. run python setup.py


How to use
====================

   ```python
    # After installation, add newapp to your INSTALLED_APPS in the settings.py
    # Add newapp to your urls.py
    # Create the appropriate templates
   ```


Advanced users:
====================

   ```python
    # you rename every occurrence of newapp to your favorite app name
    # and build a new Django app fast.
   ```


Running the tests
====================

To run the tests against the current environment:

    python manage.py test


License
====================

Released under a ([BSD](LICENSE.md)) license.


Version
====================
X.Y.Z Version

    `MAJOR` version -- when you make incompatible API changes,
    `MINOR` version -- when you add functionality in a backwards-compatible manner, and
    `PATCH` version -- when you make backwards-compatible bug fixes.
