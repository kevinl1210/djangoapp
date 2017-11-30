from django.shortcuts import render
from .models import Genre, Image
from django.views import generic
# from .mylib.calculation import calc

# Create your views here.
def index(request):
	# num_of_image = Image.objects.all().count()
	# girl_image = Image.objects.filter(imageName__contains='girl').count()
	request.session['num_visits'] += 1
	return render(request, 'index.html', 
		context={'num_visits': request.session['num_visits']},)


def about(request):
	return render(request, 'about.html',
		context={'num_visits': request.session['num_visits']},)


def classifier(request):
	if request.method == "POST":
		classify(request)
	return render(request, 'classifier.html',
		context={'num_visits': request.session['num_visits']},)


def classify(request):
	print(request.FILES)
	return render(request, 'classifier.html',
		context={'num_visits': request.session['num_visits'], 'test': 'hihi'},)


def notes(request):
	return render(request, 'notes.html',
		context={'num_visits': request.session['num_visits']},)


class ImageListView(generic.ListView):
	model = Image
	paginate_by = 10
	'''
	context_object_name = 'my_image_list'   # your own name for the list as a template variable
	queryset = Image.objects.filter(imageName__contains='girl') # Get 5 books containing the title war
	template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

	def get_context_data(self, **kwargs):
		context = super(ImageListView, self).get_context_data(**kwargs)
		context['some_data'] = "This is just some data"
		return context
	'''

class ImageDetailView(generic.DetailView):
	model = Image