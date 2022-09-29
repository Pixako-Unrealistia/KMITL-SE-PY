quote = ["employee's name:", "hours worked in a week:", "hourly pay rate:", 
          "federal tax withholding rate:", "state tax witholding rate:"]

A = input(f"Enter {quote[0]} ")

for x in range(1,5):
    temp = chr(x + 65)
    exec(f'{temp} = float(input("Enter {quote[x]} "))')

GP = B * C
FW = GP * D
SW = GP * E

print(f"""
Employee Name: {A}
Hours Worked: {B}
Pay Rate: ${C}
Gross Pay: ${B * C}
Deductions:
      Federal Withholding({D}%) : ${FW:.2f}
      State Withholding({E}%) : ${SW:.2f}
      Total Deduction : ${(FW + SW):.2f}
Net Pay : ${(GP - FW - SW):.2f}
""")

#Very unelegant compared to the previous one. I experimented with exec and declaring variable by using ascii in combination with exec.

