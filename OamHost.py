# !/usr/bin/python3
# Script to know the LAG ID, IP addresses for customer Address ID



def main():
    add = '0001'
    ad = 'AD'
    oam = 'oam host-connectivity-verify subscriber '
    nl = '\n'
    sp = ' '

    emptylist = []

    print(
        'Paste Customers Address IDs(AD0123456789),for OAM Host-Connectivity hit Ctrl-C when done :\n>')
    while True:
        try:
            line = input('')
            # if line == '':
            #    break
            emptylist.append(line)
        except KeyboardInterrupt:
            break

    clist = '\n'.join(emptylist)
    clist = clist.splitlines()

    # print (clist)

    print('\n# Copy and paste the commands below the line on BNG to know the lag id of the CXs\n')
    print('==================================================================')
    for i in clist:
         oam_cmd = sp+ oam + i + add + nl
         print(oam_cmd)
    print('\n==================================================================')


main()
