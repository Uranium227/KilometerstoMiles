import tkinter as tk

root = tk.Tk()
root.title("Km to Mile")
root.geometry("390x200")
root.resizable(False,False)


km = 3


def calculateMile():
     try:
          mile["text"] = str(float(entry.get())*0.621371192)
          entry.delete(0,"end")
     except:
          mile["text"] = "Please write Number"
          entry.delete(0,"end")


tk.Label(master=root ,text="Kilometers to Mile").place(x=140,y=30)
entry =  tk.Entry(master=root,textvariable="km")
entry.place(x=120,y=100)
tk.Button(master=root,text="Convert",command=calculateMile).place(x=230,y=98)
mile = tk.Label(master=root,text="")
mile.place(x=150,y=150)





root.mainloop()