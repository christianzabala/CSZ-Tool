#!/usr/bin/python3

# CSZ Tool (CODE for SCRAPING files to ZERO human error)

"""This tool or script can be used to simplify the troubleshooting issues like fiber cut, maintenances:1x32 splitter,
Move customers, and etc., that needs to know the customers IP address & LAG-IDs and then do a clear MSAP for all
LAG-IDs. This script also includes a auto-ping an IP addresses listed on a text file and an option to remove a
duplicate network element when a multiple tickets needs a unique network element only. """

__author__ = 'christian.philip.zabala@gmail.com'

import sys  # for using sys.exit command to quit/logout of the application
import subprocess  # for the ping process
import re  # for finding a regular expression
import os  # for os path in searching file


def main():
    """Creates the Main Menu of the script"""

    print("                      ************MAIN MENU**************")
    # time.sleep(1)
    print()

    choice = input("""
                      1: Use Customer's Address IDs for OAM command
                      2: Input IPs to ping
                      3: Ping IPs that is on a file
                      4: Search LAG IDs on a file for clearing MSAP
                      5: For removing duplicate network element
                      6: Find the different network element between two files(Ticket)
                      Q: Quit/Log Out
                      Please enter your choice: """)

    if choice == "1":
        ids()
    elif choice == "2":
        ping()
    elif choice == "3":
        ping2()
    elif choice == "4":
        msap()
    elif choice == "5":
        dup_id()
    elif choice == "6":
        diff_ne()
    elif choice == "Q" or choice == "q":
        sys.exit()
    else:
        print("You must only select either 1,2,3 or 4.")
        print("Please try again")
        main()


def ids():
    """Generate OAM command from a list of Address IDs"""

    add = "0001"
    oam = "oam host-connectivity-verify subscriber "
    nl = "\n"
    sp = " "
    quotation = "\""

    result = []

    print("Paste Customers Address IDs for the OAM Command then hit Ctrl+C "
          "when done :\n>")

    while True:
        try:
            line = input("")
            result.append(line)
        except KeyboardInterrupt:  # Ctrl+F2 in pycharm
            break

    ndlist = "\n".join(result)
    ndlist = ndlist.splitlines()

    print("\n" + "=" * 85)
    print("Total Number of Address IDs: ")
    print(len(ndlist))
    print("=" * 85)

    print("\n# Copy and paste the commands below the line on BNG to know the LAG-ID of the CXs\n")
    print("=" * 85)
    for i in ndlist:
        oam_cmd = sp + oam + quotation + i + add + quotation + nl
        print(oam_cmd)
    print("\n" + "=" * 85)
    main()


def ping():
    """Input or paste a list of IP addresses to have it auto-ping the IP address"""

    result = []
    ip = []
    ip_count = []

    print(
        "Paste All IP address then hit Ctrl+C when done :\n>")  # Enter is needed to have the last IP included
    while True:
        try:
            line = input("")
            result.append(line + "\n")
        except KeyboardInterrupt:
            break

    ndlist = "\n".join(result)
    ndlist = ndlist.splitlines()

    for line in ndlist:
        line1 = str(line)
        match = re.search(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line1)  # regex to find IP addresses
        if match:
            ips = match.group(0)
            ip.append(ips)

    print("\n" + "=" * 85)
    print("Ping Results: \n")
    for address in ip:
        res = subprocess.call(["ping", "-c", "3", address])
        if res == 0:
            print("\nPing to", address, "is OK \n")
            ip_count.append(res)
        elif res == 2:
            print("\nNo response from", address, "\n")
        else:
            print("\nPing to", address, "failed! \n")

    print("\n" + "=" * 85)
    print("Total IP Address inputted: ", len(ip))
    print("Total IP Address that is pingable: ", len(ip_count))
    print("Total IP Address that can't be ping: ", len(ip) - len(ip_count))
    print("\n" + "=" * 85)
    main()


def ping2():
    """open a file that has IP addresses on it then gather the total IP address and auto-ping it"""

    result = []
    final_list = []
    ip_count = []
    no_ip = []

    file_name = input("Enter a filename(Case Sensitive, include file type ex: .txt): ")
    while (not os.path.isfile(file_name)) or (not os.path.exists(file_name)):
        file_name = input("File not found in the directory, Try again: ")

    with open(file_name, "r") as file:
        for line in file:
            match = re.search(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)  # regex to find IP addresses
            match1 = re.search(r"\b(\w*No host-connectivity states found\w*)\b", line)
            if match:
                ips = match.group(0)
                result.append(ips)
            elif match1:
                noips = match1.group(0)
                no_ip.append(noips)

    for num in result:
        if num not in final_list:
            final_list.append(num)

    ndlist = "\n".join(final_list)
    ndlist = ndlist.splitlines()

    print("=" * 85)
    print("\n Ping Results: \n")

    for address in ndlist:
        res = subprocess.call(["ping", "-c", "3", address])
        if res == 0:
            print("\nPing to", address, "is OK \n")
            ip_count.append(res)
        elif res == 2:
            print("\nno response from", address, "\n")
        else:
            print("\nping to", address, "failed! \n")

    print("\n" + "=" * 85)
    print("Total IP Address on the file: ", len(ndlist))
    print("Total Address IDs on the file that have NO IP: ", len(no_ip))
    print("Total IP Address that is pingable: ", len(ip_count))
    print("Total IP Address that can't be ping: ", len(ndlist) - len(ip_count))
    print("\n" + "=" * 85)
    main()


def msap():
    """open a file that has LAG-IDs on it then generate a clear service id Command"""

    result = []
    final_list = []
    no_ip = []
    clear = "clear service id 1 msap "
    nl = "\n"

    file_name = input("Enter a filename(Case Sensitive, include file type ex: .txt): ")
    while (not os.path.isfile(file_name)) or (not os.path.exists(file_name)):
        file_name = input("File not found in the directory, Try again: ")

    with open(file_name, "r") as file:
        for line in file:
            match = re.search(r"[^[]*\[([^]]*)\]", line)  # regex to fine words inside a bracket[]
            match1 = re.search(r"\b(\w*No host-connectivity states found\w*)\b", line)
            if match:
                lags = match.group(1)
                result.append(lags)
            elif match1:
                noips = match1.group(0)
                no_ip.append(noips)

    for num in result:
        if num not in final_list:
            final_list.append(num)

    ndlist = "\n".join(final_list)
    ndlist = ndlist.splitlines()

    print("=" * 85)
    print("Total Number of LAG-IDs: ", len(ndlist))
    print("Total Address IDs on the file that have NO LAG-IDs: ", len(no_ip))
    print("=" * 85)
    print('\n# Copy the commands below and paste it on BNG to Clear the LAG-IDs of the CXs\n')
    print("=" * 85)

    for i in ndlist:
        ab = clear + i + nl
        print(ab)
    print("=" * 85)
    main()


def dup_id():
    """open a file that has consolidated network elements from different outage tickets then the script will return
    a result without a duplicate network element """

    final_list = []

    file_name = input("Enter a filename(Case Sensitive, include file type ex: .txt): ")
    while (not os.path.isfile(file_name)) or (not os.path.exists(file_name)):
        file_name = input("File not found in the directory, Try again: ")

    with open(file_name, "r") as file:
        file1 = file.readlines()
        st = "".join(file1)
        match = re.split(", |,|\n", st)

        for cxid in match:
            if cxid not in final_list:
                final_list.append(cxid)

    ndlist = "\n".join(final_list)
    ndlist = ndlist.splitlines()
    l_to_s = ", ".join(ndlist)

    print("=" * 85 + "\nTotal Number of Network Elements: ")
    print(len(ndlist))
    print("=" * 85)
    print("Network elements without Duplicate: \n(Doesn't remove an element when the whole PON is included already)")
    print("=" * 85)
    print(l_to_s)
    print("=" * 85)
    main()


def diff_ne():
    """open two files that has network elements from different outage tickets then the script will return
    a result on the different network elements between the tickets"""

    file_name1 = input("Enter a filename(Case Sensitive, include file type ex: .txt): ")
    while (not os.path.isfile(file_name1)) or (not os.path.exists(file_name1)):
        file_name1 = input("File not found in the directory, Try again: ")

    file_name2 = input("Enter a filename(Case Sensitive, include file type ex: .txt): ")
    while (not os.path.isfile(file_name2)) or (not os.path.exists(file_name2)):
        file_name2 = input("File not found in the directory, Try again: ")

    with open(file_name1, "r") as file1, open(file_name2, "r") as file2:
        file1 = file1.readlines()
        file2 = file2.readlines()

        st1 = "".join(file1)
        match1 = re.split(", |,|\n", st1)
        st2 = "".join(file2)
        match2 = re.split(", |,|\n", st2)

        difference = set(match1).symmetric_difference(match2)  # difference on both files

        # Compare file 1 to file 2
        element2 = set(difference).intersection(match1)
        l_to_s2 = ", ".join(element2)
        print("=" * 85 + "\nNetwork Elements that file 1 has but file 2 doesn't have:")
        print("=" * 85)
        print(l_to_s2)
        print("=" * 85)

        # Compare file 2 to file 1
        element1 = set(difference).intersection(match2)
        l_to_s1 = ", ".join(element1)
        print("=" * 85 + "\nNetwork Elements that file 2 has but file 1 doesn't have::")
        print("=" * 85)
        print(l_to_s1)
        print("=" * 85)
    main()


main()
