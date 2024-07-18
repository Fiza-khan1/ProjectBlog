from django.shortcuts import render, redirect, get_object_or_404
from .models import PostModel,comments
from django.contrib.auth.decorators import login_required
from .forms import PostmodelForm,postUpdateForm,commentform
from Blogapp.templatetags import getval

def post(request):
    if request.method == 'POST':
        print('POST')
        form = PostmodelForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')  
        
    else:
        form = PostmodelForm()
        return render(request, 'blogappss/post.html', {'form': form})
    
    

def home(request):
    posts = PostModel.objects.all() 
    return render(request, 'blogappss/index.html', {'posts': posts})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    commentss = comments.objects.filter(post=post ,parent=None)
    replies = comments.objects.filter(post=post).exclude(parent=None)
    repdict={}
    for reply in replies:
        if reply.parent.id not in repdict.keys():
         repdict[reply.parent.id]=[reply]

        else:
            repdict[reply.parent.id].append(reply)


    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            parent_id = request.POST.get('PC_sno')
            parent_comment = None
            if parent_id:
                parent_comment = comments.objects.get(id=parent_id)
            comment = comments.objects.create(user=request.user, post=post, content=content, parent=parent_comment)
            return redirect('post_detail', pk=pk)
    else:
        form = commentform()

    context = {
        'post': post,
        'comments': commentss,
        'form': form,
        'repdict':repdict
    }
    return render(request, 'blogappss/post_detail.html', context)


def fullcontent(request,id):
    post=PostModel.objects.get(id=id)
    return render(request,'blogappss/fullcontent.html',{'post':post})

# def post_detail(request, pk):
#     post = get_object_or_404(PostModel, pk=pk)
#     commentss = comments.objects.filter(post=post, parent=None) 
#     replies=comments.objects.filter(post=post).exclude(parent=None) 
#     repDict={}
#     for reply in replies:
#         if reply.parent.id  not in repDict:
#             repDict[reply.parent.id] = [reply]
#         else:
#             repDict[reply.parent.id].append(reply)

#     print(repDict)
#     if request.method == 'POST':
#         form = commentform(request.POST)
#         if form.is_valid():
#             content = form.cleaned_data['content']
#             parent_id = form.cleaned_data.get('parent_id')
#             parent_comment = None
#             if parent_id:
#                 parent_comment = comments.objects.get(id=parent_id)
#             comment = comments.objects.create(user=request.user, post=post, content=content, parent=parent_comment)
#             return redirect('post_detail', pk=pk)
#     else:
#         form = commentform()

#     context = {
#         'post': post,
#         'comments': commentss,
#         'form': form,
#     }
#     return render(request, 'blogappss/post_detail.html', context)


def postEditform(request,pk):
    post=PostModel.objects.get(id=pk)
    if request.method=='POST':
        form=postUpdateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail',pk=post.id)

    else:
        form=postUpdateForm(instance=post)
    return render(request,'blogappss/edit.html',{'post':post,'form':form})

def post_delete(request,pk):
    post=PostModel.objects.get(id=pk)
    if request.method=='POST':
         post=PostModel.objects.get(id=pk)
         post.delete()
         return redirect('home')
    else: 
        return render(request,'blogappss/delete.html',{'id':pk})


