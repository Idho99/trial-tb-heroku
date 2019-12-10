from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from imgpro_app.process import ImageEqualizer as imgEQ
from imgpro_app.models import TBImage
from imgpro_app.forms import TBImageForm

# Create your views here.
def HomeImg(request):
    if request.method == 'POST' and request.FILES['imgDefault']:
        myfile = request.FILES['imgDefault']
        fs = FileSystemStorage()
        filename = fs.save('image_input.jpg', myfile)
        uploaded_file_url = fs.path(filename)
        image = imgEQ(uploaded_file_url)
        uploaded_file_url = fs.url(filename)
        img_src_url = {'defImg':uploaded_file_url, 'proImg':image}
        return render(request, 'imgpro_app/img_pro.html', context=img_src_url)
    return render(request, 'imgpro_app/home_img.html', {'form':TBImageForm})

def ImgPro(request):
    return render(request, 'imgpro_app/img_pro.html')

def NewHomeImg(request):
    form = TBImageForm(data=request.POST or None)
    if request.POST == 'POST' and form.is_valid():
        img = form.save(commit=False)
        imgProcessed = request.FILES['imgProcessed'].name()
        print(imgProcessed)
        return render(request, 'imgpro_app/home_img.html', {'form':TBImageForm})
    return render(request, 'imgpro_app/home_img.html', {'form':TBImageForm})