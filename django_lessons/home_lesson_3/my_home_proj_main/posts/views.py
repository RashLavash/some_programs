from django.shortcuts import render



def posts_list(request):

    context = {
        'current_id': 6
    }
    return render(request, 'posts/posts_list.html', context)


def post_detail(request, id):

    context = {
        'user_id': id
    }
    return render(request, 'posts/post_detail.html', context)
