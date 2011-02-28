from django.http import HttpResponse
from Photos.models import Photos, FamilyMembers
from django.template import Context, loader
#Loading up a templating system, and the files should be in "templates/" directory
# Create your views here.

def index(request):
	return HttpResponse("hello, world. You're at the photo/family index")

def family(request):
	family_members = FamilyMembers.objects.all().order_by('id')
	t = loader.get_template('familytemplate.html')
	c = Context({'family_members': family_members})
	return HttpResponse(t.render(c))
	
def photos(request):
	last_8_photos = Photos.objects.all().order_by('id')[:8]
	t = loader.get_template('phototemplate.html')
	c = Context({'last_8_photos': last_8_photos})
	return HttpResponse(t.render(c))

def detail(request, Photos_photos_id):
	# return HttpResponse("This is a single photo detail page. %s" % Photos[Photos_photos_id].imagefile)
	return HttpResponse("This is a single photo detail page. %s" % dir(Photos.objects))

def upload(request):
	return HttpResponse("hello, upload here")

def familydetail(request, Photos_familymembers_id):
	return HttpResponse("Family member detail page.")
	
def server(request, path, document_root, show_indexes=False):
	return HttpResponse(document_root + '' + path)