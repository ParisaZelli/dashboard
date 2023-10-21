from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import post
from home.models import contact
from.forms import TestForm

def blog(request,auth=None,cat=None,**kwargs):
    posts=post.objects.filter(Active=1)
    if auth!=None:
        posts=posts.filter(author__username=auth)
    elif cat!=None:
        posts=posts.filter(category__name=cat)
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    context={'posts':posts}
    return render(request,'blog/blog.html',context)

@login_required
def blog_details(request,num):
    #Post=post.objects.get(pk=num,Active=1)
    Post=get_object_or_404(post,pk=num,Active=1)
    return render(request,'blog/blog_details.html',{'Post':Post})

def elements(request):
    return render(request,'blog/elements.html')

def latest_news(request):
    return render(request,'blog/latest_news.html')


def search(request):
    posts=post.objects.filter(Active=1)
    if request.method=='GET':
        posts=posts.filter(content__contains=request.GET.get('q'))
        return render(request,'blog/blog.html',{'posts':posts})


def test_form(request):
    if request.method=='POST':
        # name=request.POST.get('name')
        # email=request.POST.get('email')
        # subject=request.POST.get('subject')
        # message=request.POST.get('message')
        
        # form=TestForm(request.POST)
        # if form.is_valid():
        #     name=form.cleaned_data['name']
        #     email=form.cleaned_data['email']
        #     subject=form.cleaned_data['subject']
        #     message=form.cleaned_data['message']
        #     c=Contact()
        #     c.name=name
        #     c.email=email
        #     c.subject=subject
        #     c.message=message
        #     c.save()
        #     return redirect(to='/')
        form=TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/')
            
    else:
        form=TestForm()
        return render(request,'test.html',{'form':form})
