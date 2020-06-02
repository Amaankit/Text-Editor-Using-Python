from tkinter import scrolledtext#STARTing Comment added
from tkinter import filedialog,messagebox
import datetime
import os
import webbrowser
class TextEditor:
    current_file="nothing"
    c=0
    def __init__(self,root):
    
        self.root=root
        #self.root.withdraw()
        self.root.title("Untitled -TextEditor")
        self.root.bind('<Control-Shift-U>',self.upper1)
        self.root.bind('<Control-Shift-L>',self.low1)
        self.root.bind('<Control-Shift-T>',self.title_case)
        self.root.bind('<Control-Shift-W>',self.swapcase)
        self.root.bind('<Control-Shift-S>',self.save_as)
        self.root.bind('<Control-s>',self.save)
        self.root.bind('<Control-n>',self.new)
        self.root.bind('<Control-o>',self.open)
        self.root.bind('<Alt-F4>',self.exit)
        self.root.bind('<F12>',self.HELP)
        self.root.bind('<Escape>',self.exit)
        self.root.bind('<Control-d>',self.date)
        scrolledtext.scrollbar=Scrollbar(self.root)
        scrolledtext.scrollbar.pack(side=RIGHT,fill=Y)
        self.text_area=Text(wrap=WORD,selectbackground="red",yscrollcommand=scrolledtext.scrollbar.set,undo=True,padx="10px")
        self.text_area.pack(fill=BOTH,expand=1)
        self.main_menu=Menu(self.root)
        self.root.config(menu=self.main_menu)
        self.file_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="File",menu=self.file_menu)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="New       Ctrl+N",command=self.new)
        self.file_menu.add_command(label="Open     Ctrl+O",command=self.open)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save as  Ctrl+Shift+S",command=self.save_as)
        self.file_menu.add_command(label="Save       Ctrl+S",command=self.save)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",command=self.exit)
        self.edit_menu=Menu(self.main_menu,tearoff=False)
        self.edit_menu.add_command(label="Undo              Ctrl+Z",command=self.undo)
        self.edit_menu.add_command(label="Redo               Ctrl+Y",command=self.redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut                  Ctrl+X",command=self.cut)
        self.edit_menu.add_command(label="Copy               Ctrl+C",command=self.copy)
        self.edit_menu.add_command(label="Paste               Ctrl+V",command=self.paste)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Delete               Del",command=self.delete)
        self.edit_menu.add_command(label="Date                 Ctrl+D",command=self.date)
        self.edit_menu.add_command(label="Date/Time      Ctrl+T",command=self.date_time)
        self.main_menu.add_cascade(label="Edit",menu=self.edit_menu)
        self.format_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Format",menu=self.format_menu)
        self.format_menu.add_command(label="UpperCase   Ctrl+Shift+U",command=self.upper1)
        self.format_menu.add_command(label="LowerCase   Ctrl+Shift+L",command=self.low1)
        self.format_menu.add_command(label="TitleCase      Ctrl+Shift+T",command=self.title_case)
        self.format_menu.add_command(label="SwapCase    Ctrl+Shift+W",command=self.swapcase)
        self.font_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Font",menu=self.font_menu)
        #helvetica=IntVar() 
        #courier=IntVar()
        self.font_menu.add_command(label="Courier", command=self.FontCourier)
        self.font_menu.add_command(label="Helvetica",command=self.FontHelvetica)
        self.font_menu.add_command(label="Modern",command=self.FontModern)
        self.font_menu.add_command(label="Roman",command=self.FontRoman)
        self.font_menu.add_command(label="Aparajita",command=self.FontScript)
        self.font_menu.add_command(label="Arabic",command=self.FontArabic)
        self.font_menu.add_command(label="Times New Roman",command=self.FontTimes_New_Roman)
        self.font_menu.add_command(label="Nyala",command=self.FontNyala)
        self.font_menu.add_command(label="Verdana",command=self.FontVerdana)
        self.font_menu.add_command(label="Kokila",command=self.FontWebdings)
        self.font_menu.add_command(label="Bookman Old Style",command=self.FontBookman)
        self.font_menu.add_command(label="Book Antiqua",command=self.FontBook_Antiqua)
        self.font_menu.add_command(label="Calibri",command=self.FontCalibri)
        self.about_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="About",menu=self.about_menu)
        self.about_menu.add_command(label="About TextEditor",command=self.ABOUT)
        self.help_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Help",menu=self.help_menu)
        self.help_menu.add_command(label="Help     F12",command=self.HELP)
        self.root.protocol("WM_DELETE_WINDOW",self.exit)
    def open(self,event=""):
            filedata=filedialog.askopenfile(initialdir="/",parent=root,title="Select File To Open",filetypes=(("text files","*.txt"),("all files","*.*")))
            if filedata !=None:
                self.root.title((filedata.name)+" -TextEditor")
                self.text_area.delete(1.0,END)
            for line in filedata: 
                self.text_area.insert(END,line)
            self.current_file=filedata.name
            print(self.current_file)
               # print(line)    
    def save_as(self,event=""):
        self.file_data=self.text_area.get('1.0',END+"-1c")
        if self.file_data!="":
        
            filehnd=filedialog.asksaveasfile(initialdir="/",title="SAVE",mode="w",defaultextension=".txt",filetypes=(("text files","*.txt"),("all files","*.*")))
            #  print(filehnd)
            if filehnd !=None:
                self.root.title((filehnd.name)+" -TextEditor")
                self.file_data=self.text_area.get('1.0',END+"-1c")
                filehnd.write(self.file_data)
                self.current_file=filehnd.name
                #print(self.current_file)
                filehnd.close()
        else:
            messagebox.showinfo("Empty File","File is Empty")
            
    def save(self,event=""):
        if self.current_file=="nothing":
            self.save_as()
        else:
            f=open(self.current_file,"w")
            self.data=self.text_area.get(1.0,END)
            f.write(self.data)
            f.close()
            #print("hi")
    def new(self,event=""):
        if (self.text_area.get('1.0',END+'-1c')!=""):
            if messagebox.askokcancel("Text Editor","Do you want to save file"):
                self.save()
                global c
                c=1
                self.text_area.delete(1.0,END)
            else:
                self.text_area.delete(1.0,END)
                c=1
            self.current_file="nothing"
            self.root.title("Untitled -TextEditor")
        else:
            pass
    def exit(self,event=""):
        global c
        if self.current_file=="nothing":
            if messagebox.askokcancel("SAVE?","Do you want to save this file"):
                self.save()
                self.root.destroy()
                if c==1:
                    c=0
                    self.root.destroy()
            else:
                self.root.destroy()
        else:
            if messagebox.askokcancel("SAVE CHANGES?","Do you want to save changes"):
                self.save()
                #print("hi")
                self.root.destroy()
            else:
                self.root.destroy()
            
    def copy(self):
        try:
            self.text_area.clipboard_clear()
            self.text_area.clipboard_append(self.text_area.selection_get())
        except:
            pass
    def cut(self):
        try:
            self.copy()
            self.text_area.delete("sel.first","sel.last")
        except:
            pass
    def paste(self):
        try:
            self.text_area.insert(INSERT,self.text_area.clipboard_get())
            pass
        except:
            pass
    def delete(self):
        try:
            self.text_area.delete("sel.first","sel.last")
        except:
            pass
    def undo(self):
        try:
            self.text_area.edit_undo()
            print("0")
        except:
            pass
    def redo(self,event=""):
        try:
            self.text_area.edit_redo()
        except:
            pass
    def upper1(self,event=""):
        try:
            data=self.text_area.selection_get()
            self.pos=self.text_area.index("sel.first")
            #print(self.pos)
            self.text_area.delete("sel.first","sel.last")
            data=data.upper()
            self.text_area.insert(self.pos,data)
        except:
            pass
    def low1(self,event=""):
        try:
            data=self.text_area.selection_get()
            self.pos=self.text_area.index("sel.first")
            #print(self.pos)
            self.text_area.delete("sel.first","sel.last")
            data=data.lower()
            self.text_area.insert(self.pos,data)
        except:
            pass
    def swapcase(self,event=""):
        try:
            data=self.text_area.selection_get()
            self.pos=self.text_area.index("sel.first")
            #print(self.pos)
            self.text_area.delete("sel.first","sel.last")
            data=data.swapcase()
            self.text_area.insert(self.pos,data)
        except:
            pass
    def title_case(self,event=""):
        try:
            data=self.text_area.selection_get()
            self.pos=self.text_area.index("sel.first")
            #print(self.pos)
            self.text_area.delete("sel.first","sel.last")
            data=data.title()
            self.text_area.insert(self.pos,data)
        except:
            pass
    def FontHelvetica(self):
        '''self.text_area.selection_get().config(font="Helvetica")
        self.pos=self.text_area.index("sel.first")
        #print(self.pos)
        self.text_area.delete("sel.first","sel.last")'''
        self.text_area.config(font="Helvetica"'''fontsize='15''')
        #self.text_area.insert(self.pos,data)
        
    def FontCalibri(self):
        self.text_area.config(font="Calibri")

    def FontCourier(self):
        self.text_area.config(font="Courier")
    def FontModern(self):
        self.text_area.config(font="Modern")
 
    def FontRoman(self):
        self.text_area.config(font="Roman")

    def FontScript(self):
        self.text_area.config(font="Aparajita")

    def FontArabic(self):
        self.text_area.config(font="Arabic")

    def FontTimes_New_Roman(self):
        self.text_area.config(font="Times_New_Roman")

    def FontNyala(self):
        self.text_area.config(font="Nyala")

    def FontVerdana(self):
        self.text_area.config(font="Verdana")

    def FontWebdings(self):
        self.text_area.config(font="Kokila")

    def FontBookman(self):
        self.text_area.config(font="'Bookman_Old_Style'")

    def FontBook_Antiqua(self):
        self.text_area.config(font="Book_Antiqua")
    def date(self,event=""):
        self.date_object = datetime.date.today()
        self.text_area.insert(INSERT,self.date_object)
    def date_time(self,event=""):
        self.datetime_object = datetime.datetime.now()
        self.text_area.insert(INSERT,self.datetime_object)
    def HELP(self,event=""):
        self.url="file:///D:/pythonp/gui/text_editor_help.html"
        new=2
        webbrowser.open(self.url,new=new)
    def ABOUT(self):
        #pass

        
        from PIL import  Image,ImageTk
        #tkinter.NoDefaultRoot()
        self.win1=Tk()
        self.win1.configure(background="white")
        self.win1.geometry("700x400")
        self.win1.title("About")
        self.win1.resizable(0,0)
        #image = Image.open('about.jpg')
        #photoimage = ImageTk.PhotoImage(image)
        #Label(self.win1, image=photoimage).place(x=30, y=10)
        self.widget=Label(self.win1, text="TEXT EDITOR")
        self.widget.place(x=165, y=40)
        labelfont = ('times', 30, 'bold')
        self.widget.config(font=labelfont)    
        self.widget.config(bg='white', fg='blue')         
        self.widget.config(height=3, width=20)       

        self.widget1=Label(self.win1, text="____________________________________________________________________________________________________________________________________________________________________________________________")
        self.widget1.place(x=0, y=160)
        self.labelfont = ('times', 10, 'bold')
        self.widget1.config(font=labelfont) 
        self.widget1.config(bg='white')      

        self.widget2=Label(self.win1, text=" Version 1.1.0")
        self.widget2.place(x=0, y=180)
        labelfont = ('times', 20, 'bold')
        self.widget2.config(font=labelfont)    
        self.widget2.config(bg='white', fg='black')   




        self.widget4=Label(self.win1, text="\nCopyright @ 2019 MOHD AMAAN .All rights reserved.")
        self.widget4.place(x=0, y=210)
        labelfont = ('times', 20, 'bold')
        self.widget4.config(font=labelfont)    
        self.widget4.config(bg='white', fg='black')    
   
        self.widget3=Label(self.win1, text=" Language Used - Python      ")
        self.widget3.place(x=0, y=287)
        labelfont = ('times', 20, 'bold')
        self.widget3.config(font=labelfont)    
        self.widget3.config(bg='white', fg='black')     



        self.widget5=Label(self.win1, text="Module Used-tkinter,os,messagebox.")
        self.widget5.place(x=0, y=325)
        labelfont = ('times', 20, 'bold')
        self.widget5.config(font=labelfont)    
        self.widget5.config(bg='white', fg='black')     

        self.win1.mainloop()
            
       
from tkinter import *
import tkinter
from PIL import  Image,ImageTk
root=Tk()
root.title("TEXT EDITOR")
t=TextEditor(root)
root.mainloop()
