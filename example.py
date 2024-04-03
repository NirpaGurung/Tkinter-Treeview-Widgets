from tkinter import*
from tkinter import ttk

root = Tk()
root.title("Treeview")

#create a treeview widgets
tree =ttk.Treeview(root, columns = ("Name", "Class"))

#set the column heading
tree.column("#0", width=70)
tree.column("Name", width=70)
tree.column("Class", width=70)

tree.heading("#0", text = "Students code")
tree.heading("Name", text = "Name")
tree.heading("Class", text = "Class")

#insert the values in the treeview
tree.insert("","end",text="201.0001", values = ("Karma", "19"))
tree.insert("","end",text="201.0002", values = ("Dorji", "17"))
tree.insert("","end",text="201.0003", values = ("Singye", "20"))
tree.insert("","end",text="201.0004", values = ("Nado", "18"))

tree.pack()
root.mainloop()
