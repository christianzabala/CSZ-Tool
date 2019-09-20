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
                      Q: Quit/Log Out

                      Please enter your choice: """)

    if choice == "1":
        IDs()
    elif choice == "2":
        PING()
    elif choice == "3":
        PING2()
    elif choice == "4":
        MSAP()
    elif choice == "5":
        DupID()
    elif choice == "Q" or choice == "q":
        sys.exit()
    else:
        print("You must only select either 1,2,3 or 4.")
        print("Please try again")
        main()


def IDs():
    """Generate OAM command from a list of Address IDs"""

    add = "0001"
    oam = "oam host-connectivity-verify subscriber "
    nl = "\n"
    sp = " "
    quotation = "\""

    result = []

    print("Paste Customers Address IDs for the OAM Command then press ENTER then hit Ctrl+C "
          "when done :\n>")
    # (ctrl+f2 in pycharm)
    while True:
        try:
            line = input("")
            result.append(line)
        except KeyboardInterrupt:
            break

    ndlist = "\n".join(result)  #To remove duplicates
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


def PING():
    """Input or paste a list of IP addresses to have it auto-ping the IP address"""

    result = []
    ip_count = []

    print("Paste All IP address then press ENTER then hit Ctrl+C when done :\n>") #Enter is needed to have the last IP included 
    while True:
        try:
            line = input(" \n")
            result.append(line)
        except KeyboardInterrupt:
            break

    ndlist = "\n".join(result)  #To remove duplicates
    ndlist = ndlist.splitlines()

    print("\n" + "=" * 85)
    print("Ping Results: \n")
    for address in ndlist:
        res = subprocess.call(["ping", "-c", "3", address])
        if res == 0:
            print("\nPing to", address, "is OK \n")
            ip_count.append(res)
        elif res == 2:
            print("\nNo response from", address, "\n")
        else:
            print("\nPing to", address, "failed! \n")

    print("\n" + "=" * 85)
    print("Total IP Address inputted: ", len(ndlist))
    print("Total IP Address that is pingable: ", len(ip_count))
    print("Total IP Address that can't be ping: ", len(ndlist) - len(ip_count))
    print("\n" + "=" * 85)
    main()


def PING2():
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

    ndlist = "\n".join(final_list)  #To remove duplicates
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


def MSAP():
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

    ndlist = "\n".join(final_list)  #To remove duplicates
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


def DupID():
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
    ndlist = "\n".join(final_list)  #To remove duplicates
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


main()
