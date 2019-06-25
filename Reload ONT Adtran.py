# !/usr/bin/python
# super quick script to convert circuit id to adtran indexes for reboot

import sys


def main():
    at = '@'
    s = "/"
    gpon = 'gpon'
    d = '.'
    y = 'y'
    nl = '\n'
    rel = 'reload'
    sp = ' '

    emptylist = []

    print(
        'Paste Adtran circuits (olt01.nuq222 1/1/18/7/2), it will be converted to Adtran ONT index for reloading ont, hit Ctrl-C when done :\n>')
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

    print('\n# Copy and paste the commands below the line on Adtran OLT to reboot the ONTs\n')
    print('==================================================================')
    print('enable\n')
    for i in clist:
        ignore, shelf, slot, pon, ont = i.split('/')
        adt_index = ont + at + shelf + s + slot + s + pon + d + gpon + nl + y
        rel_cmd = rel + sp + adt_index
        print(rel_cmd)
    print('\n==================================================================')


main()
