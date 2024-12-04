"""
URL configuration for RENT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rentapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landingpage,name='landingpage'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('viewcategory/',views.viewcategory,name='viewcategory'),
    path('userregistration/',views.userreg,name='userreg'),
    path('userhome',views.userhome,name='userhome'),
    path('userprofile',views.userprofile,name='userprofile'),
    # path('useredit/<int:id>',views.userupdate,name='userupdate'),
    path('userupdate/',views.userupdate,name='userupdate'),
    path('login/',views.logins,name='logins'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('makerent',views.makerent,name='makerent'),
    path('viewusers',views.viewusers,name='viewusers'),
    path('removeuser/<int:uid>',views.removeuser,name='removeuser'),
    path('logout',views.logout,name='logout'),
    path('products',views.products,name='products'),
 
    path('viewproducts',views.viewproduct,name='viewproduct'),
    path('remove/<int:pid>',views.remove,name='remove'),
    path('removemyproduct/<int:pid>',views.removemyproduct,name='removemyproduct'),
    path("removecategory/<int:cid>",views.removecategory,name='removecategory'),
    path("rentitem/<int:pid>",views.rentitem,name='rentitem'),
    path("myproduct",views.myproduct,name="myproduct"),
    path("enquiry/",views.enquiry,name="enquiry"),
    path("removerequest/<int:rid>",views.removerequest,name="removerequest"),
    path("confirmrequest/<int:cid>",views.confirmrequest,name="confirmrequest"),
    path("disaproverequest/<int:did>",views.disaproverequest,name="disaproverequest"),


    path("myrenteditems/",views.myitems,name="myrenteditems"),

    path('returnproduct/<int:rid>', views.returnproduct, name='return_product'),
    path('cancelreturn/<int:rid>', views.cancelreturn, name='cancelreturn'),

    path('receivedproduct/<int:rid>',views.receivedproduct,name='receivedproduct'),
    path('notreceivedproduct/<int:nid>',views.notreceivedproduct,name='notreceivedproduct'),

    path('notreceivedproductincrement/<int:nid>',views.notreceivedproductincrement,name='notreceivedproductincrement'),


    path('removehistory/<int:rid>',views.removehistory,name='removehistory'),












]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



