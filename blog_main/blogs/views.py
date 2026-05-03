from django.shortcuts import render, redirect, get_object_or_404 #type: ignore
from . models import Blog, Category

def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    # use try and except when we want to do some custom action if the category does't exists
    try:
        category = Category.objects.get(pk=category_id)
    except:
        #redirect the user to home page
        return redirect('home')
    # use get_object_or_404 when you want to show 404 error page if the category does't exists
    # category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)
