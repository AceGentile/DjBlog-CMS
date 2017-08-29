from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Dj_post

# Create your views here.
def index(request):
	latest_post = Dj_post.objects.all()
	template = loader.get_template('blog/index.html')
	context = {
		'latest_post' : latest_post,
	}
	return HttpResponse(template.render(context,request))