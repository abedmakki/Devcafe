__author__ = 'Abedmakki'

from rest_framework.authtoken.models import Token
from django.contrib.auth import login , logout
from django.shortcuts import HttpResponsePermanentRedirect

def login_by_token(request , user):
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request , user)

def auth_Token(token):
    if token:
        token = token.replace("\"","")
        try:
            existToken = Token.objects.get(key=token)
            if existToken:
                user = existToken.user
                return user
            else:
                return None
        except: return None


class AuthenticationMiddlewareToken(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            return
        token = request.COOKIES.get('authenticatedAccount',None)
        if token:
            user = auth_Token(token)
            if user is not None:
                login_by_token(request,user)
                request.rememberMe = token
            else:
                logout(request)
                request.rememberMe = 'delete'

    def process_response(self, request, response):
        if response.status_code==401:
            logout(request)
            response = HttpResponsePermanentRedirect('/')
            response.status_code=401
            response.delete_cookie('authenticatedAccount')
        else:
            remember_token = getattr(request, 'rememberMe', None)
            if remember_token is not None:
                if remember_token=='delete':
                    response.delete_cookie('authenticatedAccount')
                else:
                    response.set_cookie( 'authenticatedAccount', remember_token , max_age=30*24*60*60 , expires=None )
                    response.set_cookie( 'accId', request.user.id , max_age=30*24*60*60 , expires=None )
        return response