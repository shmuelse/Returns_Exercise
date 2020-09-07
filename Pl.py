import BL
import Utiles

# from tkinter import Tk, Button, Label, Entry, Listbox, MULTIPLE
input_str = ("To add a customer press 1\n"
             "To add a driver press 2\n"
             "To add a van press 3\n"
             "to add a consignment press 4\n"
             "for exit please press 0")


def add_to_db(val):
    while val != 0:
        if val == 1:
            f_name = input('first name')
            l_name = input('last name')
            p_number = Utiles.is_correct_phone_num(input('phone number'))
            e_address = Utiles.is_email_correct(input('email address'))
            address = input('address')
            BL.add_new_customer(f_name, l_name, e_address, p_number, address)
            val = input(input_str)
        elif val == 2:
            f_name = input('first name')
            l_name = input('last name')
            p_number = Utiles.is_correct_phone_num(input('phone number'))
            e_address = Utiles.is_email_correct(input('email address'))
            branch = input('branch')
            BL.add_new_driver(f_name, l_name, p_number, e_address, branch)
            val = input(input_str)
        elif val == 3:
            geo_area = input('geo_area')
            branch = input('branch')
            BL.add_new_van(geo_area, branch)
            val = input(input_str)
        elif val == 4:
            customer_id = input('customer id')
            BL.add_new_consignment(customer_id)
            val = input(input_str)


print("Welcome To Ldt Global returns system")
add_to_db(int(input(input_str)))


# main_panel = Tk()
# main_panel.title('Ldt Returns system')
# main_panel.geometry("750x500")
# main_panel.iconbitmap('ITD-logo-1.ico')
# main_panel.resizable(False, False)
#
# select_van_btn = Button(main_panel, text="consignment position on which van").place(x=520, y=20)
# show_map = Button(main_panel, text="Show map to destination").place(x=520, y=50)
#
# lbl_1 = Label(main_panel, text="consignment ID").place(x=400, y=20)
# ent_1 = Entry(main_panel, width=20).place(x=300, y=20)
#
#
# lstbox = Listbox(main_panel, selectmode=MULTIPLE)
#
#
#
# main_panel.mainloop()
