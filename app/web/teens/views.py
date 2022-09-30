from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import pyqrcode
import png
import pygame as pg
import pandas as pd
from cv2 import flip,rotate,imwrite,ROTATE_90_CLOCKWISE
import datetime
import base64


# Create your views here.
day=pd.read_csv("day.csv")
alpha=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
dat=datetime.date.today().strftime(r"-%m-%Y")
d=datetime.date.today().strftime(r"%d")
dayy=datetime.date.today().strftime(r"%a")
if (dayy=="Mon" and day.x[0]==0):
    dd=datetime.datetime.today() - datetime.timedelta(days=7)
    dd=str(dd)
    dd=dd[8:10]+dd[4:7]
    days=["name","number"]+alpha
    att=pd.DataFrame(columns=days)
    att2=pd.read_csv(str(dd)+dat[3:8]+".csv")
    print(str(dd)+dat[3:8])
    for i in range(len(att2.index)):
        att.loc[len(att.index)]=list(att2.iloc[i,0:2])+[0,0,0,0,0,0,0]
    att.to_csv(str(d)+str(dat)+".csv",index=False)
    day.x[0]=1
    day.to_csv("day.csv",index=False)
elif(dayy=="Sun"):
    day.x[0]=0
    day.to_csv("day.csv",index=False)

dd=datetime.datetime.today() - datetime.timedelta(days=alpha.index(dayy))
dd=str(dd)
dd=dd[8:10]+dd[4:7]
dat=str(dd)+dat[3:8]
print(dat)

def id(name,email,phone,password):
    att=pd.read_csv(dat+".csv")
    volu=pd.read_csv("volunterr.csv")
    volu.loc[len(volu.index)]=[name,email,phone,password]
    att.loc[len(att.index)]=[name,"2022"+str(day.num[0]),0,0,0,0,0,0,0]
    volu.to_csv("volunterr.csv",index=False)
    att.to_csv(dat+".csv",index=False)
    qrcod=pyqrcode.create(email)
    qrcod.png("qrcodee.png",scale=6)
    blue=(0,0,255)
    green=(0,255,0)
    pg.init()
    base_font=pg.font.Font(None,32)
    idcard=pg.display.set_mode((300,400))
    idcardr=idcard.get_rect()
    idcardr.center=(350,250)
    namee=base_font.render(f"Name: {name}",True,blue,None)
    contactt=base_font.render(f"Contact: {phone}",True,blue,None)
    emaill=base_font.render(f"Number: 2022{str(day.num[0])}",True,blue,None)
    day.num[0]+=1
    day.to_csv("day.csv",index=False)
    namer=namee.get_rect()
    contacttr=contactt.get_rect()
    emailr=emaill.get_rect()
    namer.center=(130,120)
    contacttr.center=(130,150)
    emailr.center=(130,180)
    qrcod=pg.image.load("qrcodee.png")
    qrcodr=qrcod.get_rect()
    qrcodr.center=(150,300)
    logo=pg.image.load("logo.png")
    logo=pg.transform.rotozoom(logo,0,0.3)
    logor=logo.get_rect()
    logor.center=(150,50)
    idcard.fill(green)
    idcard.blit(namee,namer)
    idcard.blit(contactt,contacttr)
    idcard.blit(emaill,emailr)
    idcard.blit(qrcod,qrcodr)
    idcard.blit(logo,logor)
    pg.display.flip()
    idcard=pg.surfarray.array3d(idcard)
    idcard=flip(idcard,0)
    idcard=rotate(idcard, ROTATE_90_CLOCKWISE)
    imwrite("web/idcard.png",idcard)
    pg.quit()
    print("done successfully")


def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        id(name,email,phone,password)
        print(name,email,phone,password)
        # return render("thanku.html")
        file_location = 'web/idcard.png'


        with open(file_location, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        ctx = {"image": image_data}

        return render(request, 'thanku.html', ctx)

    return render(request,'index.html')

def add_volu(request):

    return render(request,'donor.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def donate(request):
    return render(request,'donate.html')

def gallery(request):
    return render(request,'gallery.html')

def bedonor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('contact')
        donations=pd.read_csv("donation.csv")
        donations.loc[len(donations.index)]=[name,number]
        donations.to_csv("donations.csv",index=False)
        print(name,number)
        return render(request,'Thankyou.html')
    return render(request,'donar.html')

def added(request):
    return render(request,"index.png")

