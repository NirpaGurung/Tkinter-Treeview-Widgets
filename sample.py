#import tkinter and ttk module
from tkinter import*
from tkinter import ttk

root = Tk()
root.title("Tree View")

#create Treeview widgets
tree = ttk.Treeview(root, columns = ("Name", "Age"))
"""
This line creates a treeview widget inside the root window.
The columns parameter specifies the columns that will be displayed in the treeview.
In this case, it will have two columns: "Name" and "Age".
"""

#Set treeview column heading
tree.column("#0", width = 80)
"""
This line sets the width of the first column of the treeview to 80 pixels.
The #0 represents the index of the first column,
which is usually reserved for the item identifiers.
"""
tree.column("Name", width=80)
tree.column("Age", width=80)
"""
This line sets the width of the "Name" and "Age" column of the treeview to 80 pixels.
"""

tree.heading("#0", text="Student Code")
"""
This line sets the heading text of the first column (with index #0) to "Student Code".
"""
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

#insert values into treeview widgets
tree.insert("", "end", text="201.0012", values = ("Karma",24))
tree.insert("", "end", text="201.0013", values = ("Sonam",23))
tree.insert("", "end", text="201.0014", values = ("Dorji",20))
"""
This line inserts an item into the treeview.
The empty string "" as the first argument means that the item will be inserted at the top level.
"end" specifies that the item will be inserted at the end of the list of items.
text="201.0012" sets the identifier of the item.
values=("Karma", 24) sets the values for the "Name" and "Age" columns respectively.
""""
tree.pack()
root.mainloop()
