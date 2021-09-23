from django.shortcuts import render
from .hashgen import Hash_Genrator
from .forms import Get_str_form
# Create your views here.

def home(request):
    gsf = Get_str_form()
    if request.method == "POST":
        gsf = Get_str_form(request.POST)
        if gsf.is_valid():
            hash_str = gsf.cleaned_data["hash_str"]
            gen_obj = Hash_Genrator(str(hash_str))
            data = {
                "md5":gen_obj.md5(),
                "sha1":gen_obj.sha1(),
                "sha224":gen_obj.sha224(),
                "sha256":gen_obj.sha256(),
                "sha384":gen_obj.sha384(),
                "sha512":gen_obj.sha512(),
                "blake2b":gen_obj.blake2b(),
                "blake2s":gen_obj.blake2s(),
            }
            return render(request,"home.html",{"data":data,"gsf":gsf})
    return render(request,"home.html",{"gsf":gsf})




