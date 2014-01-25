import pexpect
import sys
import gc
import time

intelligence = 1024
spellbook = 1024
tooledHorn = 1024
Pw = 1024
ring1 = 1024
ring2 = 1024
count = 0

# or spellbook != 0 or intelligence != 0 or ring1 !=0 or ring2 !=0

while (spellbook != 0 or intelligence != 0 or ring1 !=0):
    count = count + 1
    intelligence = 1024
    Pw = 1024
    tooledHorn = 1024
    spellbook = 1024
    ring1 = 1024
    ring2 = 1024
    child = pexpect.spawn('nethack')
    child.delaybeforesend = 0.01
    #child.logfile_read = sys.stdout
    child.writelines('nwhfn')
    intelligence = child.expect(['In:18', 'Ch:'])
    #Pw = child.expect(['Pw:8', 'AC:'])
    child.writelines('    i')
    child.expect('a - ')
    spellbook = child.expect(['spellbook of magic missile', 'Potions'])
    ring1 = child.expect(['ring of slow digestion', 'Wands'])
    #child.writelines('    i')
    #child.expect('a - ')
    #ring2 = child.expect(['ring of foo',  'Wands'])
    child.writelines('    ')
    if (tooledHorn != 0):
        child.sendline('#quit')
        #child.expect('Really')
        child.writelines('y       ')
        print str(count) + ': No expected Wizard.' + ' Spellbook: ' + str(spellbook) + ' Ring1: ' + str(ring1) ' Intelligence: ' + str(intelligence)
        gc.collect()

child.writelines('    SY')
print('You get an expected Wizard.')
gc.collect()
