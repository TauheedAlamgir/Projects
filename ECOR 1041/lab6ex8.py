# Tauheed Alamgir 101194927

def bank_statement(t: list) -> list:
    """
    Returns the sum of the deposits, the second is a negative number which will 
    be the sum of the withdrawals, and the last will be the current account 
    balance
    >>> bank_statement([999, -67, 76, 7.9])
    [1082.9, -67, 1015.9]
    >>> bank_statement([12576, -1000, 45.9, 89.9])
    [12711.8, -1000, 11711.8]
    >>> bank_statement([1090823, -110987, 6.7] )    
    [1090829.7, -110987, 979842.7]
    """
    Deposit = 0
    Withdrawal = 0
    for a in range(len(t)):
        if t [a] > 0:
            Deposit = Deposit + t[a]
        if t [a] < 0:
            Withdrawal = Withdrawal + t[a]
    return [round(Deposit, 2),round(Withdrawal,2),round(Deposit + Withdrawal,2)] 

a = [999, -67, 76, 7.9]
print(bank_statement(a))
a = [12576, -1000, 45.9, 89.9]
print(bank_statement(a))
a = [1090823, -110987, 6.7]    
print(bank_statement(a))
