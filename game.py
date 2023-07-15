import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS=3
COLS=3

symbol_count={"$":2,"@":4,"#":6,"&":8}
symbol_value={"$":5,"@":4,"#":3,"&":2}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings,winning_lines



def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    columns =[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")

        print()


def deposit():
    while True:
        amount=input("How much you would like to deposit? $ ")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Need greater than 0.")
        else:
            print("Please enter number:")
    return amount


def get_number_of_lines():
    
    while True:
        lines=input("The line You want to bet on each line(1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines=int(lines)
            if lines >=1 and lines<= MAX_LINES:
                break
            else:
                print("Enter valid number of line:")
        else:
            print("Please enter number:")
    return lines


def get_bet():
    while True:
        amount=input("How much you would like to bet? $ ")
        if amount.isdigit():
            amount=int(amount)
            if amount > MIN_BET and amount<MAX_BET:
                break
            else:
                print(f"amount must be ${MIN_BET}-${MAX_BET}")
        else:
            print("Please enter number:")
    return amount


def spin(balance):
    lines=get_number_of_lines()
    while True:
        bets=get_bet()
        total_bet=bets*lines
        if total_bet > balance:
            print(f"Insufficient Balance!Your current balance is :${balance}")
        else:
            break

    print(f"You are betting ${bets} on {lines} lines. Total Bet is : ${total_bet}")
    # print(balance,lines,bets)

    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    Winnings,winning_lines=check_winnings(slots,lines,bets,symbol_value)
    print(f"You Won {Winnings}")
    print(f"You Won On lines:", *winning_lines)

    return Winnings - total_bet



def main():
    balance=deposit()
    while True:
        print(f"Current balance is: ${balance}")
        Button=input("press ENTER to play or (e to exit)")
        if Button == "e":
            break
        balance += spin(balance)
    print(f"You left ${balance}")

main()