from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.shortcuts import HttpResponseRedirect
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token


class IndexView(TemplateView):
    template_name = 'index.html'
    acceptURL = (
        '/',
        '/login',
        '/register',
                 )
    def get(self, request, *args, **kwargs):
        if not ( request.user.is_authenticated() ):
            if request.path not in self.acceptURL:
                return HttpResponseRedirect('/login')

        context = self.get_context_data(**kwargs)
        rs= self.render_to_response(context)
        return rs

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)
