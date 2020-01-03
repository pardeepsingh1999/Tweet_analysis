from tkinter import *
#import tweepy 
import time
from PIL import ImageTk,Image
from tweet_graph import *
from tkinter import messagebox
import matplotlib.pyplot as plt

zoo=Tk()
zoo.title('Twittes')
#zoo.geometry("750x600")
#zoo.configure(bg='#99ff99')

width = 770
height = 450
screen_width = zoo.winfo_screenwidth()
screen_height = zoo.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
zoo.geometry("%dx%d+%d+%d" % (width, height, x, y))
zoo.resizable(0,0)
zoo.config(bg="#99ff99")


    
canvas = Canvas(zoo,width = 90, height = 80)  
canvas.grid(column=0,row=0,pady=20,padx=20)  
img = ImageTk.PhotoImage(Image.open(r'images\twitter8.jpg'))  
canvas.create_image(1,1, anchor=NW, image=img)

canvas = Canvas(zoo,width = 400, height = 80)  
canvas.grid(column=1,row=0,pady=20,padx=20)  
img1 = ImageTk.PhotoImage(Image.open(r'images\twitter10.jpg'))  
canvas.create_image(1,1, anchor=NW, image=img1)

    

name=Label(zoo,text='Enter Name :',relief=RIDGE,bg='light blue',fg='blue',font = ('times new roman','16'))
name.grid(column=0,row=1,pady=10,padx=10)
#name.pack(pady=10,ipady=5,ipadx=5)
a=Entry(zoo,font=('Times New Roman',16))
a.grid(column=1,row=1,pady=10,padx=10)
#a.pack(ipady=5)

count=Label(zoo,text='Enter Count :',relief=RIDGE,bg='light blue',fg='blue',font = ('times new roman','16'))
count.grid(column=0,row=2,pady=10,padx=10)
#count.pack(pady=10,ipady=5,ipadx=5)
b=Entry(zoo,font=('Times New Roman',16))
b.grid(column=1,row=2,pady=10,padx=10)
#b.pack(ipady=5)

#out=Label()
#out.grid(column=1,row=4,pady=10,padx=10)
#out.pack()

def pie():
            def gettweet():
                    x = a.get()
                    res=[]
                    #res.append(x)
                    res.append(get_tweet_result(x))
        
                    #print(res)
                    return res
            
            res = gettweet()
            #print(res)
            resl=[]
            for r in res:
                for ro in r:
                    w = resl.append(ro)

            print(resl)

            # Data to plot
            labels = 'Positive','Negative','Neutral'
            sizes = resl
            colors = ['gold', 'yellowgreen', 'lightcoral']
            explode = (0.1, 0, 0)  # explode 1st slice
            x = "'",a.get(),"'"
            # Plot
            plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
            plt.title(x)
            plt.axis('equal')
            plt.show()
    
def gettwitt():

        aa=a.get()
        try:
            bb=int(b.get())
        except:
            messagebox.showerror('WARNING!!!','Typecasting mistake only take int value in count box')
        if aa=='' or bb=='':
            messagebox.showerror('WARNING!!!','Blank Input Not Allowed')    
        else:  
            btn1=Button(zoo,text='ANALYSIS',command=pie,bg="#123456",fg="#99ff99",font=('times new roman',14))
            btn1.grid(column=2,row=4,pady=20,padx=20,ipadx=20)

            ck='TL7RyLnfilYH6xaoAlS0XFDCg'
            cs='u5uBn4P62PMIxT4uwUVTl1Ycx4rsfByFs6jl2e4SQ9zDjPIzCO'
            at='919434545924935681-2woCDEXuXQdhJewDaCRBqHBYmi5SFDN'
            ats ='T29jqUm6rZqsRYO7AGc47GlgYTaAaN5OtJD0DATo1uBjh'

            au = OAuthHandler(ck,cs)
            au.set_access_token(at,ats)
            ob = tweepy.API(au)

            ss = int(b.get())
            
            number = ss

            t = ob.search(q=a.get(),count=number)
        
            for r in t:
                try:
                    z = r.text
                    print('==========================')
                    print (z)
                    print('==========================')
                    #print out.configure(text=z)
                    time.sleep(2)
                except:
                    print ('Error')
                    #print out.configure(text='Error')

btn=Button(zoo,text='Submit',command=gettwitt,bg="#123456",fg="#99ff99",font=('times new roman',16))
btn.grid(column=1,row=3,pady=20,padx=20,ipadx=20)

#btn1=Button(zoo,text='ANALYSIS',command=pie,bg="black",fg="yellowgreen",font=('times new roman',14))
#btn1.grid(column=2,row=4,pady=20,padx=20,ipadx=20)
            
btn2=Button(zoo,text='EXIT!!!',command=zoo.destroy,bg="#66ff66",fg="red",font=('times new roman',16))
btn2.grid(column=2,row=5,pady=20,padx=20,ipadx=30)
#btn.pack(ipady=5,ipadx=5)

zoo.mainloop()

