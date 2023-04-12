import tkinter as tk


def calculate_tax():
    """
    Calculates the tax based on the user's input and displays the result
    """
    try:
        income1 = float(income1_entry.get())
        income2 = float(income2_entry.get() or 0)
        married = bool(married_var.get())
        mpf_1 = float(cal_self_mpf(income1))
        mpf_2 = float(cal_self_mpf(income2))
        selftax1 = float(selftax(income1,mpf_1))
        spousetax1 =float(spousetax(income2, mpf_2))
        mixtax = float(mix_tax(selftax1, spousetax1))
        standard1 = float(calculate_standard_tax_amount(income1,income2,mpf_1,mpf_2)) 
        tax = calculate_tax_amount(income1,income2,married)
        total_tax = calculate_total_tax_amount(income1,income2,married)
        tax_label.config(text=f"Joint Tax: ${tax:.2f}")
        total_tax_label.config(text=f"Seperate Tax: ${total_tax:.2f}")
        self_mpf_label.config(text=f"Self Mpf: ${mpf_1:.2f}")
        spouse_mpf_label.config(text=f"Spouse Mpf: ${mpf_2:.2f}")
        tax_label_15.config(text=f"Standard Tax: ${standard1:.2f}")
        self_label.config(text=f"self: ${selftax1:.2f}")
        spouse_label.config(text=f"spouse: ${spousetax1:.2f}")
        mix_tax_label.config(text=f"mix: ${mixtax:.2f}")
    except ValueError:
        tax_label.config(text="Invalid input. Please enter a number.")

def calculate_standard_tax_amount(income1,income2,mpf_1,mpf_2):
    standard = (income1 +  income2 - mpf_1 - mpf_2)*0.15
    return standard

def cal_self_mpf(income1):
    mpf_1 = income1 *0.05
    if mpf_1 >18000:
        mpf_1 = 18000
        return mpf_1
    elif income1/12 < 7001:
        mpf_1 = 0
        return mpf_1
    else:
        return mpf_1

def cal_spouse_mpf(income2):
    mpf_2 = income2 *0.05
    if mpf_2 >18000:
        mpf_2 = 18000
        return mpf_2
    elif income2/12 < 7100:
        mpf_2 = 0
        return mpf_2   
    else: 
        mpf_2 = 0
        return mpf_2



def selftax(income1,mpf_1):
    income = income1 
    income1 = income1 -132000 -mpf_1
    if income1 <= 50000:
        selftax = income1 * 0.02
    elif income1 <= 100000:
        selftax = 1000 + (income1 - 50000) * 0.06
    elif income1 <= 150000:
        selftax = 4000 + (income1 - 100000) * 0.10
    elif income1 <= 200000:
        selftax = 9000 + (income1 - 150000) * 0.14
    elif income1 <= 0:
        selftax = 0
    else:
        selftax = 16000 + (income1 - 200000) * 0.17   
    stanincome1 = (income-mpf_1)*0.15
    if stanincome1 < selftax:
        return stanincome1
    else:
        return selftax

def spousetax(income2,mpf_2):
    income = income2 
    income2 = income2 -132000 -mpf_2
    if income2 <= 50000:
        spousetax = income2 * 0.02
    elif income2 <= 100000:
        spousetax = 1000 + (income2 - 50000) * 0.06
    elif income2 <= 150000:
        spousetax = 4000 + (income2 - 100000) * 0.10
    elif income2 <= 200000:
        spousetax = 9000 + (income2 - 150000) * 0.14
    elif income2 <= 0:
        spousetax = 0
    else:
        spousetax = 16000 + (income2 - 200000) * 0.17   
   
    stanincome2 = (income-mpf_2)*0.15
    if stanincome2 < spousetax:
        return stanincome2
    else:
        return spousetax

def calculate_tax_amount(income1,income2,married):
    """
    Calculates the tax for a given taxable_income
    """
    mpf_1 = income1 *0.05
    if mpf_1 >18000:
        mpf_1 = 18000
       
    mpf_2 = income2 *0.05
    if mpf_2 >18000:
        mpf_2 = 18000
    if married:
        
        taxable_income = income1 + income2 -mpf_1 -mpf_2 - 264000
    else:
        taxable_income = income1 -mpf_1 -132000
    if taxable_income < 0:
        taxable_income = 0
    if taxable_income <= 50000:
        tax = taxable_income * 0.02
    elif taxable_income <= 100000:
        tax = 1000 + (taxable_income - 50000) * 0.06
    elif taxable_income <= 150000:
        tax = 4000 + (taxable_income - 100000) * 0.10
    elif taxable_income <= 200000:
        tax = 9000 + (taxable_income - 150000) * 0.14
    else:
        tax = 16000 + (taxable_income - 200000) * 0.17
    return tax

def calculate_total_tax_amount(income1,income2,married):
    """
    Calculates the tax for a given income
    """
    mpf_1 = income1 *0.05
    if mpf_1 >18000:
        mpf_1 = 18000
        
    mpf_2 = income2 *0.05
    if mpf_2 >18000:
        mpf_2 = 18000
    income1 = income1 -mpf_1 -132000
    income2 = income2 -mpf_2 -132000
    if income1 < 0:
        income1 = 0
    if income2 < 0:
        income2 = 0
    if married:  
        if income1 <= 50000:
            tax1 = income1 * 0.02
        elif income1 <= 100000:
            tax1 = 1000 + (income1 - 50000) * 0.06
        elif income1 <= 150000:
            tax1 = 4000 + (income1 - 100000) * 0.10
        elif income1 <= 200000:
            tax1 = 9000 + (income1 - 150000) * 0.14
        else:
            tax1 = 16000 + (income1 - 200000) * 0.17    
        if income2 <= 50000:
            tax2 = income2 * 0.02
        elif income2 <= 100000:
                tax2 = 1000 + (income2- 50000) * 0.06
        elif income2 <= 150000:
            tax2 = 4000 + (income2 - 100000) * 0.10
        elif income2 <= 200000:
            tax2 = 9000 + (income2 - 150000) * 0.14
        else:
            tax2 = 16000 + (income2 - 200000) * 0.17
        return tax1 + tax2
    else:
        if income1 <= 50000:
            tax1 = income1 * 0.02
        elif income1 <= 100000:
            tax1 = 1000 + (income1 - 50000) * 0.06
        elif income1 <= 150000:
            tax1 = 4000 + (income1 - 100000) * 0.10
        elif income1 <= 200000:
            tax1 = 9000 + (income1 - 150000) * 0.14
        else:
            tax1 = 16000 + (income1 - 200000) * 0.17
        return tax1

def mix_tax(spouse1, selftax1):
    if spouse1 <0:
        spouse1 = 0
    if selftax1 <0:
        selftax1 =0
    mix = selftax1 + spouse1 
    return mix


# Create the main window
root = tk.Tk()
root.title("Tax Calculator (Hong Kong)")

# Create the income label and entry
income1_label = tk.Label(root, text="Self Annual Income:")
income1_label.grid(column=0, row=0, sticky= tk.W)

income1_entry = tk.Entry(root)
income1_entry.grid(column=1, row=0)

income2_label = tk.Label(root, text="Spouse Annual Income:")
income2_label.grid(column=0, row=1)

income2_entry = tk.Entry(root)
income2_entry.grid(column=1, row=1)

# Create the marital status label and radio buttons
married_label = tk.Label(root, text="Married:")
married_label.grid(column=0, row=2)

married_var = tk.BooleanVar()
married_var.set(False)

married_yes = tk.Radiobutton(root, text="Yes", variable=married_var, value=True)
married_yes.grid(column=1, row=2)

married_no = tk.Radiobutton(root, text="No", variable=married_var, value=False)
married_no.grid(column=2, row=2)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_tax)
calculate_button.grid(row=8, column=3, sticky= tk.W)

# Create the tax label
tax_label = tk.Label(root, text="Joint Tax: $0.00")
tax_label.grid(row=3, column=0, columnspan=2)

total_tax_label = tk.Label(root, text="Seperate Tax: $0.00")
total_tax_label.grid(row=3, column=2, columnspan=2)

self_mpf_label = tk.Label(root, text="Self MPF: $0.00")
self_mpf_label.grid(row=4,column=0, columnspan=2)

spouse_mpf_label = tk.Label(root, text="Spouse MPF: $0.00")
spouse_mpf_label.grid(row=4,column=2, columnspan=2)

# 15% tax
tax_label_15 = tk.Label(root, text="Standard Tax: $0.00")
tax_label_15.grid(row=5, column=0,  columnspan=2)

self_label = tk.Label(root, text="Self : ")
self_label.grid(row=6, column=0, columnspan=2)

spouse_label = tk.Label(root, text="Spouse : ")
spouse_label.grid(row=6, column=2, columnspan=2)

mix_tax_label = tk.Label(root, text="Mix :")
mix_tax_label.grid(row=7, column=0, columnspan=2)

# Run the main loop
root.mainloop()
