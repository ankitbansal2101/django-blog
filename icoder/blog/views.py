from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse
from blog.models import Post,BlogComment

def bloghome(request):
    allposts=Post.objects.all()
    params={"allposts":allposts}
    print(allposts)
    return render(request,"blog/bloghome.html",params)
def blogpost(request,slug):
    post=Post.objects.get(slug=slug)
    comments=BlogComment.objects.filter(post=post)
    user=request.user
    count=len(comments)
    context={"post":post,"comments":comments,"user":user,"count":count}
    return render(request,"blog/blogpost.html",context)  

def postcomment(request):
    if request.method=="POST":
        user=request.user
        comment=request.POST.get("comment")
        print(comment)
        postSno=request.POST.get("postSno")
        post=Post.objects.get(sno=postSno)
        parentSno=request.POST.get("parentSno")
        if parentSno=="":
            comment=BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,"commented successfully")
        else:
            parent=BlogComment.objects.get(sno=parentSno) 
            comment=BlogComment(comment=comment,user=user,post=post,parent=parent )       
            comment.save()
            messages.success(request,"replied successfully")
    return redirect("/blog/{}".format(post.slug))        
 