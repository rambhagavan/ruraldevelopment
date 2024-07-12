from django.http import HttpResponse
from django.shortcuts import render,redirect
from userlist.models import supplier,company
from product_details.models import product,categorie
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from relation.models import relationtable
# request.session.flush() -> is used to close the session of the current Userp
STATE_CHOICES = (
    'Andhra Pradesh',
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Delhi',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'J&K',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal',
)


def helper(request):
    if request.user.is_authenticated:
        try:
            s=supplier.objects.get(user=request.user)
            return s.profileimage
        except:
            c=company.objects.get(user=request.user)
            return c.profileimage



def home(request):
    if request.user.is_authenticated:
        try:
            s=supplier.objects.get(user=request.user)
            data={
                # 'username': request.user.username,
                'name': s.name,
                'email':request.user.email,
                'phone':s.phone,
                'Where_To_Go':"supplierprofile",
                'city':s.city,
                'state':s.state,
                'zipcode':s.zipcode,
                'profileimage':s.profileimage,
            }
            return render(request,"index.html",data)
        except:
            c=company.objects.get(user=request.user)
            data={
                'username': request.user.username,
                'name': c.name,
                'email':request.user.email,
                'phone':c.phone,
                'city':c.city,
                'Where_To_Go':"companyprofile",
                'state':c.state,
                'zipcode':c.zipcode,
                'profileimage':c.profileimage,
            }
            return render(request,"index.html",data)
        # Tried for handle multiple exception But could not complete this task # except:
        # except ObjectDoesNotExist:
        #         logger.error('Object does not exist error')
        #         return render(request,"login.html")        
    return render(request,"index.html")

def companyregister(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        user1=None

        if User.objects.filter(username=request.POST.get('username')).exists():
            messages.error(request, "Username already taken!")
            return render(request,"companyregister.html")
        else:
            user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
            user.first_name = fname
            user.last_name  = lname
            user1=user
                # user.save() Aqge ki info ke bad save kiya hai alreaady to yaha jrvt nahi.
        city=request.POST.get('city')
        state=request.POST.get('state')
        zipcode=request.POST.get('zipcode')
        name=fname + " " + lname
        data=company(user=user1,name=name,city=city,state=state,zipcode=zipcode)
        data.save()
    k={
        'state':STATE_CHOICES
    }
    return render(request,"companyregister.html",k) 

def login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            auth_login(request, user)
            return redirect('/')
            # return render(request,'index.html',{'user':user})
        else:
            messages.error(request, "Username or Password is Incorrect")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

def supplierregister(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        user1=None

        if User.objects.filter(username=request.POST.get('username')).exists():
            messages.error(request, "Username already taken!")
            return render(request,"supplierregister.html")
        else:
            user = User.objects.create_user(request.POST.get(
                'username'), request.POST.get('email'), request.POST.get('password'))
            user.first_name = fname
            user.last_name  = lname
            user1=user
            # user.save()
        city=request.POST.get('city')
        state=request.POST.get('state')
        zipcode=request.POST.get('zipcode')
        name=fname+" "+lname
        data=supplier(user=user1,name=name,city=city,state=state,zipcode=zipcode)
        data.save()
    k={
        'state':STATE_CHOICES
    }
    return render(request,"supplierregister.html",k)

def allproducts(request):
    ew=product.objects.all()
    newew=[]
    old = None
    if request.method=="POST":
        whichstate=request.POST.get('whichstate')
        supp=supplier.objects.filter(state=whichstate)
        p=[]
        old = whichstate
        image=helper(request)
        for s in supp:
            pr=product.objects.filter(supplied_by=s.user)
            for prod in pr:
                p.append(prod)
        
            l=[]
            for t in p:
                if t.name not in l:
                    l.append(t.name)
            newew=[]
            for t in p:
                if t.name in  l:
                    newew.append(t)
                    l.remove(t.name)
        try:
            return render(request,"allproducts.html",{'old':old,'data':newew,'profileimage':image,'state':STATE_CHOICES}) 
        except:
            pass
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)

    return render(request,"allproducts.html",{'data':newew,'profileimage':image,'state':STATE_CHOICES})




def earthenware(request):
    ew=product.objects.filter(category=1)
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)
    return render(request,"Earthenware.html",{'data':newew,'profileimage':image})    

def stoneware(request):
    ew=product.objects.filter(category=3)   
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)
    return render(request,"Stoneware.html",{'data':newew,'profileimage':image})

def poreclain(request):
    ew=product.objects.filter(category=2)
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)
    return render(request,"Poreclain.html",{'data':newew,'profileimage':image})


def oils(request):
    ew=product.objects.filter(category=7)
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)
    return render(request,"oils.html",{'data':newew,'profileimage':image}) 

def vegetables(request):
    ew=product.objects.filter(category=15)
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)
    return render(request,"vegetables.html",{'data':newew,'profileimage':image}) 

def seeds(request):
    ew=product.objects.filter(category=14)
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)
    return render(request,"seeds.html",{'data':newew,'profileimage':image}) 


def decors(request):
    ew=product.objects.filter(category=10)
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)
    return render(request,"decors.html",{'data':newew,'profileimage':image}) 



def woods(request):
    ew=product.objects.filter(category=13)
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)
    return render(request,"woods.html",{'data':newew,'profileimage':image}) 


def clothingproducts(request):
    ew=product.objects.filter(category=12)
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)
    return render(request,"clothingproducts.html",{'data':newew,'profileimage':image}) 

def kajal(request):
    ew=product.objects.filter(category=8)
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)
    return render(request,"kajal.html",{'data':newew,'profileimage':image}) 

def lighting(request):
    ew=product.objects.filter(category=9)
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)
    return render(request,"lighting.html",{'data':newew,'profileimage':image}) 

def handcrafts(request):
    ew=product.objects.filter(category=11)
    l=[]
    for t in ew:
        if t.name not in l:
            l.append(t.name)
    newew=[]
    for t in ew:
        if t.name in  l:
            newew.append(t)
            l.remove(t.name)
    image=helper(request)
    return render(request,"handcrafts.html",{'data':newew,'profileimage':image}) 

def supplierprofile(request): 
    if request.user.is_authenticated:
        if request.method=="POST":
            # uuser=User.objects.get(email=request.POST.get('email'))
            supp=supplier.objects.get(user=request.user)
            supp.name=request.POST.get('name')
            supp.phone=request.POST.get('phone')
            supp.city=request.POST.get('city')
            supp.email=request.POST.get('email')
            supp.profileimage=request.FILES.get('profileimage')
            supp.state=request.POST.get('state')
            supp.zipcode=request.POST.get('zipcode')
            supp.save()
        s=supplier.objects.get(user=request.user)
        st=product.objects.filter(supplied_by=request.user)
        # st.save()
        # Relation table
        rt=relationtable.objects.filter(suppliedby=s)

        data={
            'username': request.user.username,
            'name': s.name,
            'email':request.user.email,
            'phone':s.phone,
            'city':s.city,
            'state':s.state,
            'zipcode':s.zipcode,
            'profileimage':s.profileimage,
            'productlist':st,
            'rt':rt,
            # 'rtsuppliedto':rt.suppliedto,
            # 'rtsuppliedby':rt.suppliedby,
            # 'rtproductsupplied':rt.productsupplied,
            # 'rtApproval':rt.Approval,

        }
        return render(request,"supplierprofile.html",data)
    return render(request,"login.html")        

def removeitems(request):
    if request.user.is_authenticated:
        st=product.objects.filter(supplied_by=request.user)
        data={
             'productlist':st,
             'profileimage':helper(request)
        }
        if request.method=="POST":
            product_id=product.objects.all()
            pid=request.POST.get('konsihtani')
            product.objects.filter(id=pid).delete()
    return render(request,"removeitems.html",data)    

def addproduct(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            c=request.POST.get('options')
            category=categorie.objects.get(name=c)
            name=request.POST.get('name')
            description=request.POST.get('description')
            image=request.FILES.get("productimage")
            supplied_by=request.user
            data=product(category=category,name=name,description=description,image=image,supplied_by=supplied_by)
            data.save()
        categories=categorie.objects.all()
        data={
                'categories':categories,
                 'profileimage':helper(request)
            }
        return render(request,"addproduct.html",data)    

def listofsupplier(request,productName):
    product_supp=product.objects.filter(name=productName)
    whichuser=[]
    # u=User.objects.get(username=request.user)
    # ut = None
    for t in product_supp:
        whichuser.append(supplier.objects.get(user=t.supplied_by))
        # if u == t.supplied_by:
        #     ut= t.supplied_by
    # for t in product_supp:
        # print(t)
    # whichuser=supplier.objects.all()
    data={
        'zipped':zip(product_supp,whichuser),
        'profileimage':helper(request)
    }
    return render(request,"listofsupplier.html",data)

def viewsupplierprofile(request,productname,suppliername):
    temp=User.objects.get(username=suppliername)
    supp=supplier.objects.get(user=temp)
    cp=company.objects.get(user=request.user)
    prid=product.objects.get(name=productname,supplied_by=temp)
    hired = 'N'
    if request.user.is_authenticated:
        if request.method=="POST":
            t=User.objects.get(username=suppliername)
            s=supplier.objects.get(user=t)
            p=product.objects.get(name=productname,supplied_by=t)
            c=company.objects.get(user=request.user)
            data1=relationtable(suppliedby=s,productsupplied=p,suppliedto=c,Approval='R')
            data1.save()
                
        try:
            rt=relationtable.objects.get(suppliedby=supp.id,suppliedto=cp,productsupplied=prid)
            # hired = 'R'
            # rt.Approval = 'R'
            # rt.save()
            # rt=relationtable.objects.filter(suppliedby=supp.id,suppliedto=cp)
            # for t in rt:
            # print(rt.suppliedby)
            # rt1=relationtable.objects.filter(suppliedto=request.user)
            # if rt.Approval == 'N':
            #     hired = 'N'
            if rt.Approval == 'R':
                hired = 'R'
            else:
                hired = 'H'
        except:
            pass
   
    data={
        'hired':hired,
        # 'username1':temp.name,
        'name':supp.name,
        'phone':supp.phone,
        'email':temp.email,
        # 'userid':temp.username,
        'city':supp.city,
        'state':supp.state,
        'zipcode':supp.zipcode,
        'pimage':supp.profileimage,   
        'profileimage':helper(request),
        'supplierName':suppliername
    }
    return render(request,"viewsupplierprofile.html",data)
  
def companyprofile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            # uuser=User.objects.get(email=request.POST.get('email'))
            comp=company.objects.get(user=request.user)
            comp.name=request.POST.get('name')
            comp.phone=request.POST.get('phone')
            comp.city=request.POST.get('city')
            comp.email=request.POST.get('email')
            comp.profileimage=request.FILES.get('profileimage')
            comp.state=request.POST.get('state')
            comp.zipcode=request.POST.get('zipcode')
            comp.save() 
            # uuser.save()
        s=company.objects.get(user=request.user)
        # st=User.objects.filter(username=request.user)
        rt=relationtable.objects.filter(suppliedto=s.id)
        whichuser=supplier.objects.all()
        # whichuser=[]
        data={
            'zipped':zip(rt,whichuser),
            # 'rt':rt,
            'username': request.user.username,
            'name': s.name,
            'email':request.user.email,
            'phone':s.phone,
            'city':s.city,
            'state':s.state,
            'zipcode':s.zipcode,
            'profileimage':s.profileimage,
        }
        return render(request,"companyprofile.html",data)    
    return render(request,"login.html")
# def deleteRequest(request,id):
#     if request.user.is_authenticated:
#         rt=relationtable.objects.get(id=id).delete()
#         rt.save()
#         return redirect(supplierprofile)
def Request(request,id,operation):
    # if request.user.is_authenticated:
    if operation == 'A':
        rt=relationtable.objects.get(id=id)
        rt.Approval='H'
        rt.save()
    else:
        rt=relationtable.objects.get(id=id).delete()
    return redirect(supplierprofile)