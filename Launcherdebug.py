#!/usr/bin/python
#Launch me with gdb -x []
import gdb


print "***************************** Starting debug... ***************************"
gdb.execute("set pagination off")
gdb.execute("file ./debugme")
dissas = gdb.execute("disas main", to_string=True)
print dissas
