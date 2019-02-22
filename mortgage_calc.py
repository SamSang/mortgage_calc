"""
set of functions to build a schedule of mortgage payments
"""
from datetime import datetime


def monthly_i(i):
    #calculate the monthly interest rate
    return i / 12

def monthly_payment(term, start_date, rate, loan_amount):
    """
    calculates the monthly payment
    based on the term, fixed interest rate, loan amount
    """
    #plug in the forumal to compute the payment
    #payment = loan_amount * ((rate*(1+rate)**term) / ((1+rate)**term-1))
    payment = loan_amount * ( (rate*(1+rate)**term) / (  ( (1+rate)**term)-1 ) )

    #return the payment as a money object
    return payment

def payment_schedule(start_date, term, interest_rate, loan_amount):
    """
    calculates the payment schedule
    based on the start date, term, interest rate, loan amount
    
    returns a dict of the payment schedule

    #first, calculate the monthly payment
    second, calculate the interest on the loan
    third, subtract the interest from the payment to get the principal
    fourth, subtract the principal from the balance to get the new balance
    """

    #use the monthly interest rate
    rate = monthly_i(interest_rate)
    print("rate: "+ str(rate))

    #compute the monthly payment
    payment = monthly_payment(term, start_date, rate, loan_amount)
    print("payment: "+ str(payment))

    #start our array
    schedules = []

    #loop through 1 .. term
    #create installment, payment_date, interest, balance, principal
    #account for the 0 index
    for n in range(term + 1): 
        schedule = {} #installment, paymment_date, interest, principal, balance
        if n == 0:
            #instantiate the row zero of the schedule
            schedule['installment'] = 0
            schedule['payment_date'] = start_date
            schedule['balance'] = loan_amount
        else:
            #calculate the interest on the loan
            schedule['installment'] = n
            ##schedule[n]['payment_date'] = start_date
            schedule['interest'] = schedules[n-1]['balance']*rate
            schedule['principal'] = payment - schedule['interest']
            schedule['balance'] = schedules[n-1]['balance'] - schedule['principal']
        schedules.append(schedule)
    #return the dictionary
    return schedules