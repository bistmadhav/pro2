from tkinter import *
import sqlite3

root = TK()

conn = sqlite3.connect("")

c= conn.cursor()



root.title( ' Welcome to Car Rental')
root.geometry("900x950")

main_Add_new_cust = Button(root, text ="Add New Customer")
main_Add_new_cust.pack(pady = 12)

main_Add_new_Vehicle = Button(root, text ="Add New Vehicle")
main_Add_new_Vehicle.pack(pady = 12)

main_Search_rental_Car = Button(root, text ="Search Rental Car")
main_Search_rental_Car.pack(pady = 12)

main_Return_Car = Button(root, text ="Return Car") 
main_Return_Car.pack(pady = 12)

main_Search_Customer = Button(root, text ="Search Customer") 
main_Search_Customer.pack(pady = 12)

main_Search_Vehicle = Button(root, text ="Search Customer") 
main_Search_Vehicle.pack(pady = 12)



def ADD_New_Customer()
    cursor.execute(Insert into CUSTOMER)
    {

        'NAME':name.get()
        'PHONE':phone.get()
    })

customer_name = Entry(ADD_New_Customer, width = 30)
customer_name.grid(row =0, column =0 )

customer_phome =Entry(ADD_New_Customer, width = 30) 
customer_phone.grid(row =1, column =0 )

customer_name_l = Label(ADD_New_Customer, text="Customer Name")
customer_name_l.grid(row =0, column =0 )
customer_phome =Label(ADD_New_Customer, text ="Customer Phone") 
customer_phone.grid(row =1, column =0 )

def ADD_Vehicle()
    cursor.execute(Insert into Vehicle)
    {

        'VIN': get()
        'DESCRIPTION':get()
        'YEAR':get()
        'CATAGORY':get()



    })

ADD_vin = Entry(ADD_Vehicle, width = 30)
ADD_vin.grid(row =0, column =0 )

ADD_desc = Entry(ADD_Vehicle, width = 30)
ADD_desc.grid(row =1, column =0 )

ADD_year = Entry(ADD_Vehicle, width = 30)
ADD_year.grid(row =2, column =0 )

DD_type = Entry(ADD_Vehicle, width = 30)
ADD_type.grid(row =2, column =0 )


ADD_cata = Entry(ADD_Vehicle, width = 30)
ADD_cata.grid(row =3, column =0 )


customer_vin_l = Label(ADD_Vehicle, text="VIN")
customer_vin_l.grid(row =0, column =0 )

customer_desc_l = Label(ADD_Vehicle, text="DESCRIPTIOM")
customer_desc_l.grid(row =1, column =0 )

customer_YEAR_l = Label(ADD_Vehicle, text="YEAR")
customer_YEAR_l.grid(row =2, column =0 )

customer_TYPE_l = Label(ADD_Vehicle, text="TYPE")
customer_TYPE_l.grid(row =3, column =0 )

customer__CATl = Label(ADD_Vehicle, text="CATAGORY")
customer_CATl.grid(row =4, column =0 )

customer_vin_l = Label(ADD_Vehicle, text="submit")
customer_vin_l.grid(row =5, column =0 , padx =8)



def ADD_rental_info()
    {
        'Vehicle':get()
        'Order Date':get()
        'Return Date';get()
  

    })



ADD_vehi = Entry(ADD_rental_info, width = 30)
ADD_vehi.grid(row =0, column =0 )

ADD_order = Entry(ADD_rental_info, width = 30)
ADD_order.grid(row =1, column =0 )


ADD_return = Entry(ADD_rental_info, width = 30)
ADD_return.grid(row =2, column =0 )


add_vehi = Label(ADD_rental_info, text="Vehicle")
add_vehi.grid(row =0, column =0 )

add_order = Label(ADD_rental_info, text="Order Date")
add_order.grid(row =1, column =0 )

add_ret = Label(ADD_rental_info, text="Return Date")
add_ret.grid(row =2, column =0 )

add_find = Label(ADD_rental_info, text="Click here to find")
add_find.grid(row =3, column =0 , padex = 8)




def search_re_hist()
    {
       'Order Date':get()
       'Enter Name': get()
       'VIN_Number':get()


    })

rental_order = Entry(search_re_hist, width = 30)
rental_order.grid(row =0, column =0 )

rental_name = Entry(search_re_hist, width = 30)
rental_name.grid(row =1, column =0 )

rental_vin = Entry(search_re_hist, width = 30)
rental_vin.grid(row =2, column =0 )

rental_retrive = Entry(search_re_hist, width = 30)
rental_retrive.grid(row =3, column =0 )



search_order = Label(search_re_hist, text="Order Date")
search_order.grid(row =0, column =0 )

search_name = Label(search_re_hist, text="Enter Name")
search_name.grid(row =1, column =0 )


search_vinu = Label(search_re_hist, text="VIN_Number")
search_vinu.grid(row =2, column =0 )


search_vinu = Label(search_re_hist, text="Retrive")
search_vinu.grid(row =3, column =0, padex = 10 )










