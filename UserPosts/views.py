from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required

from .models import UserPostModel
from .forms import UserPostModelForm

# Create your views here.
@login_required
def UserPostView(request):
    if request.method == 'POST':
        form = UserPostModelForm(request.POST)
        Post = UserPostModel()
        if form.is_valid():
            Post.PostBody = form.cleaned_data['PostBody']
            Post.PostUser = request.user
            Post.save()
            return redirect('UserProfiles:UserProfile', {'Username':request.user.username})

    else:
        form = UserPostModelForm()

    return render(request, 'UserPosts/UserPost.html', {'form': form})
