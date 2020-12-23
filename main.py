# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# test2
xx = "23 12 2012"
data = xx.split()
xd = data[0]
xm = data[1]
xy = data[2]

ced = 1
cem = 1
cey = 1602

cgd = 8
cgm = 9
cgy = 1609

dd = 1
mm = 1
yyyy = 2012

nly = int(yyyy / 4) - int(1602 / 4)
nod = (dd - ced) + ((mm - cem) * 30) + ((yyyy - cey) * 365) + cgd + nly
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

i = cgm - 1
ym = cgm
yy = cgy

while nod > arr[i] :
    nod = nod - arr[i]
    ym = ym + 1
    if ym == 12:
        ym = 0
    if i != 12 :
        i = i + 1
    if i == 12:
        i = 0
        yy = yy + 1
    if(yy % 400 == 0) or ((yy % 100 != 0) and (yy % 4 == 0)):
        arr[1] = 29
    else:
        arr[1] = 28

if ym == 0:
    ym = 12

print(str(nod) + " " + str(ym) + " " + str(yy))
