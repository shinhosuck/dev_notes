from django.contrib.auth.hashers import check_password

check_password(password_user_entered, request.user.password)

OR 

-User instance has access to check_password() method

user.check_password(password_user_entered)

