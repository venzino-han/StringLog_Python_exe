#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
from tkinter.ttk import *
from re import findall

class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
 
        self.master = master
        self.master.title("String Log 생성")
        self.pack(fill=BOTH, expand=True)
        
        
        frame1 = Frame(self)
        frame1.pack(fill=X)
        lblIntro0 = Label(frame1,text="사용법" ,width=12)
        lblIntro0.pack(side=LEFT, padx=10, pady=10)
        
        lblIntro1 = Label(frame1,text="1. 모듈명 입력\n2. String 번호 입력\n3. [생성]버튼 클릭" ,width=20)
        lblIntro1.pack(side=LEFT, padx=10, pady=10)
 
        # 모듈
        frame2 = Frame(self)
        frame2.pack(fill=X)
 
        lblModule = Label(frame2, text="Module", width=12)
        lblModule.pack(side=LEFT, padx=10, pady=10)
        
        #변수정의
        self.moduleName = StringVar()
        entryModule = Entry(frame2, text = self.moduleName)
        entryModule.pack(fill=X, padx=10, expand=True)
        
        
        
        # string num
        frame3 = Frame(self)
        frame3.pack(fill=X)
 
        lblString = Label(frame3, text="String Numbers", width=12)
        lblString.pack(side=LEFT, padx=10, pady=10)
        
        #변수정의
        self.inputNumbers = StringVar()
        entryString = Entry(frame3, text = self.inputNumbers)
        entryString.pack(fill=X, padx=10, expand=True)
 
        # log
        frame4 = Frame(self)
        frame4.pack(fill=BOTH, expand=True)
 
        lblLog = Label(frame4, text="Log output", width=12)
        lblLog .pack(side=LEFT, anchor=N, padx=10, pady=10)
        
        #self.logtext = StringVar()
        #txtLog  = Text(frame3, text = self.logtext)
        self.txtLog  = Text(frame4)
        self.txtLog .pack(fill=X, pady=10, padx=10)
 
        # 생성
        frame5 = Frame(self)
        frame5.pack(fill=X)
        btnCreate = Button(frame5, text="생성", command=self.Click_btn)
        btnCreate.pack(side=LEFT, padx=10, pady=10)
        
        
        
        
    def Click_btn(self):
        module = self.moduleName.get()
        raw_num =  re.findall("\d",self.inputNumbers.get())
        
        count = len(raw_num)//4
        count = str(count)
        result = "*"+ module +" String 추가 ("+ count +"건)\n"
        
        for i in range(0,len(raw_num)):
            if (i+1)%40 == 0 :
                result = result + raw_num[i] +"\n"

            elif (i+1)%4 == 0 :
                result = result + raw_num[i] +" "

            else :
                result = result + raw_num[i]
                
        self.txtLog.insert(1.0,result)
        #print("log")

def main():
    root = Tk()
    root.geometry("600x550+100+100")
    app = MyFrame(root)
    root.mainloop()
 
if __name__ == '__main__':
    main()


# In[ ]:




