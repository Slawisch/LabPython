from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Link
from .models import UserLike


def index(request):
    images_List = Link.objects.all()
    return render(request, 'Images/imageList.html', {'images_List': images_List})


def detail(request, link_id):
    try:
        a = Link.objects.get(id=link_id)
    except:
        raise Http404("Image not found")
    return render(request, 'Images/detail.html', {'link': a})


def addLikeDislike(request, link_id):
    try:
        a = Link.objects.get(id=link_id)
    except:
        raise Http404("Image not found")

    ul = UserLike.objects.filter(user_id=request.POST["nameId"], link_id=link_id).count()
    print(ul)

    if ul == 0:
        if "like" in request.POST:
            print("F")
            a.likes += 1
            ul = UserLike(isLike=True, link_id=link_id, user_id=request.POST["nameId"])
        elif "dislike" in request.POST:
            a.dislikes += 1
            ul = UserLike(isLike=False, link_id=link_id, user_id=request.POST["nameId"])
        elif "to_main" in request.POST:
            return HttpResponseRedirect(reverse('media:index'))
        a.save()
        ul.save()

    return HttpResponseRedirect(reverse('media:detail', args=(link_id,)))