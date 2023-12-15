from tkinter import *
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv 
from selenium.webdriver.common.keys import Keys
from datetime import datetime
# Main Tkinter window
ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#f25252')
def convert_to_list_format(data, indent=""):
    result = []
    for item in data:
        label = item["label"]
        text = item["text"]
        result.append(f"{indent}{text}")

        if "|" in label:
            # Recursive call for sub-items
            sub_items = convert_to_list_format(
                [sub_item for sub_item in data if sub_item["label"].startswith(label + "|")],
                indent + "|   "
            )
            result.extend(sub_items)

    return result

def load_json(filename):
    try:
        with open(filename) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def on_entry_change(event):
    value = entry.get().lower()
    filtered_options = [option for option in options if value in option.lower()]
    update_listbox(filtered_options)

def on_listbox_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_option = listbox.get(selected_index[0])
        entry.delete(0, END)
        entry.insert(0, selected_option)

def update_listbox(filtered_options):
    listbox.delete(0, END)
    for option in filtered_options:
        listbox.insert(END, option)

def on_ok_button_click():
    selected_value = ''
    selected_value = entry.get()
    if selected_value:
        print(f"Selected Value: {selected_value}")
        # Add your code here to handle the selected value
    return selected_value



def stop_app():
    ws.destroy()
stop_duration = 5000
def open_website():
    Username = 0
    Email = 1
    URL = 2

    with open('data.csv', 'r') as csv_file:

        csv_reader = csv.reader(csv_file)
        next(csv_reader)

    #-------------------------------------------------------------------------------
    # Web Automation

        for line in csv_reader:


            driver = webdriver.Firefox()
            driver.get('http://www.1abc.org/submit.php')
            driver.maximize_window()
            time.sleep(5)

            regular_links = driver.find_element("xpath", '/html/body/div/div/table/tbody/tr/td/form/table[1]/tbody/tr/td/table/tbody/tr[4]/td[1]/input')
            regular_links.click()
            time.sleep(5)

            Title_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[1]/td[2]/input')
            Title_field.send_keys(line[3])
            time.sleep(3)

            URL_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/input')
            URL_field.send_keys(line[2])
            time.sleep(3)

            Description_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[3]/td[2]/textarea')
            Description_field.send_keys(line[4])
            time.sleep(3)

            username_field = driver.find_element("xpath",'//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[4]/td[2]/input')
            username_field.send_keys(line[0])
            time.sleep(3)

            Email_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[5]/td[2]/input')
            Email_field.send_keys(line[1])
            time.sleep(3)


            element = driver.find_elements(By.NAME, 'CATEGORY_ID')
            print('ok')
            drp = Select(element[0])
            # selected_option = combobox.get()  # Get the selected option from the combobox
            # drp.select_by_visible_text(selected_option)
            selected_option =on_ok_button_click()
            drp.select_by_visible_text(selected_option)
            time.sleep(4)


            submit = driver.find_elements(By.XPATH, '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[8]/td[2]/input')
            submit[0].click()


            driver.quit()
            ws.after(stop_duration, stop_app)

# # Main Tkinter window
# # ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('400x300')
# ws.config(bg='#f25252')

# Frame
frame = Frame(ws, bg='#f25252')
frame.pack(expand=True)

# Label
Label(
    frame,
    bg='#f25252',
    font=('Times', 21),
    text='Select the category '
).pack()

# Entry for searching
entry = Entry(
    frame,
    font=('Times', 18),
)
entry.pack()

# Listbox for displaying filtered options
listbox = Listbox(frame, font=('Times', 18), selectmode=SINGLE)
listbox.pack()

# Load options from JSON
options = convert_to_list_format(load_json('output.json'))

# Link the Entry widget to update the Listbox values on text change
entry.bind('<KeyRelease>', on_entry_change)

# Link the Listbox widget to update the Entry on selection
listbox.bind('<<ListboxSelect>>', on_listbox_select)

# OK Button
ok_button = Button(frame, text="Select", command=on_ok_button_click)
ok_button.pack()
button = Button(frame, text="Open Website", command=open_website)
button.pack()
# Run Tkinter main loop
ws.mainloop()














