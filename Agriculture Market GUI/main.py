from cgitb import text
import email
from tkinter import *
from tkinter import messagebox
# from tkinter import PhotoImage
import mysql.connector as mysql

#CROP
class Crop:

    def cropWindow(self):

        cropWindow = Toplevel(window)
        cropWindow.title("Crop")
        cropWindow.geometry("500x500")

        crop_name = Label(cropWindow, text="Crop Name", font=('Sans Serif',12))
        crop_type = Label(cropWindow, text="Type", font=('Sans Serif',12))
        crop_desc = Label(cropWindow, text="Description", font=('Sans Serif', 12))
        exp_date = Label(cropWindow,text="Expiry Date", font=('Sans Serif', 12))

        crop_name.place(x=10,y=20)
        crop_type.place(x=10,y=50)
        crop_desc.place(x=10,y=80)
        exp_date.place(x=10,y=110)

        crop_name_entry = Entry(cropWindow, font=('Sans Serif', 12))
        crop_name_entry.place(x=200,y=20)
        crop_type_entry = Entry(cropWindow, font=('Sans Serif', 12))
        crop_type_entry.place(x=200,y=50)
        crop_desc_entry = Entry(cropWindow, font=('Sans Serif', 12))
        crop_desc_entry.place(x=200,y=80)
        exp_date_entry = Entry(cropWindow, font=('Sans Serif', 12))
        exp_date_entry.place(x=200,y=110)

        crop_insert = Button(cropWindow, text='Insert', font=('Sans Serif', 12), command= lambda: self.insert(exp_date_entry,crop_desc_entry,crop_type_entry,crop_name_entry,table_content))
        crop_insert.place(x=25,y=150)
        crop_delete = Button(cropWindow, text='Delete', font=('Sans Serif', 12), command= lambda: self.delete(exp_date_entry,crop_desc_entry,crop_type_entry,crop_name_entry,table_content))
        crop_delete.place(x=80,y=150)
        crop_update = Button(cropWindow, text='Update', font=('Sans Serif', 12), command= lambda: self.update(exp_date_entry,crop_desc_entry,crop_type_entry,crop_name_entry,table_content))
        crop_update.place(x=145,y=150)

        table_heading = Label(cropWindow, text='Table Content', font=('System',32))
        table_heading.place(x=115 , y=250)
        table_content = Listbox(cropWindow,width=50,height=10)
        table_content.place(x= 100 ,y=300)

        self.show(table_content)


    def insert(self,exp_date_entry,crop_desc_entry,crop_type_entry,crop_name_entry,table_content):
        name = crop_name_entry.get()
        type = crop_type_entry.get()
        desc = crop_desc_entry.get()
        exp_date = exp_date_entry.get()

        if(name == "" or type == "" or desc == "" or exp_date == ""):
            messagebox.showinfo(title='Error',message='Attributes cannot be NULL', icon='error')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("insert into crop values('"+ name +"','"+ type +"','"+ desc +"','"+ exp_date +"')")
            cursor.execute("commit")

            crop_name_entry.delete(0,END)
            crop_type_entry.delete(0,END)
            crop_desc_entry.delete(0,END)
            exp_date_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Values added to table')
            con.close()

    def delete(self,exp_date_entry,crop_desc_entry,crop_type_entry,crop_name_entry,table_content):
        if crop_name_entry.get() == "":
            messagebox.showinfo(title="Info", message='Crop name is compulsory to delete')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("delete from crop where crop_name = '" + crop_name_entry.get() +"'")
            cursor.execute("commit")

            crop_name_entry.delete(0,END)
            crop_type_entry.delete(0,END)
            crop_desc_entry.delete(0,END)
            exp_date_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Deleted Successfully!')
            con.close()

    def update(self,exp_date_entry,crop_desc_entry,crop_type_entry,crop_name_entry,table_content):
        name = crop_name_entry.get()
        type = crop_type_entry.get()
        desc = crop_desc_entry.get()
        exp_date = exp_date_entry.get()

        if(name == "" or type == "" or desc == "" or exp_date == ""):
            messagebox.showinfo(title='Error',message='Attributes cannot be NULL', icon='error')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("update crop set crop_type ='"+ type +"', crop_desc = '" + desc + "', exp_date = '" + exp_date +"' where crop_name = '"+ name +"' ")
            cursor.execute("commit")

            crop_name_entry.delete(0,END)
            crop_type_entry.delete(0,END)
            crop_desc_entry.delete(0,END)
            exp_date_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Updated Successfully!')
            con.close()

    def show(self,table_content):
        con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
        cursor = con.cursor()
        cursor.execute("select * from crop")
        rows = cursor.fetchall()
        table_content.delete(0, table_content.size())
        for row in rows:
            insertData = str(row[0]) + "        " + str(row[1]) + "        " + str(row[2]) + "        " + str(row[3])
            table_content.insert(table_content.size()+1, insertData)

        con.close()

#SUPPLIER
class Supplier:
    def supplierWindow(self):
        supplierWindow = Toplevel(window)
        supplierWindow.title("Supplier")
        supplierWindow.geometry("500x500")

        sup_name = Label(supplierWindow, text="Supplier Name", font=('Sans Serif',12))
        s_id = Label(supplierWindow, text="Supplier ID", font=('Sans Serif',12))
        commission = Label(supplierWindow, text="Commission", font=('Sans Serif', 12))
        phone = Label(supplierWindow,text="Phone", font=('Sans Serif', 12))
        email = Label(supplierWindow,text="Email", font=('Sans Serif', 12))

        sup_name.place(x=10,y=20)
        s_id.place(x=10,y=50)
        commission.place(x=10,y=80)
        phone.place(x=10,y=110)
        email.place(x=10,y=140)

        sup_name_entry = Entry(supplierWindow, font=('Sans Serif', 12))
        sup_name_entry.place(x=200,y=20)
        s_id_entry = Entry(supplierWindow, font=('Sans Serif', 12))
        s_id_entry.place(x=200,y=50)
        commission_entry = Entry(supplierWindow, font=('Sans Serif', 12))
        commission_entry.place(x=200,y=80)
        phone_entry = Entry(supplierWindow, font=('Sans Serif', 12))
        phone_entry.place(x=200,y=110)
        email_entry = Entry(supplierWindow, font=('Sans Serif', 12))
        email_entry.place(x=200,y=140)

        crop_insert = Button(supplierWindow, text='Insert', font=('Sans Serif', 12), command= lambda: self.insert(sup_name_entry,s_id_entry,commission_entry,phone_entry,email_entry,table_content))
        crop_insert.place(x=25,y=200)
        crop_delete = Button(supplierWindow, text='Delete', font=('Sans Serif', 12), command= lambda: self.delete(sup_name_entry,s_id_entry,commission_entry,phone_entry,email_entry,table_content))
        crop_delete.place(x=80,y=200)
        crop_update = Button(supplierWindow, text='Update', font=('Sans Serif', 12), command= lambda: self.update(sup_name_entry,s_id_entry,commission_entry,phone_entry,email_entry,table_content))
        crop_update.place(x=145,y=200)

        table_heading = Label(supplierWindow, text='Table Content', font=('System',32))
        table_heading.place(x=115 , y=250)
        table_content = Listbox(supplierWindow,width=50,height=10)
        table_content.place(x= 100 ,y=300)

        self.show(table_content)

    def insert(self,sup_name_entry,s_id_entry,commission_entry,phone_entry,email_entry,table_content):
        name = sup_name_entry.get()
        sid = s_id_entry.get()
        commission = commission_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()

        if(name == "" or sid == "" or commission == "" or phone == "" or email == ""):
            messagebox.showinfo(title='Error',message='Attributes cannot be NULL', icon='error')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("insert into supplier values('"+ name +"','"+ sid +"','"+ commission +"','"+ phone +"','"+ email +"')")
            cursor.execute("commit")

            sup_name_entry.delete(0,END)
            s_id_entry.delete(0,END)
            commission_entry.delete(0,END)
            phone_entry.delete(0,END)
            email_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Values added to table')
            con.close()

    def delete(self,sup_name_entry,s_id_entry,commission_entry,phone_entry,email_entry,table_content):
        if s_id_entry.get() == "":
            messagebox.showinfo(title="Info", message='Supplier ID is compulsory for deleting')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("delete from supplier where s_id = '" + s_id_entry.get() +"'")
            cursor.execute("commit")

            sup_name_entry.delete(0,END)
            s_id_entry.delete(0,END)
            commission_entry.delete(0,END)
            phone_entry.delete(0,END)
            email_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Deleted Successfully!')
            con.close()

    def update(self,sup_name_entry,s_id_entry,commission_entry,phone_entry,email_entry,table_content):
        name = sup_name_entry.get()
        sid = s_id_entry.get()
        commission = commission_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()

        if(name == "" or sid == "" or commission == "" or phone == "" or email == ""):
            messagebox.showinfo(title='Error',message='Attributes cannot be NULL', icon='error')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("update supplier set sup_name ='"+ name +"', commission = '" + commission + "', phone = '" + phone +"', email = '" + email +"' where s_id = '"+ sid +"' ")
            cursor.execute("commit")

            sup_name_entry.delete(0,END)
            s_id_entry.delete(0,END)
            commission_entry.delete(0,END)
            phone_entry.delete(0,END)
            email_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Updated Successfully!')
            con.close()

    def show(self,table_content):
        con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
        cursor = con.cursor()
        cursor.execute("select * from supplier")
        rows = cursor.fetchall()
        table_content.delete(0, table_content.size())
        for row in rows:
            insertData = str(row[0]) + "        " + str(row[1]) + "        " + str(row[2]) + "        " + str(row[3]) + "        " + str(row[4])
            table_content.insert(table_content.size()+1, insertData)

        con.close()

#FARMER
class Farmer:
    def farmerWindow(self):
        farmerWindow = Toplevel(window)
        farmerWindow.title("Supplier")
        farmerWindow.geometry("500x500")

        farmer_name = Label(farmerWindow, text="Farmer Name", font=('Sans Serif',12))
        f_id = Label(farmerWindow, text="Farmer ID", font=('Sans Serif',12))
        age = Label(farmerWindow, text="Age", font=('Sans Serif', 12))
        phone = Label(farmerWindow,text="Phone", font=('Sans Serif', 12))

        farmer_name.place(x=10,y=20)
        f_id.place(x=10,y=50)
        age.place(x=10,y=80)
        phone.place(x=10,y=110)

        farmer_name_entry = Entry(farmerWindow, font=('Sans Serif', 12))
        farmer_name_entry.place(x=200,y=20)
        f_id_entry = Entry(farmerWindow, font=('Sans Serif', 12))
        f_id_entry.place(x=200,y=50)
        age_entry = Entry(farmerWindow, font=('Sans Serif', 12))
        age_entry.place(x=200,y=80)
        phone_entry = Entry(farmerWindow, font=('Sans Serif', 12))
        phone_entry.place(x=200,y=110)

        crop_insert = Button(farmerWindow, text='Insert', font=('Sans Serif', 12), command= lambda: self.insert(farmer_name_entry,f_id_entry,age_entry,phone_entry,table_content))
        crop_insert.place(x=25,y=200)
        crop_delete = Button(farmerWindow, text='Delete', font=('Sans Serif', 12), command= lambda: self.delete(farmer_name_entry,f_id_entry,age_entry,phone_entry,table_content))
        crop_delete.place(x=80,y=200)
        crop_update = Button(farmerWindow, text='Update', font=('Sans Serif', 12), command= lambda: self.update(farmer_name_entry,f_id_entry,age_entry,phone_entry,table_content))
        crop_update.place(x=145,y=200)

        table_heading = Label(farmerWindow, text='Table Content', font=('System',32))
        table_heading.place(x=115 , y=250)
        table_content = Listbox(farmerWindow,width=50,height=10)
        table_content.place(x= 100 , y=300)

        self.show(table_content)

    def insert(self,farmer_name_entry,f_id_entry,age_entry,phone_entry,table_content):
        name = farmer_name_entry.get()
        f_id = f_id_entry.get()
        age = age_entry.get()
        phone = phone_entry.get()

        if(name == "" or f_id == "" or age == "" or phone == ""):
            messagebox.showinfo(title='Error',message='Attributes cannot be NULL', icon='error')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("insert into farmer values('"+ name +"','"+ f_id +"','"+ age +"','"+ phone +"')")
            cursor.execute("commit")

            farmer_name_entry.delete(0,END)
            f_id_entry.delete(0,END)
            age_entry.delete(0,END)
            phone_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Values added to table')
            con.close()

    def delete(self,farmer_name_entry,f_id_entry,age_entry,phone_entry,table_content):
        if f_id_entry.get() == "":
            messagebox.showinfo(title="Info", message='Farmer ID is compulsory for deleting')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("delete from farmer where f_id = '" + f_id_entry.get() +"'")
            cursor.execute("commit")

            farmer_name_entry.delete(0,END)
            f_id_entry.delete(0,END)
            age_entry.delete(0,END)
            phone_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Deleted Successfully!')
            con.close()

    def update(self,farmer_name_entry,f_id_entry,age_entry,phone_entry,table_content):
        name = farmer_name_entry.get()
        fid = f_id_entry.get()
        age = age_entry.get()
        phone = phone_entry.get()

        if(name == "" or fid == "" or age == "" or phone == ""):
            messagebox.showinfo(title='Error',message='Attributes cannot be NULL', icon='error')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("update farmer set farmer_name ='"+ name +"', age = '" + age + "', phone = '" + phone +"' where f_id = '"+ fid +"' ")
            cursor.execute("commit")

            farmer_name_entry.delete(0,END)
            f_id_entry.delete(0,END)
            age_entry.delete(0,END)
            phone_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Updated Successfully!')
            con.close()

    def show(self,table_content):
        con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
        cursor = con.cursor()
        cursor.execute("select * from farmer")
        rows = cursor.fetchall()
        table_content.delete(0, table_content.size())
        for row in rows:
            insertData = str(row[0]) + "        " + str(row[1]) + "        " + str(row[2]) + "        " + str(row[3])
            table_content.insert(table_content.size()+1, insertData)

        con.close()


#WAREHOUSE
class Warehouse:
    def warehouseWindow(self):
        warehouseWindow = Toplevel(window)
        warehouseWindow.title("Supplier")
        warehouseWindow.geometry("500x500")

        w_id = Label(warehouseWindow, text="Warehouse ID", font=('Sans Serif',12))
        address = Label(warehouseWindow, text="Address", font=('Sans Serif',12))
        max_capacity = Label(warehouseWindow, text="Max Capacity", font=('Sans Serif', 12))
        present_storage = Label(warehouseWindow,text="Present Storage", font=('Sans Serif', 12))

        w_id.place(x=10,y=20)
        address.place(x=10,y=50)
        max_capacity.place(x=10,y=80)
        present_storage.place(x=10,y=110)

        w_id_entry = Entry(warehouseWindow, font=('Sans Serif', 12))
        w_id_entry.place(x=200,y=20)
        address_entry = Entry(warehouseWindow, font=('Sans Serif', 12))
        address_entry.place(x=200,y=50)
        max_capacity_entry = Entry(warehouseWindow, font=('Sans Serif', 12))
        max_capacity_entry.place(x=200,y=80)
        present_storage_entry = Entry(warehouseWindow, font=('Sans Serif', 12))
        present_storage_entry.place(x=200,y=110)

        crop_insert = Button(warehouseWindow, text='Insert', font=('Sans Serif', 12), command= lambda: self.insert(w_id_entry,address_entry,max_capacity_entry,present_storage_entry,table_content))
        crop_insert.place(x=25,y=200)
        crop_delete = Button(warehouseWindow, text='Delete', font=('Sans Serif', 12), command= lambda: self.delete(w_id_entry,address_entry,max_capacity_entry,present_storage_entry,table_content))
        crop_delete.place(x=80,y=200)
        crop_update = Button(warehouseWindow, text='Update', font=('Sans Serif', 12), command= lambda: self.update(w_id_entry,address_entry,max_capacity_entry,present_storage_entry,table_content))
        crop_update.place(x=145,y=200)

        table_heading = Label(warehouseWindow, text='Table Content', font=('System',32))
        table_heading.place(x=115 , y=250)
        table_content = Listbox(warehouseWindow,width=50,height=10)
        table_content.place(x= 100 , y=300)

        self.show(table_content)

    def insert(self,w_id_entry,address_entry,max_capacity_entry,present_storage_entry,table_content):
        w_id = w_id_entry.get()
        address = address_entry.get()
        max_capacity = max_capacity_entry.get()
        present_storage = present_storage_entry.get()

        if(w_id == "" or address == "" or max_capacity == "" or present_storage == ""):
            messagebox.showinfo(title='Error',message='Attributes cannot be NULL', icon='error')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("insert into warehouse values('"+ w_id +"','"+ address +"','"+ max_capacity +"','"+ present_storage +"')")
            cursor.execute("commit")

            w_id_entry.delete(0,END)
            address_entry.delete(0,END)
            max_capacity_entry.delete(0,END)
            present_storage_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Values added to table')
            con.close()

    def delete(self,w_id_entry,address_entry,max_capacity_entry,present_storage_entry,table_content):
        if w_id_entry.get() == "":
            messagebox.showinfo(title="Info", message='Farmer ID is compulsory for deleting')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("delete from warehouse where w_id = '" + w_id_entry.get() +"'")
            cursor.execute("commit")

            w_id_entry.delete(0,END)
            address_entry.delete(0,END)
            max_capacity_entry.delete(0,END)
            present_storage_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Deleted Successfully!')
            con.close()

    def update(self,w_id_entry,address_entry,max_capacity_entry,present_storage_entry,table_content):
        w_id = w_id_entry.get()
        address = address_entry.get()
        max_capacity = max_capacity_entry.get()
        present_storage = present_storage_entry.get()

        if(w_id == "" or address == "" or max_capacity == "" or present_storage == ""):
            messagebox.showinfo(title='Error',message='Attributes cannot be NULL', icon='error')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("update warehouse set address ='"+ address +"', max_capacity = '" + max_capacity + "', present_storage = '" + present_storage +"' where w_id = '"+ w_id +"' ")
            cursor.execute("commit")

            w_id_entry.delete(0,END)
            address_entry.delete(0,END)
            max_capacity_entry.delete(0,END)
            present_storage_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Updated Successfully!')
            con.close()

    def show(self,table_content):
        con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
        cursor = con.cursor()
        cursor.execute("select * from warehouse")
        rows = cursor.fetchall()
        table_content.delete(0, table_content.size())
        for row in rows:
            insertData = str(row[0]) + "        " + str(row[1]) + "        " + str(row[2]) + "        " + str(row[3])
            table_content.insert(table_content.size()+1, insertData)

        con.close()

#PAYMENT
class Payment:
    def paymentWindow(self):
        paymentWindow = Toplevel(window)
        paymentWindow.title("Supplier")
        paymentWindow.geometry("500x500")

        p_id = Label(paymentWindow, text="Payment ID", font=('Sans Serif',12))
        amount = Label(paymentWindow, text="Amount", font=('Sans Serif',12))
        discount = Label(paymentWindow, text="Discount", font=('Sans Serif', 12))
        tax = Label(paymentWindow,text="Tax", font=('Sans Serif', 12))
        mode_of_payment = Label(paymentWindow,text="Mode of Payment", font=('Sans Serif', 12))
        cust_id = Label(paymentWindow,text="Customer ID", font=('Sans Serif', 12))

        p_id.place(x=10,y=20)
        amount.place(x=10,y=50)
        discount.place(x=10,y=80)
        tax.place(x=10,y=110)
        mode_of_payment.place(x=10,y=140)
        cust_id.place(x=10,y=170)

        p_id_entry = Entry(paymentWindow, font=('Sans Serif', 12))
        p_id_entry.place(x=200,y=20)
        amount_entry = Entry(paymentWindow, font=('Sans Serif', 12))
        amount_entry.place(x=200,y=50)
        discount_entry = Entry(paymentWindow, font=('Sans Serif', 12))
        discount_entry.place(x=200,y=80)
        tax_entry = Entry(paymentWindow, font=('Sans Serif', 12))
        tax_entry.place(x=200,y=110)
        mode_of_payment_entry = Entry(paymentWindow, font=('Sans Serif', 12))
        mode_of_payment_entry.place(x=200,y=140)
        cust_id_entry = Entry(paymentWindow, font=('Sans Serif', 12))
        cust_id_entry.place(x=200,y=170)

        crop_insert = Button(paymentWindow, text='Insert', font=('Sans Serif', 12), command= lambda: self.insert(p_id_entry,amount_entry,discount_entry,tax_entry,mode_of_payment_entry,cust_id_entry,table_content))
        crop_insert.place(x=25,y=200)
        crop_delete = Button(paymentWindow, text='Delete', font=('Sans Serif', 12), command= lambda: self.delete(p_id_entry,amount_entry,discount_entry,tax_entry,mode_of_payment_entry,cust_id_entry,table_content))
        crop_delete.place(x=80,y=200)
        crop_update = Button(paymentWindow, text='Update', font=('Sans Serif', 12), command= lambda: self.update(p_id_entry,amount_entry,discount_entry,tax_entry,mode_of_payment_entry,cust_id_entry,table_content))
        crop_update.place(x=145,y=200)

        table_heading = Label(paymentWindow, text='Table Content', font=('System',32))
        table_heading.place(x=115 , y=250)
        table_content = Listbox(paymentWindow,width=50,height=10)
        table_content.place(x= 100 , y=300)

        self.show(table_content)

    def insert(self,p_id_entry,amount_entry,discount_entry,tax_entry,mode_of_payment_entry,cust_id_entry,table_content):
        p_id = p_id_entry.get()
        amount = amount_entry.get()
        discount = discount_entry.get()
        tax = tax_entry.get()
        mode_of_payment = mode_of_payment_entry.get()
        cust_id = cust_id_entry.get()

        if(p_id == "" or amount == "" or discount == "" or tax == "" or mode_of_payment == "" or cust_id == ""):
            messagebox.showinfo(title='Error',message='Attributes cannot be NULL', icon='error')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("insert into payment values('"+ p_id +"','"+ amount +"','"+ discount +"','"+ tax +"','"+ mode_of_payment +"','"+ cust_id +"')")
            cursor.execute("commit")

            p_id_entry.delete(0,END)
            amount_entry.delete(0,END)
            discount_entry.delete(0,END)
            tax_entry.delete(0,END)
            mode_of_payment_entry.delete(0,END)
            cust_id_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Values added to table')
            con.close()

    def delete(self,p_id_entry,amount_entry,discount_entry,tax_entry,mode_of_payment_entry,cust_id_entry,table_content):
        if p_id_entry.get() == "":
            messagebox.showinfo(title="Info", message='Payment ID is compulsory for deleting')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("delete from payment where p_id = '" + p_id_entry.get() +"'")
            cursor.execute("commit")

            p_id_entry.delete(0,END)
            amount_entry.delete(0,END)
            discount_entry.delete(0,END)
            tax_entry.delete(0,END)
            mode_of_payment_entry.delete(0,END)
            cust_id_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Deleted Successfully!')
            con.close()

    def update(self,p_id_entry,amount_entry,discount_entry,tax_entry,mode_of_payment_entry,cust_id_entry,table_content):
        p_id = p_id_entry.get()
        amount = amount_entry.get()
        discount = discount_entry.get()
        tax = tax_entry.get()
        mode_of_payment = mode_of_payment_entry.get()
        cust_id = cust_id_entry.get()

        if(p_id == "" or amount == "" or discount == "" or tax == "" or mode_of_payment == "" or cust_id == ""):
            messagebox.showinfo(title='Error',message='Attributes cannot be NULL', icon='error')
        else:
            con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
            cursor = con.cursor()
            cursor.execute("update payment set amount ='"+ amount +"', discount = '" + discount + "', tax = '" + tax +"', mode_of_payment = '" + mode_of_payment +"', cust_id = '" + cust_id +"' where p_id = '"+ p_id +"' ")
            cursor.execute("commit")

            p_id_entry.delete(0,END)
            amount_entry.delete(0,END)
            discount_entry.delete(0,END)
            tax_entry.delete(0,END)
            mode_of_payment_entry.delete(0,END)
            cust_id_entry.delete(0,END)

            self.show(table_content)

            messagebox.showinfo(title='Info', message='Updated Successfully!')
            con.close()

    def show(self,table_content):
        con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='agriculture')
        cursor = con.cursor()
        cursor.execute("select * from payment")
        rows = cursor.fetchall()
        table_content.delete(0, table_content.size())
        for row in rows:
            insertData = str(row[0]) + "        " + str(row[1]) + "        " + str(row[2]) + "        " + str(row[3]) + "        " + str(row[4]) + "        " + str(row[5])
            table_content.insert(table_content.size()+1, insertData)

        con.close()


if __name__ == "__main__":
    #Main
    window = Tk()
    window.config(bg='#97F0A5')
    window.geometry("500x500") #dimension of main window
    window.title("Wholesale Market Dealer (Agriculture)") #title of window
    # icon = PhotoImage(file="CropIcon.png") #tiny icon of window
    # window.iconphoto(True,icon)

    tables = Label(window,text="Tables Available", font=('System',32), fg="Purple", bg='#97F0A5')
    tables.pack()

    c = Crop()
    c = Button(window, text="Crop Table", font=('System',16), bg='#97F0A5', activebackground='#5F9668', command=c.cropWindow)
    c.place(x=30,y=70)

    s = Supplier()
    s = Button(window, text="Supplier Table", font=('System',16), bg='#97F0A5', activebackground='#5F9668', command=s.supplierWindow)
    s.place(x=150, y=70)

    f = Farmer()
    f = Button(window, text="Farmer Table", font=('System',16), bg='#97F0A5', activebackground='#5F9668', command=f.farmerWindow)
    f.place(x=300, y=70)

    w = Warehouse()
    w = Button(window, text="Warehouse Table", font=('System',16), bg='#97F0A5', activebackground='#5F9668', command=w.warehouseWindow)
    w.place(x=30, y=140)

    p = Payment()
    p = Button(window, text="Payment Table", font=('System',16), bg='#97F0A5', activebackground='#5F9668', command=p.paymentWindow)
    p.place(x=190, y=140)

    window.mainloop()