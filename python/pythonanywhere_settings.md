# PYTHON ANYWHERE SET UP VENV

# once registered and logged in, click 'bash'

1. Clone git repo:
    - git clone https://github.com/shinhosuck/django-reactjS-pet-blog-backend.git

2. Create virtual environtment:
    - mkvirtualenv --python=/usr/bin/python3.9 venv

3. Install requirements.txt -> cd into the project:
    - pip3 install -r requirements.txt

4. Open web-tab and click on "add a new web app"
    - just follow the screen instruction to set up new app
    - remember to click on "manually configure"

5. Virtualenv
    - find "Virtualenv" sub-header and click on "Enter path to virtualenv"
    - enter the virtualenv name -> 'venv'

5. Configure WAGI
    - find "Code" sub-header
    - click on "WSGI configuration file" to configure WSGI

5. Then find 'Code' and click on 'WSGI configuration file'

import os
import sys

path = '/home/pawpals/django-reactjS-pet-blog-backend'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

6. Navigate to 'Web' page and copy your web address 'pawpals.pythonanywhere.com' and add it to allowed url in the settings.py


COPY AND PASTE FROM THE TERMINAL:

copy: Ctrl-C 
paste: Ctrl-V
