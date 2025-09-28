
PYTHON ANYWHERE SETUP:

1. gitclone "git repo url"
2. mkvirtualenv --python==/usr/bin/python3.9 venv
3. cd to project dir - pip3 install -r requirements.txt
4. add new webapp
5. Configure WSGI file:

	import os
	import sys

	path = '/home/andersonPortfolio/about_me'

	if path not in sys.path:
		sys.path.append(path)

	os.environ['DJANGO_SETTINGS_MODULE'] = 'porfolio.settings'

	from django.core.wsgi import get_wsgi_application
	application = get_wsgi_application()
	
	
COPY AND PASTE FROM THE TERMINAL:

copy: Ctrl-C 
paste: Ctrl-V
