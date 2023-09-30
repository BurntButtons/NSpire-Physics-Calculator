import math
equation = input('Which equation?: ')

def numba1():
    flag = 0
    vxs = input('vx: ')
    if vxs != '':
        vx = float(vxs)
    else:
        flag += 4
    vx0s = input('vx0: ')
    if vx0s != '':
        vx0 = float(vx0s)
    else:
        flag += 1
    axs = input('ax: ')
    if axs != '':
        ax = float(axs)
    else:
        flag += 2
    ts = input('t: ')
    if ts != '':
        t = float(ts)
    else:
        flag += 3
    if flag == 1:
        vx0 = vx - ( ax * t )
    if flag == 2:
        if t == 0:
            print("it's over")
        else:
            ax = (vx - vx0) / t
    if flag == 3:
        t = (vx - vx0) / ax
    if flag == 4:
        vx = vx0 + ax * t
    else:
        print('Need more variables')

    print('vx: ', vx, 'vx0: ', vx0, 'ax: ', ax, 't: ', t)
    
def numba2():
    flag = 0
    xs = input('x: ')
    if xs != '':
        x = float(xs)
    else:
        flag += 1
    x0s = input('x0: ')
    if x0s != '':
        x0 = float(x0s)
    else:
        flag += 2
    vx0s = input('vx0: ')
    if vx0s != '':
        vx0 = float(vx0s)
    else:
        flag += 3
    axs = input('ax: ')
    if axs != '':
        ax = float(axs)
    else:
        flag += 4
    ts = input('t: ')
    if ts != '':
        t1 = float(ts)
        t2 = 'N/A'
    else:
        flag += 5
    if flag == 1:
        x = x0 + vx0 * t1 + 0.5 * ax * t1**2
    if flag == 2:
        x0 = -(ax * t1**2) / 2 - t1 * vx0 + x
    if flag == 3:
        vx0 = -(ax * t1**2 + 2 * x0 - 2 * x) / (2 * t1)
    if flag == 4:
        if t1 == 0:
            print("it's over")
        else:
            ax = -2 * (x0 + t1 * vx0 - x) / t1**2
    if flag == 5:
        evil = vx0 ** 2 - 2 * ax * (x0 - x)
        if evil >= 0:
            t1 = (-vx0 + math.sqrt(evil)) / ax
            t2 = (-vx0 - math.sqrt(evil)) / ax
        else:
            t1 = "evil"
            t2 = 'evil'
        
    print('x: ', x, 'x0: ', x0, 'vx0: ', vx0, 'ax: ', ax, 't(1): ', t1, 't2: ', t2)
    
def numba3():
    flag = 0
    xs = input('x: ')
    if xs != '':
        x = float(xs)
    else:
        flag += 1
    x0s = input('x0: ')
    if x0s != '':
        x0 = float(x0s)
    else:
        flag += 2
    vxs = input('vx: ')
    if vxs != '':
        vx = float(vxs)
    else:
        flag += 3
    vx0s = input('vx0: ')
    if vx0s != '':
        vx0 = float(vx0s)
    else:
        flag += 4
    axs = input('ax: ')
    if axs != '':
        ax = float(axs)
    else:
        flag += 5
    if flag == 1:
        x = (vx ** 2 - vx0 ** 2) / (2 * ax + x0)
    if flag == 2:
        x0 = (x - vx ** 2 - vx0 ** 2) / (2 * ax)
    if flag == 3:
        v2 = vx0 ** 2 + 2 * ax * (x - x0)
        vx = math.sqrt(v2)
    if flag == 4:
        vx02 = vx ** 2 - 2 * ax * (x - x0)
        vx0 = math.sqrt(vx02)
    if flag == 5:
        ax = (vx ** 2 - vx0 ** 2) / (2 * (x - x0))
    s = x - x0
    print('s: ', s, 'x: ', x, 'x0: ', x0, 'vx: ', vx, 'vx0: ', vx0, 'ax: ', ax, )
        
        
if equation == '1':
    numba1()
    
if equation == '2':
    numba2()

if equation == '3':
    numba3()

else:
    print('Not a valid equation')
    