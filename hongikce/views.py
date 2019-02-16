from django.shortcuts import render, get_object_or_404

from .utils  import Crawler
from .models import Category, Board

def board_index(request):
    if request.method == 'POST':
        board_type = request.POST['board_type']    
        category   = get_object_or_404(Category, board_type=board_type)
        url = category.url

        crawler   = Crawler(url)
        snapshots = crawler.fetch()

        return redirect('board-index')

    posts        = Board.objects.all().order_by('-updated_at')[:10]
    categories   = Category.objects.all()

    data = { 
        'posts': posts,
        'categories': categories
    }

    return render(request, 'hongikce/index.html', data)


def board_for_category(request, category):
    posts = Board.objects \
                    .filter(category_eq=category) \
                    .order_by('-updated_at')[:10]

    data = { 
        'posts': posts
    }
    return render(request, 'hongikce/index_for_category.html', data)