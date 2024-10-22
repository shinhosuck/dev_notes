# Command to run test

Runs all the tests:
coverage run manage.py test

Runs test on specified app:
coverage run manage.py test app_name

Run test on all models on a file:
coverage run manage.py test app_name.tests.test_models

Run test on specified function.
coverage run manage.py test app_name.tests.test_functions.some_func 


# Potential test
coverage report

# Show Coverage Report on HTML
coverage html


