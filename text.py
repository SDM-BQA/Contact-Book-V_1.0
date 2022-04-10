
global search_frame
search_frame = Frame(root, background="White")
search_frame.pack(fill=BOTH, expand=1)

# btn frame
global btn_s_frame
btn_s_frame = Frame(root, background="white")
btn_s_frame.pack(row=1, column=0, columnspan=2,
                 padx=8, sticky=W+E)

# Show Frame
global show_frame
show_frame = Frame(root, background="white")
show_frame.grid(row=2, column=0, columnspan=2,
                padx=8, sticky=W+E)

# Main Label
main_s_label = Label(search_frame, text="Search Contact",
                     font=("Times New Roman", 24), fg="yellow", bg="blue")
main_s_label.grid(row=0, column=0, pady=10, padx=8, columnspan=2)

# Search by name label and entry
name_label = Label(search_frame, text="Search By Name",
                   font=("Times New Roman", 18), width=14, bg="white")
name_label.grid(row=1, column=0, padx=10, pady=10)

global name_e
name_e = Entry(search_frame, font=(
    "Times New Roman", 18), bd=3)
name_e.grid(row=1, column=1, padx=15, pady=10)

# Search by Number label and entry
no_label = Label(search_frame, text="Search By \nContact Number",
                 font=("Times New Roman", 18), width=14, bg="white")
no_label.grid(row=2, column=0, padx=10, pady=10, rowspan=2)

global no_e
no_e = Entry(search_frame, font=(
    "Times New Roman", 18), bd=3)
no_e.grid(row=2, column=1, padx=15, pady=10, rowspan=2)

# creating show record button
show_btn = Button(btn_s_frame, text="Show Records",
                  padx=5, pady=5, font=("Times New Roman", 16), fg="red", bg="yellow", command=search_contact_f)
show_btn.grid(row=0, column=0, padx=50, pady=50)

# creating back to main page btn
back_btn = Button(btn_s_frame, text="Back to Main Page",
                  padx=5, pady=5, font=("Times New Roman", 16), fg="red", bg="yellow", command=back_func)
back_btn.grid(row=0, column=1, padx=25, pady=50)

# show label
global show_rec_label
show_rec_label = Label(btn_s_frame, text='', font=(
    "Times New Roman", 16), bg="white", fg="red")
show_rec_label.grid(row=1, column=0, columnspan=2, pady=20, sticky=W+E)
