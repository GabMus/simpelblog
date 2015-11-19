from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponse                    #These two imports are no longer
#from django.template import RequestContext, loader      #needed when using render

from .models import Article, PagePost, BlogPost as Post


def index(request, page_id=None):
    artsPerPage=5
    npage=1
    ppage=-1
    if not page_id:
        page_id=0
    else:
        page_id=int(page_id)
        npage=page_id+1
        ppage=page_id-1
        page_id=page_id*5
        if page_id < 0: page_id=0

    if page_id!=0: selectedtab=-1
    else: selectedtab=0
    latest_post_list = Post.objects.order_by('-pub_date')[page_id:artsPerPage+page_id]
    if len(Post.objects.order_by('-pub_date')) < artsPerPage+page_id+1:
        npage=-1
    for i in latest_post_list:
        if len(i.post)>590:
            i.post=i.post[:590]+"..."
    context = {'latest_post_list': latest_post_list, 'selectedtab': selectedtab, 'npage': npage, 'ppage': ppage} #dictionary?
    return render(request, 'blog/index.html', context) #here's the magic shortcut *-*

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post.html', {'post': post})

def page(request, page_name):
    print(page_name)
    if page_name=="gear":
        selectedtab=1
    elif page_name=="projects":
        selectedtab=2
    elif page_name=="about":
        selectedtab=3
    else:
        selectedtab=-1
    post_list = PagePost.objects.filter(tag=page_name)
    context = {'latest_post_list': post_list, 'selectedtab': selectedtab, 'nothome': True} #dictionary?
    return render(request, 'blog/index.html', context)

"""
def results(request, question_id):
    response= "Result<br />You're looking at results of question %s."
    return HttpResponse(response  % question_id)

def vote(request, question_id):
    response= "Vote<br />You're voting on question %s."
    return HttpResponse(response  % question_id)
"""
