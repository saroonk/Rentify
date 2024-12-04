from django.shortcuts import render,redirect,HttpResponse
from rentapp.models import CATEGORY,USERSDETAILS,PRODUCT,User,RENTITEM
from django.contrib.auth import authenticate,login,logout
from datetime import datetime



# Create your views here.

def adminhome(request):
    x=USERSDETAILS.objects.count()
    y=PRODUCT.objects.count()
    z=RENTITEM.objects.all()
    c=RENTITEM.objects.filter(status=False)
    cn=c.count()
    
    return render(request,'adminhome.html',{'x1':x,'y1':y,'z1':z,'count':cn})

def logins(request):
    if request.method=='POST':
        USERNAME=request.POST['uname']
        PASSWORD=request.POST['upass']
        userpass= authenticate(request,username=USERNAME,password=PASSWORD)
        if userpass is not None and userpass.is_superuser==1:
            return redirect(adminhome)
        elif userpass is not None and userpass.is_active==1 and userpass.usertype=='USER':
            login(request, userpass)
            request.session['user_id']=userpass.id
            return redirect(userhome)
        else:
            return HttpResponse("INAVALID USER NAME OR PASSWORD")
    else:
        return render(request,'login.html')



def logout(request):
    return redirect(logins)





    
    
def addcategory(request):
    if request.method=='POST':
        cat=request.POST['cat']
        x=CATEGORY.objects.create(Categoryname=cat)
        x.save()
        return redirect(viewcategory)
        
    else:
        return render(request,'Addcategory.html')
    
def viewcategory(request):
    x=CATEGORY.objects.all()
    return render(request,'viewcategory.html',{'x1':x})

def removecategory(request,cid):
    x=CATEGORY.objects.get(id=cid)
    x.delete()
    return redirect(viewcategory)




def userreg(request):
    if request.method=='POST':
        pic=request.FILES.get('img')
        fn=request.POST['fname']
        ln=request.POST['lname']
        age=request.POST['age']
        em=request.POST['email']
        ph=request.POST['phone']
        add=request.POST['address']
        un=request.POST['un']
        ps=request.POST['ps']
        x=User.objects.create_user(first_name=fn,last_name=ln,password=ps,username=un,email=em,usertype='USER')
        x.save()
        y=USERSDETAILS.objects.create(user_id=x,profile_image=pic,Age=age,phone=ph,Address=add)
        y.save()
        return render(request,"login.html")
    else:

        return render(request,'user_registration.html')


def userhome(request):
    users=request.session.get('user_id')
    use=USERSDETAILS.objects.get(user_id_id=users)
    uid=use.user_id_id
    c=CATEGORY.objects.all()
    x = PRODUCT.objects.exclude(Owner_id=uid)[:6]

    
    return render(request,"userhome.html",{'x1':x,'c1':c})
    
def userprofile(request):
    users=request.session.get('user_id')
    use=USERSDETAILS.objects.get(user_id_id=users)
    return render(request,'userprofile.html',{'view':use})



def userupdate(request):
    users=request.session.get('user_id')
    # print('llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll',users)
    use=USERSDETAILS.objects.get(user_id_id=users)
    uid=use.user_id_id
    us=User.objects.get(id=uid)
    if request.method=="POST":
        age=request.POST.get('age')
        address=request.POST.get('address')
        fnme=request.POST.get('fname')
        lnme=request.POST.get('lname')
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        img=request.FILES.get('pic')
        print(img)

        use.Address=address
        use.Age=age
        use.phone=ph
        use.profile_image=img
        us.first_name=fnme
        us.last_name=lnme
        us.email=em
        use.save()
        us.save()
        # print(us.first_name)
        return redirect(userprofile)
    else:
    
        return render(request,'userupdate.html',{'view':use})


    

def viewusers(request):
    x=USERSDETAILS.objects.all()
    return render(request,'viewusers.html',{'x1':x})

def removeuser(request,uid):
    x=USERSDETAILS.objects.get(id=uid)
    y=x.user_id.id
    x.delete()
    User.objects.filter(id=y).delete()
    return redirect(viewusers)


def makerent(request):
    users = request.session.get('user_id')
    use = USERSDETAILS.objects.get(user_id_id=users)
    uid = use.user_id_id

    if request.method == 'POST':
        
        od = uid
        cat = request.POST['cat']
        pi = request.FILES.get('pi')
        pn = request.POST['pn']
        pd = request.POST['pd']
        pp = request.POST['pp']
        pq = request.POST['pq']
        pt = request.POST['pt']  


        x = PRODUCT.objects.create(
            Owner_id=od,
            Category_name_id=cat,
            Product_name=pn,
            image=pi,
            description=pd,
            price=pp,
            price_type=pt,  
            quantity_available=pq
        )
        x.save()

        return redirect(userhome)
    
    else:
     
        x = CATEGORY.objects.all()
        return render(request, 'makerent.html', {'x1': x})






def products(request):
    users = request.session.get('user_id')
    use = USERSDETAILS.objects.get(user_id_id=users)
    uid = use.user_id_id
    search_query = request.GET.get('search', '') 

    x = PRODUCT.objects.exclude(Owner_id=uid)

    if search_query:
       
        x_filtered = x.filter(Product_name__icontains=search_query)
        no_match_found = len(x_filtered) == 0  
    else:
        x_filtered = x
        no_match_found = False  

    return render(request, "products.html", {'x1': x_filtered, 'search_query': search_query, 'no_match_found': no_match_found})

def viewproduct(request):
    x=PRODUCT.objects.all()
    return render(request,"viewproduct.html",{'x1':x})

def remove(request,pid):
    x=PRODUCT.objects.get(id=pid)
    x.delete()
    return redirect(viewproduct)

def removemyproduct(request,pid):
    x=PRODUCT.objects.get(id=pid)
    x.delete()
    return redirect(myproduct)





def myproduct(request):
    users=request.session.get('user_id')
    use=USERSDETAILS.objects.get(user_id_id=users)
    uid=use.user_id_id
    x=PRODUCT.objects.filter(Owner_id=uid)
    

    return render (request,"myproduct.html",{'x1':x})



    

def rentitem(request,pid):
    users=request.session.get('user_id')
    x=PRODUCT.objects.get(id=pid)
  
  
    if request.method=='POST':
        fd=request.POST['fd']
        td=request.POST['td']
        mobile=request.POST['num']

        from_date = datetime.fromisoformat(fd)
        to_date = datetime.fromisoformat(td) 


        y=RENTITEM.objects.create(product=x, from_date=from_date, to_date=to_date,mobile=mobile,username_id=users)
        

        y.save()
        return redirect(products)
        
    


        
    return render(request,'rentitem.html',{'product': x})






def enquiry(request):
    users = request.session.get('user_id')
    use = USERSDETAILS.objects.get(user_id_id=users)
    uid = use.user_id_id
    products = PRODUCT.objects.filter(Owner_id=uid)


    rent_items = RENTITEM.objects.filter(product__in=products)

    return render(request, 'enquiry.html', {'x1': rent_items})




def landingpage(request):
    return render(request,'landingpage.html')




def removerequest(request,rid):
    x=RENTITEM.objects.filter(id=rid)
    x.delete()
    return redirect(enquiry)

def disaproverequest(request,did):
    x=RENTITEM.objects.get(id=did)
    p=x.product_id
    y=PRODUCT.objects.get(id=p)

    x.status=False
    x.is_returned=False
    x.save()


    qa=y.quantity_available
    qa+=1
    y.quantity_available=qa
    y.save()
    return redirect(enquiry)


def receivedproduct(request,rid):
    x=RENTITEM.objects.get(id=rid)
    x.is_returned=True
    x.return_status = "Approved"


    p=x.product_id
    y=PRODUCT.objects.get(id=p)
    qa=y.quantity_available
    qa+=1
    y.quantity_available=qa
    y.save()
    x.save()

    return redirect(enquiry)

def notreceivedproduct(request,nid):
    x=RENTITEM.objects.get(id=nid)
    x.is_returned=False
    x.return_status = "Disapproved"
    x.save()
    return redirect(enquiry)


def notreceivedproductincrement(request,nid):
    x=RENTITEM.objects.get(id=nid)
    x.is_returned=False
    x.return_status = "Disapproved"

    p=x.product_id
    y=PRODUCT.objects.get(id=p)
    qa=y.quantity_available
    qa-=1
    y.quantity_available=qa
    y.save()
    x.save()
    return redirect(enquiry)







def confirmrequest(request,cid):
    x=RENTITEM.objects.get(id=cid)
    print(x.status)
    p=x.product_id
    y=PRODUCT.objects.get(id=p)
    if y.quantity_available >1:


        x.status=True
        x.save()
        qa=y.quantity_available
        qa-=1
        y.quantity_available=qa
        x.status=True
        y.save()
    elif y.quantity_available == 1:
        
        qa=y.quantity_available
        qa-=1
        y.quantity_available=qa
        y.is_available=False
        x.status=True
        x.save()
        
        y.save()

    

    return redirect(enquiry)



def myitems(request):
    users=request.session.get('user_id')
    x=RENTITEM.objects.filter(username_id=users).filter(status=True)
    return render(request,"my_renteditems.html",{'x1': x})


def returnproduct(request, rid):
    rent_item = RENTITEM.objects.get(id=rid)
    rent_item.is_returned = True
    rent_item.return_status = "Pending"
    rent_item.save()

    return redirect('myrenteditems')  


def cancelreturn(request,rid):
    rent_item = RENTITEM.objects.get(id=rid)
    rent_item.is_returned = False
    rent_item.return_status = "Pending"
    rent_item.save()

    return redirect('myrenteditems')  


def removehistory(request,rid):
    x=RENTITEM.objects.get(id=rid)
    x.delete()
    return redirect(enquiry)


    