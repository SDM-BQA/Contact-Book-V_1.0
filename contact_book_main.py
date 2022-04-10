from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import re

root = Tk()
root.title("Contact Book")
app_width = 500
app_height = 600

root.iconbitmap(
    'D:/python_Programs/TKINTER/Contact Book/Fasticon-Leopard-Iphone-Users-Folder.ico')
root.resizable(0, 0)
s_width = root.winfo_screenwidth()
s_height = root.winfo_screenheight()

x = (s_width/2) - (app_width/2)
y = (s_height/2) - (app_height/2)

root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

# create the table in database
conn = sqlite3.connect("c_book.db")

# create the cursor
c = conn.cursor()

# # execute
# c.execute('''CREATE TABLE contact_book_table(
#         f_name text,
#         l_name text,
#         phone_no integer,
#         alt_no integer
# )''')


def forget_main_frame():
    main_frame.grid_forget()
    btn_frame.grid_forget()


def forget_search_frame():
    my_tabs.pack_forget()


def search_contact_by_name():

    # Create a new Database and connect
    conn = sqlite3.connect("c_book.db")

    # create the cursor
    c = conn.cursor()
    if name_e.get():

        first_name, last_name = name_e.get().split(" ")
        first_name = first_name.title()
        last_name = last_name.title()

        # execute
        c.execute("SELECT * FROM contact_book_table WHERE f_name = :f_name and  l_name = :l_name",
                  {
                      "f_name": first_name,
                      "l_name": last_name
                  })

        p_rec = ""

        record = c.fetchall()

        if record:
            for r in record:
                p_rec += str(r[0]) + " " + str(r[1]) + "\t" + \
                    str(r[2]) + "\t" + str(r[3]) + "\n"
            show_rec_label.config(text=p_rec)
        else:
            show_rec_label.config(text="No Record Found")
    else:
        show_rec_label.config(text="Please Fill The Field")

    # Commit change
    conn.commit()

    # close the connection
    conn.close()
    name_e.delete(0, END)


def search_contact_by_no():

    # Create a new Database and connect
    conn = sqlite3.connect("c_book.db")

    # create the cursor
    c = conn.cursor()
    if no_e_n.get() != "":
        c.execute("SELECT * FROM contact_book_table WHERE phone_no = :phone_no",
                  {
                      "phone_no": no_e_n.get()
                  })

        p_rec = ""

        record = c.fetchall()

        if record:
            for r in record:
                p_rec += str(r[0]) + " " + str(r[1]) + "\t" + \
                    str(r[2]) + "\t" + str(r[3]) + "\n"
            show_rec_label_n.config(text=p_rec)
        else:
            show_rec_label_n.config(text="No Record Found")

    else:
        show_rec_label_n.config(text="Please Fill the Field")

    # Commit change
    conn.commit()

    # close the connection
    conn.close()

    no_e_n.delete(0, END)


def search_contact_all():
    # Create a new Database and connect
    conn = sqlite3.connect("c_book.db")

    # create the cursor
    c = conn.cursor()

    c.execute("SELECT * FROM contact_book_table")

    p_rec = ""

    record = c.fetchall()

    if record:
        for r in record:
            p_rec += str(r[0]) + " " + str(r[1]) + "\t" + \
                str(r[2]) + "\t" + str(r[3]) + "\n"
        show_rec_label_all.config(text=p_rec)
    else:
        show_rec_label_all.config(text="No Record Found")

    # Commit change
    conn.commit()

    # close the connection
    conn.close()


def phone_no_check(no):
    pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return pattern.match(no)


def add_to_book():
    if f_name_e.get() != "" and l_name_e.get() != "" and contact_no_e.get() != "":

        no = contact_no_e.get()
        if phone_no_check(no):
            # Create a new Database and connect
            conn = sqlite3.connect("c_book.db")

            # create the cursor
            c = conn.cursor()

            # check if phone no already exists
            c.execute("SELECT * FROM contact_book_table WHERE phone_no = :phone_no",
                      {
                          "phone_no": contact_no_e.get()
                      })

            p_rec = ""
            rec = c.fetchall()

            for r in rec:
                p_rec += str(r[0]) + " " + str(r[1])
                # print(r[0])

            if not rec:
                # insert values in the table
                c.execute("INSERT INTO contact_book_table VALUES(:f_name, :l_name, :phone_no, :alt_no)",
                          {
                              "f_name": f_name_e.get().title(),
                              "l_name": l_name_e.get().title(),
                              "phone_no": contact_no_e.get(),
                              "alt_no": alt_no_e.get()
                          })

                f_name_e.delete(0, END)
                l_name_e.delete(0, END)
                contact_no_e.delete(0, END)
                alt_no_e.delete(0, END)

                warn_label.config(text="")

                # show sucessfull task msg
                messagebox.showinfo(
                    "Contact Book", "New Data Has been added\n to the Contact Book")
            else:
                warn_label.config(
                    text="Phone No Already Existed with Name\n" + p_rec)

            # Commit change
            conn.commit()

            # close the connection
            conn.close()

        else:
            warn_label.config(text="Please Enter a Valid Phone Number")
    else:
        warn_label.config(text="Please Fill All * Fields")


def back_func():
    forget_search_frame()
    opening_code()


def del_name_f():
    if name_e_del.get() != "":

        first_name, last_name = name_e_del.get().split(" ")
        # Create a new Database and connect
        conn = sqlite3.connect("c_book.db")

        # create the cursor
        c = conn.cursor()

        c.execute("DELETE from contact_book_table WHERE f_name =:f_name and l_name = :l_name",
                  {
                      "f_name": first_name,
                      "l_name": last_name
                  })
        rec = c.fetchone()

        if rec:
            del_rec_label_name.config(text="No Data Found")
        else:
            del_rec_label_name.config(text="Data Deleted Sucessfully")
        # Commit change
        conn.commit()

        # close the connection
        conn.close()
    else:
        del_rec_label_name.config(text="Plaese Fill The Field")


def del_no_f():
    if no_e_del.get() != "":

        # Create a new Database and connect
        conn = sqlite3.connect("c_book.db")

        # create the cursor
        c = conn.cursor()

        c.execute("DELETE from contact_book_table WHERE phone_no = :phone_no",
                  {
                      "phone_no": no_e_del.get()
                  })

        rec = c.fetchone()

        if not rec:
            del_rec_label_no.config(text="No Data Found")
        else:
            del_rec_label_no.config(text="Data Deleted Sucessfully")
        # Commit change
        conn.commit()

        # close the connection
        conn.close()
    else:
        del_rec_label_no.config(text="Plaese Fill The Field")


def find_func():
    forget_main_frame()

    # create Tab
    global my_tabs
    my_tabs = ttk.Notebook(root, padding=5)
    my_tabs.pack()

    # creating search_frame Name
    global search_frame_name
    search_frame_name = Frame(root, background="White")
    search_frame_name.pack(fill=BOTH, expand=1)

    # creating search_frame No
    global search_frame_no
    search_frame_no = Frame(root, background="White")
    search_frame_no.pack(fill=BOTH, expand=1)

    # creating search_frame All
    global search_frame_all
    search_frame_all = Frame(root, background="White")
    search_frame_all.pack(fill=BOTH, expand=1)

    # creating search_frame All inside
    global search_frame_in
    search_frame_in = Frame(search_frame_all, background="White")
    search_frame_in.pack(fill=BOTH, expand=1)

    # creating delete frame by name
    global del_frame_name
    del_frame_name = Frame(root, background="White")
    del_frame_name.pack(fill=BOTH, expand=1)

    # creating delete frame by no
    global del_frame_no
    del_frame_no = Frame(root, background="White")
    del_frame_no.pack(fill=BOTH, expand=1)

    # adding to tabs
    my_tabs.add(search_frame_name, text="Search By Name")
    my_tabs.add(search_frame_no, text="Search By Number")
    my_tabs.add(search_frame_all, text="Show All Records")
    my_tabs.add(del_frame_name, text="Delete Record")
    my_tabs.add(del_frame_no, text="Delete Record")

    # Main Label
    main_s_label = Label(search_frame_name, text="Search Contact",
                         font=("Times New Roman", 24), fg="yellow", bg="blue")
    main_s_label.grid(row=0, column=0, pady=10, padx=8, columnspan=2)

    # Search by name label and entry
    name_label = Label(search_frame_name, text="Search By Name",
                       font=("Times New Roman", 18), width=14, bg="white")
    name_label.grid(row=1, column=0, padx=15, pady=10)

    global name_e
    name_e = Entry(search_frame_name, font=(
        "Times New Roman", 18), bd=3)
    name_e.grid(row=1, column=1, padx=15, pady=10)

    # creating show record button
    show_btn = Button(search_frame_name, text="Show Records",
                      padx=5, pady=5, font=("Times New Roman", 14), fg="red", bg="yellow", command=search_contact_by_name)
    show_btn.grid(row=2, column=0, pady=(50, 20))

    # creating back to main page btn
    back_btn = Button(search_frame_name, text="Back to Main Page",
                      padx=5, pady=5, font=("Times New Roman", 14), fg="red", bg="yellow", command=back_func)
    back_btn.grid(row=2, column=1, pady=(50, 20))

    # show label
    global show_rec_label
    show_rec_label = Label(search_frame_name, text='', font=(
        "Times New Roman", 16), bg="white", fg="red")
    show_rec_label.grid(row=3, column=0, columnspan=2, pady=20, sticky=W+E)

    ########Create Tab 2###########

    # Main Label
    main_s_label = Label(search_frame_no, text="Search Contact",
                         font=("Times New Roman", 24), fg="yellow", bg="blue")
    main_s_label.grid(row=0, column=0, pady=10, padx=8, columnspan=2)

    # Search by Number label and entry
    no_label_n = Label(search_frame_no, text="Search By \nContact Number",
                       font=("Times New Roman", 18), width=14, bg="white")
    no_label_n.grid(row=1, column=0, padx=15, pady=10, rowspan=2)

    global no_e_n
    no_e_n = Entry(search_frame_no, font=(
        "Times New Roman", 18), bd=3)
    no_e_n.grid(row=1, column=1, padx=15, pady=10, rowspan=2)

    # creating show record button
    show_btn_n = Button(search_frame_no, text="Show Records",
                        padx=5, pady=5, font=("Times New Roman", 14), fg="red", bg="yellow", command=search_contact_by_no)
    show_btn_n.grid(row=3, column=0, pady=(50, 20))

    # creating back to main page btn
    back_btn_n = Button(search_frame_no, text="Back to Main Page",
                        padx=5, pady=5, font=("Times New Roman", 14), fg="red", bg="yellow", command=back_func)
    back_btn_n.grid(row=3, column=1, pady=(50, 20))

    # show label
    global show_rec_label_n
    show_rec_label_n = Label(search_frame_no, text='', font=(
        "Times New Roman", 16), bg="white", fg="red")
    show_rec_label_n.grid(row=4, column=0, columnspan=2, pady=20, sticky=W+E)

    ##### All REC #####
    # Main Label

    main_s_label = Label(search_frame_in, text="Search Contact",
                         font=("Times New Roman", 24), fg="yellow", bg="blue")
    main_s_label.grid(row=0, column=0, padx=20, pady=10, columnspan=2)

    # creating show record button
    show_btn_all = Button(search_frame_in, text="Show Records",
                          padx=5, pady=5, font=("Times New Roman", 14), fg="red", bg="yellow", command=search_contact_all)
    show_btn_all.grid(row=1, column=0, padx=20, pady=(50, 20))

    # creating back to main page btn
    back_btn_all = Button(search_frame_in, text="Back to Main Page",
                          padx=5, pady=5, font=("Times New Roman", 14), fg="red", bg="yellow", command=back_func)
    back_btn_all.grid(row=1, column=1, padx=20, pady=(50, 20))

    # show label
    global show_rec_label_all
    show_rec_label_all = Label(search_frame_in, text='', font=(
        "Times New Roman", 16), bg="white", fg="red")
    show_rec_label_all.grid(row=2, column=0,
                            pady=20, sticky=W+E, columnspan=2)


######################## DELTete RECORd########################

    # Delete record by name

    main_del_label = Label(del_frame_name, text="Delete Contact",
                           font=("Times New Roman", 24), fg="yellow", bg="blue")
    main_del_label.grid(row=0, column=0, pady=10, padx=5, columnspan=2)

    # Search by Number label and entry
    name_label_del = Label(del_frame_name, text="Delete By Name",
                           font=("Times New Roman", 18), width=14, bg="white")
    name_label_del.grid(row=1, column=0, padx=10, pady=10)

    global name_e_del
    name_e_del = Entry(del_frame_name, font=(
        "Times New Roman", 18), bd=3)
    name_e_del.grid(row=1, column=1, padx=10, pady=10)

    # creating show record button
    del_btn_name = Button(del_frame_name, text="Delete  Record",
                          padx=5, pady=5, font=("Times New Roman", 14), fg="red", bg="yellow", command=del_name_f)
    del_btn_name.grid(row=2, column=0, padx=30, pady=(50, 20))

    # creating back to main page btn
    back_btn_del_name = Button(del_frame_name, text="Back to Main Page",
                               padx=5, pady=5, font=("Times New Roman", 14), fg="red", bg="yellow", command=back_func)
    back_btn_del_name.grid(row=2, column=1, padx=30, pady=(50, 20))

    # show label
    global del_rec_label_name
    del_rec_label_name = Label(del_frame_name, text='', font=(
        "Times New Roman", 16), bg="white", fg="red")
    del_rec_label_name.grid(row=3, column=0,
                            pady=20, sticky=W+E, columnspan=2)

    ###################DELete by no######################
# delete record by number
    main_del_label = Label(del_frame_no, text="Delete Contact",
                           font=("Times New Roman", 24), fg="yellow", bg="blue")
    main_del_label.grid(row=0, column=0, pady=10, padx=5, columnspan=2)

    # Search by Number label and entry
    no_label_del = Label(del_frame_no, text="Delete By Number",
                         font=("Times New Roman", 18), width=14, bg="white")
    no_label_del.grid(row=1, column=0, padx=10, pady=10)

    global no_e_del
    no_e_del = Entry(del_frame_no, font=(
        "Times New Roman", 18), bd=3)
    no_e_del.grid(row=1, column=1, padx=10, pady=10)

    # creating show record button
    del_btn_no = Button(del_frame_no, text="Delete  Record",
                        padx=5, pady=5, font=("Times New Roman", 14), fg="red", bg="yellow", command=del_no_f)
    del_btn_no.grid(row=2, column=0, padx=30, pady=(50, 20))

    # creating back to main page btn
    back_btn_del_no = Button(del_frame_no, text="Back to Main Page",
                             padx=5, pady=5, font=("Times New Roman", 14), fg="red", bg="yellow", command=back_func)
    back_btn_del_no.grid(row=2, column=1, padx=30, pady=(50, 20))

    # show label
    global del_rec_label_no
    del_rec_label_no = Label(del_frame_no, text='', font=(
        "Times New Roman", 16), bg="white", fg="red")
    del_rec_label_name.grid(row=3, column=0, columnspan=2,
                            pady=20, sticky=W+E)


def opening_code():
    global main_frame
    main_frame = Frame(root, background="white")
    main_frame.grid(row=0, column=0, columnspan=2, padx=8, pady=(5, 0))

    # create button frame
    global btn_frame
    btn_frame = Frame(root, background="white")
    btn_frame.grid(row=1, column=0, columnspan=2, padx=8, sticky=W+E)

    # Main Label
    main_label = Label(main_frame, text="Contact Book",
                       font=("Times New Roman", 24), fg="yellow", bg="blue")
    main_label.grid(row=0, column=0, pady=(10), padx=8, columnspan=2)

    # first name label and entry
    f_name_label = Label(main_frame, text="First Name *",
                         font=("Times New Roman", 18), width=14, bg="white")
    f_name_label.grid(row=1, column=0, padx=10, pady=10)

    global f_name_e
    f_name_e = Entry(main_frame, font=(
        "Times New Roman", 18), bd=3)
    f_name_e.grid(row=1, column=1, padx=15, pady=10)

    # last name label and entry
    l_name_label = Label(main_frame, text="Last Name *",
                         font=("Times New Roman", 18), width=14, bg="white")
    l_name_label.grid(row=2, column=0, padx=10, pady=10)

    global l_name_e
    l_name_e = Entry(main_frame, font=(
        "Times New Roman", 18), bd=3)
    l_name_e.grid(row=2, column=1, padx=15, pady=10)

    # contact no label and entry
    contact_no_label = Label(main_frame, text="Contact Number *",
                             font=("Times New Roman", 18), width=14, bg="white")
    contact_no_label.grid(row=3, column=0, padx=10, pady=10)

    global contact_no_e
    contact_no_e = Entry(main_frame, font=(
        "Times New Roman", 18), bd=3)
    contact_no_e.grid(row=3, column=1, padx=15, pady=10)

    # alt no label and entry
    alt_no_label = Label(main_frame, text="Alternative No",
                         font=("Times New Roman", 18), width=14, bg="white")
    alt_no_label.grid(row=4, column=0, padx=10, pady=10)

    global alt_no_e
    alt_no_e = Entry(main_frame, font=(
        "Times New Roman", 18), bd=3)
    alt_no_e.grid(row=4, column=1, padx=15, pady=10)

    # adding submit button
    submit_btn = Button(btn_frame, text="Add To Contact",
                        padx=5, pady=5, font=("Times New Roman", 16), fg="red", bg="yellow", command=add_to_book)
    submit_btn.grid(row=0, column=0, padx=50, pady=(50, 25))

    # adding search button
    search_btn = Button(btn_frame, text="Search Contact",
                        padx=5, pady=5, font=("Times New Roman", 16), fg="red", bg="yellow", command=find_func)
    search_btn.grid(row=0, column=1, padx=25, pady=(50, 25))

    # Warning label and entry
    global warn_label
    warn_label = Label(btn_frame, text="",
                       font=("Times New Roman", 18), width=14, bg="white", fg="red")
    warn_label.grid(row=1, column=0, padx=10, pady=(
        10, 0), columnspan=2, sticky=W+E)


# calling main code
opening_code()


# Commit change
conn.commit()

# close the connection
conn.close()
root.mainloop()
