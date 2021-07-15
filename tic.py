from tkinter import *  #IMPORT LIBRARY
from tkinter import messagebox
import array

root=Tk() #a window or GUI is created associated with root
root.title('Tic Tac Toe Game')  #title of the window

"""root.iconbitmap('/Users/saketdhakar/Desktop/straw_hat.ico')""" #sets a icon to the root window
turn=True
cnt=0
arr=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


#disable all buttons
def disable_button():
    for i in range(9):
        a[i]["state"]="disabled"

#check if won
def checkifwon():
    if cnt==9:
        messagebox.showinfo("Tic Tac Toe","Its a tie")
        disable_button()
        return
    
    for i in arr:
        sum=0;
        for j in i:
            if a[j]['text']=='X':
                sum+=1
        if sum == 3:
            for j in i:
                a[j].config(highlightbackground='red')
            messagebox.showinfo("Tic Tac Toe","X wins")
            disable_button()
            return
            
    for i in arr:
        sum=0;
        for j in i:
            if a[j]['text']=='O':
                sum+=1
        if sum == 3:
            for j in i:
                a[j].config(highlightbackground='red')
            messagebox.showinfo("Tic Tac Toe","O wins")
            disable_button()
            return

#button click
def click(a):
    global turn,cnt

    if a["text"]== " " and turn == True:
        a["text"]="X"; turn=False; cnt+=1; checkifwon()
        

    elif a["text"]==" " and turn == False:
         a["text"]="O"; turn=True; cnt+=1; checkifwon()
         
    else:
        messagebox.showerror("Tic Tac Toe","Button already clicked")
#define reset
def reset():
    global a,turn,cnt
    turn=True;cnt=0;
    a[0]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[0]))
    a[1]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[1]))
    a[2]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[2]))

    a[3]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[3]))
    a[4]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[4]))
    a[5]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[5]))

    a[6]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[6]))
    a[7]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[7]))
    a[8]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[8]))
    
    a[0].grid(row=0,column=0);a[1].grid(row=0,column=1);a[2].grid(row=0,column=2);
    a[3].grid(row=1,column=0);a[4].grid(row=1,column=1);a[5].grid(row=1,column=2);
    a[6].grid(row=2,column=0);a[7].grid(row=2,column=1);a[8].grid(row=2,column=2);



#build buttons
a=[None]*9
a[0]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[0]))
a[1]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[1]))
a[2]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[2]))

a[3]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[3]))
a[4]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[4]))
a[5]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[5]))

a[6]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[6]))
a[7]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[7]))
a[8]=Button(root,text=" ",height=5,width=5,highlightbackground='#3E4149',command=lambda:click(a[8]))

reset_button=Button(root,text="reset",highlightbackground="black",command=lambda:reset())

#grid buttons
a[0].grid(row=0,column=0);a[1].grid(row=0,column=1);a[2].grid(row=0,column=2);
a[3].grid(row=1,column=0);a[4].grid(row=1,column=1);a[5].grid(row=1,column=2);
a[6].grid(row=2,column=0);a[7].grid(row=2,column=1);a[8].grid(row=2,column=2);
reset_button.grid(row=3)











root.mainloop() #activates the window