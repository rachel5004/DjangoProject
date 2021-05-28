from django.shortcuts import render
from foodapp import models
# Create your views here.
def category(request):
    list1=models.category(1)
    cate_list1=[]
    for c in list1:
        ca={"no":c[0],"title":c[1],"poster":c[3],"subject":c[2]}
        cate_list1.append(ca)

    list2=models.category(2)
    cate_list2 = []
    for c in list2:
        ca = {"no": c[0], "title": c[1], "poster": c[3], "subject": c[2]}
        cate_list2.append(ca)

    list3=models.category(3)
    cate_list3 = []
    for c in list3:
        ca = {"no": c[0], "title": c[1], "poster": c[3], "subject": c[2]}
        cate_list3.append(ca)

    return render(request,'main/food/food_category.html',{"cate_list1":cate_list1,"cate_list2":cate_list2,"cate_list3":cate_list3})

def foodList(request):
    return render(request,'main/food/food_list.html')

def foodDetail(request):
    return render(request,'main/food/food_detail.html')