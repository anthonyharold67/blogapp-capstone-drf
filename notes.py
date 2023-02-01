print("Blog App Capstone Project")
#& pip install djangorestframework ü kurduk,bunu kurduğumuz için pip install django dememize gerek yok
#! pip install python-decouple secret key ve diğer env komutları için
#+ pip install django-cors-headers frontendi bağlamak için
# 
#? Permissions lar settingste global olark verilebilir, ya da views de istediklerine tanımlayabilirsin ve ayrıca custom permission da tanımlayabilirsin. 
#!settingste
"""REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}"""
#!viewsde
# from rest_framework.permissions import IsAuthenticated gibi   

#! pip install dj-rest-auth authentication işlemleri için hazır paket
#! pip install 'dj-rest-auth[with_social]' register ve social account işlemleri için hazır paket

# pip install drf-yasg