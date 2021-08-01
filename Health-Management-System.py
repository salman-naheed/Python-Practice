cleint_list = {1: 'Salman', 2: 'Vicky'}
log_list = {1: 'Exercise', 2: 'Diet'}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select Client's name: ")
    for key, value in cleint_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input())
    print("Selected Client: ", cleint_list[client_name], "\n", end="")

    print("Press 1 for Log ")
    print("Press 2 for Retrieve ")
    op = int(input())

    if op is 1:
        for key, value in log_list.items():
            print("Press", key, "to log ",value, "\n", end="")
        log_name = int(input())
        print("Select Job: ", log_list[log_name])
        f = open(cleint_list[client_name] + "_" + log_list[log_name] + ".txt", "a")
        k = 'y'
        while(k is not 'n'):
            print("Enter: ", log_list[log_name], "\n", end="")
            logInput = input()
            f.write("[" + str(getdate()) + "]: " + logInput + '\n')
            k = input("Add more? y/n: ")
            continue
        f.close()


    elif op is 2:
        for key,value in log_list.items():
            print("Press", key, "to Retrieve ", value, "\n", end="")
        log_name = int(input())
        print(cleint_list[client_name], "-", log_list[log_name], "Report: ", '\n', end="")
        f = open(cleint_list[client_name] + "_" + log_list[log_name] + ".txt", "rt")
        content = f.readlines()
        for line in content:
            print(line,end="")
        f.close()
    else:
        print("Invalid Input!")
except Exception as e:
    print("Wrong Input")


