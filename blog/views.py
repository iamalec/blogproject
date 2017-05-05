#coding: utf-8
from django.template import loader, Context
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse
from django.template import RequestContext, Template, loader
from django.contrib.auth.models import auth
from blog.models import BBS, Category
import os
import jwt
from blogproject import settings

def index(request):
    bbs_details = BBS.objects.all()
    return render_to_response('index.html', {'posts': bbs_details, 'user': request.user, 'path': request.path})

def p_china(request):
    bbs_chinas = BBS.objects.filter(category=Category.objects.filter(name='china'))
    return render_to_response('index.html', {'posts': bbs_chinas, 'user': request.user, 'path': request.path})
def p_usa(request):
    bbs_usas = BBS.objects.filter(category=Category.objects.filter(name='usa'))
    return render_to_response('index.html', {'posts': bbs_usas, 'user': request.user, 'path': request.path})
def sub_page(request, bbs_id):
    bbs_detail = BBS.objects.get(id=bbs_id)
    return render_to_response('detail.html', {'detail': bbs_detail, 'user': request.user})

#为了使用RequestContext,使用render函数,django1.9版本中render_to_response没有关键字context_instance
def login(request):
    DIR = os.path.dirname(os.path.dirname(__file__))
    html_dir = os.path.join(DIR, 'blog\\templates\\login.html')
    tf = open(html_dir, 'r')
    t = Template(tf.read())
    c = RequestContext(request, {'next': request.GET['next']})
    return HttpResponse(t.render(c))
#    return render_to_response('login.html', {'next': request.GET['next']})

def logout(request):
    user = request.user
    auth.logout(request)
    response = HttpResponse("<b>%s</b> logged out! <br><a href='/blog/'>Re-login</a>" % user.username)
    response.delete_cookie('username')
    return response

def login_acc(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    redirect_to = request.GET['next']
    user = auth.authenticate(username=username, password=password)

    token = {
    "short_name": settings.DUOSHUO_SHORT_NAME,
    "user_key": request.user.id,
    "name": request.user.username
            }
    print username
    duoshuo_token = jwt.encode(token, settings.DUOSHUO_SECRET)

    if user is not None:
        auth.login(request, user)
        content = '''
        Welcome %s !!!
        <a href='/logout/' >Logout</a>
        '''% user.username

        response = HttpResponseRedirect(redirect_to)
        response.set_cookie('username', username, 3600)
        response.set_cookie('duoshuo_token', duoshuo_token)
        return response
    else:
        return render_to_response('login.html', {'login_err': 'Wrong username or password!'})
