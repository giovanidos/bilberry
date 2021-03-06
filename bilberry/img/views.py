from django.shortcuts import render
from img.models import Images
from django.http import  HttpResponse ,HttpResponseNotFound

# unchecked image controleur for displaying all unchecked images
def AllImages(request):
    try:
        images = Images.objects.all()
    except:
        images = None
    return render(request, 'pages/all.html',{'images': images})

# upload image controleur for handle form request of upload  
def uploadImage(request):
    if request.method == 'POST':
        image = Images()
        image.name = request.POST.get('nom')
        image.images = request.FILES.get('images')
        image.reject = False
        image.verified = False
        image.save()
        success = 'Your image was successful upload '
        return render(request,'pages/upload.html',{"success": success})
    else :
        success = None
        return render(request, 'pages/upload.html',{"success": success})

# controleur to display one images per pages
def showOneItem(request,id):
    try:
        image = Images.objects.get(pk=id)
    except:
        return render(request, 'pages/404.html')
    return render(request, 'pages/oneitem.html',{'image': image})

# controleur for handle reject or keept querry 
def treateImage(request,action,id):
    img = Images.objects.get(pk=id)
    if action == 'reject': # by default keept
        img.reject = True 
    else:
        img.reject = False
    img.verified = True
    img.save()
    _id = id + 1
    try:
        images = Images.objects.get(id=_id)
    except:
        return HttpResponse(0)
    return HttpResponse(images.id)
    # try:
    #    image = Images.objects.get(pk=id+1)
    #    if len(image) == 0:
    #        image = None
    #        return render(request, 'pages/oneItem.html', {'image': image})
    # except :
    #     image = None
    #     return render(request, 'pages/oneItem.html', {'image': image})
    # return render(request, 'pages/oneItem.html',{'image':image[0]})