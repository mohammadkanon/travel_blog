from django.shortcuts import render, get_object_or_404, redirect
from .models import CommonInfo, BestMoments, Tour, Comments

from .forms import TourForm, CommentForm

# Create your views here.
def index(request):
    info = CommonInfo.objects.order_by('-id').first()
    best = BestMoments.objects.all()
    tour = Tour.objects.all()

    context = {
        'info': info,
        'best': best,
        'tour': tour
    }
    return render(request, 'blog/index.html', context)

def all_blog(request):
    return render(request, 'blog/all-blog.html')

def recent_stories(request):
    return render(request, 'blog/recent-stories.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def single_post(request):
    single = Tour.objects.all()
    context = {
        'single': single,
    }
    return render(request, 'blog/single-post.html', context)

def post_detail(request, pk):

    user_info = request.session.get('user_info', False)

    single = get_object_or_404(Tour, pk=pk)
    comment = Comments.objects.filter(tour=single)
    if request.method == 'POST':
        form = CommentForm(single, user_info, request.POST)
        if form.is_valid():
            form.save()
            request.session['user_info'] = {
                'user_name': request.POST['visitor_name'],
                'user_email': request.POST['visitor_email']
            }
            return redirect('post-detail', pk)
    else:
        form = CommentForm(single, user_info)



    context = {
        'single': single,
        'form': form,
        'comment': comment,
    }

    return render(request, 'blog/post-detail.html', context)

def add_post(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('index')
    else:
        form = TourForm()
        return render(request, 'blog/post-form.html', {'form': form})

def edit_post(request, pk):
    item = get_object_or_404(Tour, pk=pk)
    form = TourForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'blog/post-form.html', {'form': form})

