from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Blog
from django.db.models import Q
from .forms import ProjectForm
#from .models import Post
#create yours views here
def home(request):
    query = request.GET.get('search')
    if query:
        posts = Blog.objects.filter(title__icontains=query) | Blog.objects.filter(author__icontains=query)
    else:
        posts = Blog.objects.all()

    context = {
        'post': posts
    }
    return render(request, 'base.html', context)
def demo1(request):
    if request.method == 'POST':
        
        title=request.POST['title']
        description=request.POST['description']
        image=request.FILES.get('image')
        author=request.POST['author']
        email=request.POST['email']
        k=Blog(title=title,description=description,image=image,email=email,author=author)
        k.save()
    return render(request,"demo1.html")
def upload_page(request):
    if request.method == 'POST':
        print("harishhh")
        title=request.POST['title']
        description=request.POST['description']
        image=request.FILES.get('image')
        author=request.POST['author']
        email=request.POST['email']
        h=Blog(title=title,description=description,image=image,email=email,author=author)
        h.save()
    # Your form handling logic
    return render(request, 'upload_page.html')  # Renders the upload form page

'''def demo1(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after successful submission
    else:
        form = ProjectForm()

    return render(request, 'demo1.html', {'form': form})'''




def details(request, id):
    post = get_object_or_404(Blog, id=id)
    return render(request, 'details.html', {'post': post})
