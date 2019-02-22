#!/usr/bin/env python3
"""
will be used for testing
this time, just writes a csv file to ./var
"""

import csv
from mortgage_calc import payment_schedule
from datetime import datetime

def main():
    file_path = './var/schedule.csv'

    parameters = {
        'start_date': datetime.today(),
        'term': 30*12,
        'interest_rate': 7 / 100,
        'loan_amount': 500000
    }

    array = payment_schedule(**parameters)
    
    with open(file_path, "w+") as csvfile:
        fieldnames = ['installment', 'payment_date', 'interest', 'principal', 'balance']
        schedule_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect="unix")
        schedule_writer.writeheader()
        for row in array:
            schedule_writer.writerow(row)
    
if __name__ == "__main__":
    main()