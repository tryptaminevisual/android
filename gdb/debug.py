#! /bin/python3

import gdb

global x_array, y_array
x_array = []
y_array = []

def changeFunName():
    # This function assumes that pc points to a break point at the beginning of the function

    # Step over once to save the value in edi
    gdb.execute('ni')
    gdb.write('[+]\t\tChanging the string to: Tampered\n')
    gdb.execute('set $edi = "Tampered"')
    gdb.execute('c')

def getFunCValue():
    # This function assumes that pc points to a break point at the beginning of the function C
    gdb.execute('ni 6')
    value = int(gdb.parse_and_eval('$eax'))
    print('Obtained value %d (python script)' % value)
    gdb.execute('c')
    return value

def getFunDValues():
    # This function assumes that pc points to a break point at the beginning of the function D
    global x_array
    # rbp-0x8 or rdx<-- index loop
    # 0x63 = 99 => 100 (0 to 99) iterations

    iter = int(gdb.parse_and_eval('$edx'))
    #Input FunD == x+y
    input = int(gdb.parse_and_eval('$eax'))
    gdb.execute('c')

    #Result on eax, edx and rbp-0x14
    result = int(gdb.parse_and_eval('$edx'))

    print('Iteration: ', iter)
    print('Input FunD: ', input)
    print('Result FunD: ', result)

    x_array.append(iter)
    y_array.append(result)




def solution():
    gdb.write('[+]\tStarting...\n')
    gdb.execute('set disassembly-flavor intel')
    gdb.execute('start')
    #Added break for each function call
    gdb.execute('rb Fun.')
    #Break point at the end of FunD
    gdb.execute('b *0x00000000004006a5')

    # Continue to FunA
    gdb.write('[+]\t\tContinuing until FunA breakpoint\n')
    gdb.execute('c')
    changeFunName()
    changeFunName()
    x = getFunCValue()

    for i in range(x,100):
        getFunDValues()
        gdb.execute('c')

    gdb.write('[+]\tX array: ' + str(x_array)+"\n")
    gdb.write('[+]\tY array: ' + str(y_array)+"\n")