from django.shortcuts import render
import pyqrcode
import pandas as pd
import cv2
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
global qrnum

def id(name,email,phone,password):
    att=pd.read_csv(dat+".csv")
    volu=pd.read_csv("volunterr.csv")
    volu.loc[len(volu.index)]=[name,email,phone,password]
    att.loc[len(att.index)]=[name,"2022"+str(day.num[0]),0,0,0,0,0,0,0]
    volu.to_csv("volunterr.csv",index=False)
    att.to_csv(dat+".csv",index=False)
    qrcod=pyqrcode.create(email)
    qrcod.png("data/qrcodw.png",scale=6)
    idcard = cv2.imread("logo.png")
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(idcard, f'Name: {name}', (10,250), font, 1, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(idcard, f'Contact: {phone}', (10,300), font, 1, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(idcard, f'Number: 2022{list(day.num)[0]}', (10,350), font, 1, (0,0,0), 1, cv2.LINE_AA)
    x_offset=100
    y_offset=400
    qrcod=cv2.imread("data/qrcodw.png")
    idcard[y_offset:y_offset+qrcod.shape[0], x_offset:x_offset+qrcod.shape[1]] = qrcod
    cv2.imwrite(f"data/2022{day.iloc[0,1]}.png", idcard)
    qrnum=day.iloc[0,1]
    day.num[0]+=1
    day.to_csv("day.csv",index=False)
    print("done successfully")
    return qrnum


def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        qrnum=id(name,email,phone,password)
        # return render("thanku.html")
        file_location = f'data/2022{qrnum}.png'


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
        donations.to_csv("donation.csv",index=False)
        return render(request,'Thankyou.html')
    return render(request,'donar.html')

def added(request):
    return render(request,"index.png")

