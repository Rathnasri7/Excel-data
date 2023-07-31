import tkinter as tk

# Sample data structure to store employee details
Employee_details = {
    "205": {
        "Name": "Rathnasri",
        
        "Department":"Software engineering",
        "Work location":"Bengaluru",
        "Company name":"Infosys",
        "Salary": 50000,
        "Email":"perumallarathnasri@gmail.com",
        "Phone number":7093081816

    },
    "206": {
        "Name": "Jyothi",
         
        "Department": "Bank manager",
        "Work location":"Vizag",
        "Company name":"State bank",
        "Salary": 45000,
        "Email":"jyothivalavala@gmail.com",
        "Phone number":9948667693
    },
    "207":{
       "Name": "Satya Bindhu",
         
        "Department": "Statistics",
        "Work location":"Hyderabad",
        "Company name":"Accenture",
        "Salary": 35000,
        "Email":"satyabindhu@gmail.com",
        "Phone number": 9701945579
    },
    "208":{
        "Name": "venkanna",
         
        "Department": "Lecture",
        "Work location":"Rajamundry",
        "Company name":"Arts",
        "Salary": 40000,
        "Email":"venkanna@gmail.com",
        "Phone number":8688428933
    },
}

def display_Employee_details():
    Employee_id = entry_id.get()
    if Employee_id in Employee_details:
        details = Employee_details[Employee_id]
        output_label.config(text=f"Name: {details['Name']}\nDepartment: {details['Department']}\nWork location: {details['Work location']}\nCompany name: {details['Company name']}\nSalary: {details['Salary']}\nEmail: {details['Email']}\nPhone number: {details['Phone number']}")
    else:
        output_label.config(text="Employee not found.")

# Create the main application window
root = tk.Tk()
root.title("Employee Details")

# Create input widgets
label_id = tk.Label(root, text="Enter Employee ID:",width=50)
label_id.pack()

entry_id = tk.Entry(root)
entry_id.pack()

submit_button = tk.Button(root, text="Submit", command=display_Employee_details,width=20)
submit_button.pack()

# Create the output label
output_label = tk.Label(root, text="", justify=tk.LEFT)
output_label.pack()

# Start the application event loop
root.mainloop()