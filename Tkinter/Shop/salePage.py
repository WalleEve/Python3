from tkinter import *
from tkinter import ttk
import sqlite3
from sqlite3 import Error
import os
import sys
from datetime import date

import mystoreTables as mydb



class Sales:
	# This is a Sales page Class
	def __init__(self, master):
		self.master = master

		# Frame:
		self.sFrame = Frame(master, bg="azure4")
		self.sFrame.place(x=1, y=1, height=120, width=270 )


		# Variable
		self.mfont = ("Arial", 12)

		self.item = StringVar()
		self.qty = StringVar()
		self.price = StringVar()

		self.searchEntry = StringVar()

		self.discClicked = StringVar()
		self.gstClicked = StringVar()

		self.current_date = date.today()


		# summaryFrame Variables
		self.totalItem = StringVar()
		self.totalAmount = StringVar()
		self.totalGst = StringVar()
		self.totalDisc = StringVar()
		self.totaPayable = StringVar()
		self.totalPaid = StringVar()


		# SQLITE CONNECTIONS:
		self.base_path = os.path.dirname( os.path.abspath(__file__))
		self.config_path = os.path.join(self.base_path, "mystoredb.db")
		try:
			self.conn = sqlite3.connect(self.config_path)
			print(sqlite3.version)
		except Error as e:
			print(e)

	def btnAdd(self):
		item = self.item.get()
		qty = self.qty.get()
		price = self.price.get()
		max_tid = 0
		self.conn = sqlite3.connect(self.config_path)
		cursor = self.conn.cursor()

		sql = """
		SELECT max(tid) from current_transaction
		"""
		cursor.execute(sql)
		max_tid = cursor.fetchone()
		max_tid = max_tid[0]
		print(max_tid)
		if max_tid =='' or max_tid == None :
			max_tid = 0



		sql = """
		INSERT INTO current_transaction VALUES(?,?,?,?,?)
		"""
		print(max_tid)
		cursor.execute(sql, (max_tid+1, self.current_date,item, qty, price, ))
		self.conn.commit()

	def table_conn(self, table_name):
		self.conn = sqlite3.connect(self.config_path)
		cursor = self.conn.cursor()
		sql = "select * from " + table_name
		cursor.execute(sql)
		rows = cursor.fetchall()
		return rows
		"""
        if len(rows) !=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END, values=row)
            conn.commit()
        conn.close()"""

	def fetch_data(self):
		pass
		"""
		tableData = self.table_conn(current_transaction)
		if len(tableData) !=0:
			self.Sales_Table.delete(*self.Sales_Table.get_children()
			for row in tableData:
				self.Sales_Table.insert('',END, values=row)
			self.conn.commit()
			self.conn.close()"""



	def saleFrame(self, master):
		#mfont = self.mfont
		#sFrame = Frame(master, bg="Blue")
		#sFrame.place(x=1, y=1, height=120, width=270 )
		sFrame = self.sFrame

		Label(sFrame, text="Item", font=self.mfont, bg="azure4").grid(row=0, column=0, padx=2, pady=2, sticky=W)
		Label(sFrame, text="Quantity", font=self.mfont, bg="azure4").grid(row=1, column=0, padx=2, pady=2, sticky=W)
		Label(sFrame, text="Price", font=self.mfont, bg="azure4").grid(row=2, column=0, padx=2, pady=2, sticky=W)
		itemEntry = Entry(sFrame, textvariable = self.item, width=20, font= self.mfont)
		itemEntry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
		qtyEntry = Entry(sFrame, textvariable = self.qty, width=20, font=self.mfont)
		qtyEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
		priceEntry = Entry(sFrame, textvariable = self.price, width=20, font=self.mfont)
		priceEntry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

	def Badd(self):
		item = self.item.get()
		qty = self.qty.get()
		price = self.price.get()
		print(item, qty, price)

	def buttonFrame(self, master):
		bFrame = Frame(master, bg="azure4", relief=GROOVE)
		bFrame.place(x=1, y=125, height=35, width=270)

		addBtn = Button(bFrame, text="add", width=6, font=self.mfont, command = self.btnAdd)
		addBtn.grid(row=0, column=0, padx=2, pady=2, sticky=W)
		self.fetch_data()
		self.conn.close()
		addBtn = Button(bFrame, text="update", width=6, font=self.mfont)
		addBtn.grid(row=0, column=1, padx=2, pady=2, sticky=W)
		addBtn = Button(bFrame, text="clear", width=6, font=self.mfont)
		addBtn.grid(row=0, column=2, padx=2, pady=2, sticky=W)
		addBtn = Button(bFrame, text="delete", width=6, font=self.mfont)
		addBtn.grid(row=0, column=3, padx=2, pady=2, sticky=W)

	def summaryFrame(self, master):
		smFrame = LabelFrame(master, bg="azure4", relief=GROOVE, text="Summary")
		smFrame.place(x=1, y=165, height=230, width=270)
		"""
		gstOptions = [0, '8%', '10%', '12%', '18%']
		discOptions = [0, '5%', '10%', '12%', '15%', '20%']
		self.discClicked.set(0)
		self.gstClicked.set(0)
		OptionMenu( smFrame , self.gstClicked , *gstOptions ).grid(row=2, column=1, padx=2, pady=2, sticky=W)
		OptionMenu( smFrame , self.discClicked , *discOptions ).grid(row=3, column=1, padx=2, pady=2, sticky=W)
		"""
		Label(smFrame, text="Total Item: ", bg="azure4").grid(row=0, column=0, padx=2, pady=0, sticky=W)
		Label(smFrame, text="Total Amount: ", bg="azure4").grid(row=1, column=0, padx=2, pady=0, sticky=W)
		Label(smFrame, text="Gst: ", bg="azure4").grid(row=2, column=0, padx=2, pady=0, sticky=W)
		Label(smFrame, text="Discount: ", bg="azure4").grid(row=3, column=0, padx=2, pady=0, sticky=W)
		Label(smFrame, text="Payable: ", bg="azure4").grid(row=4, column=0, padx=2, pady=0, sticky=W)
		Label(smFrame, text="Paid: ", bg="azure4").grid(row=5, column=0, padx=2, pady=0, sticky=W)

		self.itemEntry = Entry(smFrame, textvariable = self.totalItem, font=("Arial", 10), width=20, state=DISABLED).grid(row=0, column=1, padx=2, pady=2, sticky=W)
		self.amtEntry = Entry(smFrame, textvariable = self.totalAmount, font=("Arial", 10), width=20, state=DISABLED).grid(row=1, column=1, padx=2, pady=2, sticky=W)
		self.gstEntry = Entry(smFrame, textvariable = self.totalGst, font=("Arial", 10), width=20, state=DISABLED).grid(row=2, column=1, padx=2, pady=2, sticky=W)
		self.discEntry = Entry(smFrame, textvariable = self.totalDisc, font=("Arial", 10), width=20, state=DISABLED).grid(row=3, column=1, padx=2, pady=2, sticky=W)
		self.payEntry = Entry(smFrame, textvariable = self.totaPayable, font=("Arial", 10), width=20, state=DISABLED).grid(row=4, column=1, padx=2, pady=2, sticky=W)
		self.paidEntry = Entry(smFrame, textvariable = self.totalPaid, font=("Arial", 10), width=20).grid(row=5, column=1, padx=2, pady=2, sticky=W)

		Button(smFrame, text="Pay", font=("Arial", 10), width=26).grid(row=6, columnspan=3, padx=20, pady=20)

	def searchFrame(self, master):
		sFrame = Frame(master, bg="azure4", relief=GROOVE)
		sFrame.place(x=275, y=1, height=35, width=370)

		Label(sFrame, text="Item", font=("Arial", 11), bg='azure4').grid(row=0, column=0, padx=2, pady=2, sticky=W)
		Entry(sFrame, font=("Arial", 11), width=20, textvariable=self.searchEntry).grid(row=0, column=1, padx=2, pady=2, sticky=W)
		Button(sFrame, text="Search", font=("Arial", 10), width=7).grid(row=0, column=2, padx=2, pady=2, sticky=W)
		Button(sFrame, text="Bill", font=("Arial", 10), width=9).grid(row=0, column=3, padx=2, pady=2, sticky=W)


	def table_Frame(self, master):

		table_Frame = LabelFrame(master, bg="azure4", relief=GROOVE, text="Details")
		table_Frame.place(x=275, y=40, height=355, width=370)
		scroll_x = Scrollbar(table_Frame, orient=HORIZONTAL)
		scroll_y = Scrollbar(table_Frame, orient=VERTICAL)

		# Add a Treeview widget
		#tree = ttk.Treeview(table_Frame, column=("Item", "Quantity", "Price"), show='headings', height=5)

		self.Sales_Table = ttk.Treeview(table_Frame, columns=("Item", "Quantity", "Price"),  show='headings', height=5, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM, fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_x.config(command=self.Sales_Table.xview)
		scroll_y.config(command=self.Sales_Table.yview)
		self.Sales_Table.heading("Item", text="Item")
		self.Sales_Table.heading("Quantity", text="Quantity")
		self.Sales_Table.heading("Price", text="Price")
		self.Sales_Table.column("Item", width=100)
		self.Sales_Table.column("Quantity", width=50)
		self.Sales_Table.column("Price", width=50)
		self.Sales_Table.pack(fill=BOTH, expand=1)















def mainSale():
	root = Tk()
	root.title("My Shop")
	root.geometry("650x400")
	s = Sales(root)
	s.saleFrame(root)
	s.buttonFrame(root)
	s.summaryFrame(root)
	s.searchFrame(root)
	s.table_Frame(root)

	root.mainloop()

if __name__ == "__main__":
	mainSale()
