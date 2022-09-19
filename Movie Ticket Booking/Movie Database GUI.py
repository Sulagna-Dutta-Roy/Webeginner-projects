from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql


def book():
    curr_ticket_booked = int(number_of_ticket_entry.get())
    if(customer_name_entry.get() == "" or customer_id_entry.get() == "" or customer_age_entry.get() == "" or movie_select_entry.get() == ""):
            messagebox.showinfo(title='Error',message='Attributes cannot be NULL', icon='error')
    else:
        con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='movie')
        cursor = con.cursor()
        cursor.execute("select ticket_available from movie where mov_id = ('"+movie_select_entry.get()+"')")
        rows = cursor.fetchall()
        temp = str(rows[0])
        ticket_available = int(temp[1:4])
        value =  str(ticket_available - curr_ticket_booked)
        cursor.execute("update movie set ticket_available= '"+ value +"' where mov_id = '"+ movie_select_entry.get()+"'")
        cursor.execute("commit")

        customer_name_entry.delete(0,END)
        customer_id_entry.delete(0,END)
        customer_age_entry.delete(0,END)
        movie_select_entry.delete(0,END)
        number_of_ticket_entry.delete(0,END)

        # self.show(table_content)
        cursor.execute("select * from movie")
        rows = cursor.fetchall()
        table_content.delete(0, table_content.size())
        for row in rows: 
            insertData = "               " + str(row[0]) + "                        " + str(row[1]) + "                        " + str(row[2]) + "            " + str(row[3])
            table_content.insert(table_content.size()+1, insertData)

        messagebox.showinfo(title='Info', message='Booked Successfully!')
        con.close()

window = Tk()
window.title("Movie Ticket Booking")
window.geometry("500x500")
icon = PhotoImage(file="movieIcon.png")
window.iconphoto(True,icon)
window.config(bg='grey')


heading = Label(window,text="MOVIE TICKET BOOKING", font=('System',32), fg="white", bg='grey')
heading.pack()

movie_available = Label(window,text="Movies Available", font=('System', 20), fg='white', bg='grey')
movie_available.pack()

mov_id = Label(window,text="Movie ID", font=('System', 15), fg='white', bg='grey')
mov_id.place(x=25,y=100)

mov_name = Label(window,text="Movie Name", font=('System', 15), fg='white', bg='grey')
mov_name.place(x=370,y=100)

start_time = Label(window,text="Start Time", font=('System', 15), fg='white', bg='grey')
start_time.place(x=120,y=100)

ticket_available = Label(window,text="Tickets Availabe", font=('System', 15), fg='white', bg='grey')
ticket_available.place(x=220,y=100)

table_content = Listbox(window,font=('System', 8),width=81,height=6)
table_content.place(x=5 ,y=130)

con = mysql.connect(host='localhost', user='root', password='nayakarun02', database='movie')
cursor = con.cursor()
cursor.execute("select * from movie")
rows = cursor.fetchall()
table_content.delete(0, table_content.size())
for row in rows: 
    insertData = "               " + str(row[0]) + "                        " + str(row[1]) + "                        " + str(row[2]) + "            " + str(row[3])
    table_content.insert(table_content.size()+1, insertData)

customer_name = Label(window,text='Customer Name',font=('system',12),fg='white',bg='grey')
customer_name.place(x=10,y=250)
customer_name_entry = Entry(window,font=('system',12),fg='white',bg='grey')
customer_name_entry.place(x=150,y=250)

customer_id = Label(window,text='Customer ID',font=('system',12),fg='white',bg='grey')
customer_id.place(x=10,y=280)
customer_id_entry = Entry(window,font=('system',12),fg='white',bg='grey')
customer_id_entry.place(x=150,y=280)

customer_age = Label(window,text='Customer Age',font=('system',12),fg='white',bg='grey')
customer_age.place(x=10,y=310)
customer_age_entry = Entry(window,font=('system',12),fg='white',bg='grey')
customer_age_entry.place(x=150,y=310)

movie_select = Label(window,text='Select Movie ID',font=('system',12),fg='white',bg='grey')
movie_select.place(x=10,y=340)
movie_select_entry = Entry(window,font=('system',12),fg='white',bg='grey')
movie_select_entry.place(x=150,y=340)

number_of_ticket = Label(window,text='Number of Ticket',font=('system',12),fg='white',bg='grey')
number_of_ticket.place(x=8,y=370)
number_of_ticket_entry = Entry(window,font=('system',12),fg='white',bg='grey')
number_of_ticket_entry.place(x=150,y=370)

book_ticket = Button(window,text="Book Ticket",font=('system',12), command= book)
book_ticket.place(x=360,y=290)


window.mainloop()