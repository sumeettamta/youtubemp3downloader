from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from rest_framework.views import APIView
# Create your views here.
class Login(APIView):
    """
    """
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        print "sfsf"
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_deleted == 0 and user.activated == 1:
                user.last_login = datetime.datetime.now()
                # login(request, user)
                return HttpResponseRedirect(reverse('home'))
            elif user.activated == 0:
                message = 'Your Account has been disabled.'
            else:
                message = 'Invalid credentials. Please check the email/password entered.'
        else:
            message = 'Invalid credentials. Please check the email/password entered.'

        return render(request, self.template_name, {'message': message})

    def get(self, request, *args, **kwargs):
        # if request.user and request.user.is_authenticated() and request.user.is_deleted == 0:
        #     return HttpResponseRedirect(reverse('home'))
        print "dsadads"
        return render_to_response('login.html', {})

        # return render(request, 'login.html', {})
