import BL
from tkinter import Tk, Button, Label, Entry, Listbox

main_panel = Tk()
main_panel.title('Ldt Returns system')
main_panel.geometry("750x500")
main_panel.iconbitmap('ITD-logo-1.ico')
main_panel.resizable(False, False)


select_van_btn = Button(main_panel, text="consignment position on which van").place(x=520, y=20)
show_map = Button(main_panel, text="Show map to destination").place(x=520, y=50)

lbl_1 = Label(main_panel, text="consignment ID").place(x=500, y=20)


main_panel.mainloop()
