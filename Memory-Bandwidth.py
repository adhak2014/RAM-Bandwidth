import time

myt=0.3

power=[3.3, 2.5, 1.8, 1.5, 1.2]

sdram=[168, 144]
ddr=[184,200,172]
ddr2=[240,200,214]
ddr3=[240,204,214]
ddr4=[288,256]

def sdram_ram():
    print('Years popular --> 1998 - 2002'); time.sleep(myt)
    print('Power requirement: ', power[0], 'V'); time.sleep(myt)
    print('DIMM module has: ',sdram[0], 'pins'); time.sleep(myt)
    print('So-DIMM module has:', sdram[1], 'pins'); time.sleep(myt)
    return

def ddr_ram():
    print('Years popular --> 2002 - 2005'); time.sleep(myt)
    print('Power requirement: ', power[1], 'V'); time.sleep(myt)
    print('DIMM module has: ',ddr[0], 'pins'); time.sleep(myt)
    print('So-DIMM module has:', ddr[1], 'pins'); time.sleep(myt)
    print('Micro-DIMM module has:', ddr[2], 'pins'); time.sleep(myt)
    return

def ddr2_ram():
    print('Years popular --> 2005 - 2009'); time.sleep(myt)
    print('Power requirement: ', power[2], 'V'); time.sleep(myt)
    print('DIMM module has: ',ddr2[0], 'pins'); time.sleep(myt)
    print('So-DIMM module has:', ddr2[1], 'pins'); time.sleep(myt)
    print('Micro-DIMM module has:', ddr2[2], 'pins'); time.sleep(myt)
    return

def ddr3_ram():
    print('Years popular --> 2009 - 2015'); time.sleep(myt)
    print('Power requirement: ', power[3], 'V'); time.sleep(myt)
    print('DIMM module has: ',ddr3[0], 'pins'); time.sleep(myt)
    print('So-DIMM module has:', ddr3[1], 'pins'); time.sleep(myt)
    print('Micro-DIMM module has:', ddr3[2], 'pins'); time.sleep(myt)
    return

def ddr4_ram():
    print('Years popular --> 2015+ '); time.sleep(myt)
    print('Power requirement: ', power[4], 'V'); time.sleep(myt)
    print('DIMM module has: ',ddr4[0], 'pins'); time.sleep(myt)
    print('So-DIMM module has:', ddr4[1], 'pins'); time.sleep(myt)
    return

print ('''   JEDEC and Intel standards
================================
Single Data Rate - SDR SDRAM
Double Data Rate - DDR SDRAM
Double Data Rate 2 - DDR2 SDRAM
Double Data Rate 3 - DDR3 SDRAM
Double Data Rate 4 - DDR4 SDRAM
''')

module_type=['66', '100', '133', '1600', '2100', '2700', '3200', '4200', '5300', '6400', '8500', '10600', '12800', '14900', '17000', '19200', '21300', '25600']
clock_speed=[66, 100, 116, 133.33, 150, 166.66, 200, 233.33, 266.66] # MHz
cycles_clock=[1, 2, 4, 8, 16]
bus_width=[8]

while 1:
    print ('SDR-SDRAM Module Type \t DDR-SDRAM Module Type \t DDR2-SDRAM Module Type'); time.sleep(myt)
    print (' 1.', 'PC' + module_type[0], '\t\t  4.', 'PC' + module_type[3], '\t\t  8.', 'PC2-' + module_type[6]); time.sleep(myt)
    print (' 2.', 'PC' + module_type[1], '\t\t  5.', 'PC' + module_type[4],'\t\t  9.', 'PC2-' + module_type[7]); time.sleep(myt)
    print (' 3.', 'PC' + module_type[2], '\t\t  6.', 'PC' + module_type[5],'\t\t 10.', 'PC2-' + module_type[8]); time.sleep(myt)
    print (' \t\t\t  7.', 'PC' + module_type[6], '\t\t 11.', 'PC2-' + module_type[9]); time.sleep(myt)
    print ('\t\t\t\t\t\t 12.', 'PC2-' + module_type[10]); time.sleep(myt)
    print ('DDR3-SDRAM Module Type \t DDR4-SDRAM Module Type'); time.sleep(myt)
    print ('13.', 'PC3-' + module_type[9],  '\t\t 19.', 'PC4-' + module_type[12]); time.sleep(myt)
    print ('14.', 'PC3-' + module_type[10], '\t\t 20.', 'PC4-' + module_type[13]); time.sleep(myt)
    print ('15.', 'PC3-' + module_type[11], '\t\t 21.', 'PC4-' + module_type[14]); time.sleep(myt)
    print ('16.', 'PC3-' + module_type[12], '\t\t 22.', 'PC4-' + module_type[15]); time.sleep(myt)
    print ('17.', 'PC3-' + module_type[13], '\t\t 23.', 'PC4-' + module_type[16]); time.sleep(myt)
    print ('18.', 'PC3-' + module_type[14], '\t\t 24.', 'PC4-' + module_type[17]); time.sleep(myt)
    print ()
    try:
        mtype=int(input('Enter the Module Type number or 0 to exit: '))
        print()
    except:
        print()
        print('You should enter an interger value...')
        print()
        continue
    if mtype == 1:  # SDRAM Memory Module
        time.sleep(myt)
        print('SDRAM Module: ', 'PC' + module_type[0]); time.sleep(myt)
        print('Chip Type: %0.2f' %((1/(clock_speed[0]*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Later', module_type[0], 'modules were rated at 10 ns (100 MHz)'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[0], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[0], 'MHz')
        print('Cycles per Clock: ', cycles_clock[0]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[0]*cycles_clock[0], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Transfer Rate: ', clock_speed[0]*cycles_clock[0]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        sdram_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==2:
        time.sleep(myt)
        print('SDRAM Module: ', 'PC' + module_type[1]); time.sleep(myt)
        print('Chip Type: %0.2f' %((1/(clock_speed[1]*10**6))*10**9), 'ns'); time.sleep(myt)
        print('In fact', module_type[1], 'modules were rated at 8 ns (125 MHz)'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[1], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[1], 'MHz')
        print('Cycles per Clock: ', cycles_clock[0]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[1]*cycles_clock[0], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Transfer Rate: ', clock_speed[1]*cycles_clock[0]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        sdram_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==3:
        time.sleep(myt)
        print('SDRAM Module: ', 'PC' + module_type[2]); time.sleep(myt)
        print('Chip Type: %0.2f' %((1/(clock_speed[3]*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Later', module_type[2], 'modules were rated at 7 ns (143 MHz)'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[3], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[3], 'MHz')
        print('Cycles per Clock: ', cycles_clock[0]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[3]*cycles_clock[0], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Transfer Rate: ', clock_speed[3]*cycles_clock[0]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        sdram_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==4:  # DDR Memory Module
        time.sleep(myt)
        print('DDR Module: ', 'PC' + module_type[3]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[1]*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[1], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[1]*(cycles_clock[1]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[1]*cycles_clock[1], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR'+str((clock_speed[1]*cycles_clock[1]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[1]*cycles_clock[1]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[1]*cycles_clock[1]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==5:
        time.sleep(myt)
        print('DDR Module: ', 'PC' + module_type[4]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[3]*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[3], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[3]*(cycles_clock[1]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[3]*cycles_clock[1], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR'+str((clock_speed[3]*cycles_clock[1]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[3]*cycles_clock[1]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[3]*cycles_clock[1]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==6:
        time.sleep(myt)
        print('DDR Module: ', 'PC' + module_type[5]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[5]*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[5], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[5]*(cycles_clock[1]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[5]*cycles_clock[1], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR'+str((clock_speed[5]*cycles_clock[1]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[5]*cycles_clock[1]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[5]*cycles_clock[1]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==7:
        time.sleep(myt)
        print('DDR Module: ', 'PC' + module_type[6]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[6]*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[6], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[6]*(cycles_clock[1]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[6]*cycles_clock[1], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR'+str((clock_speed[6]*cycles_clock[1]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[6]*cycles_clock[1]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[6]*cycles_clock[1]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==8:  # DDR2 Memory Module
        time.sleep(myt)
        print('DDR2 Module: ', 'PC2-' + module_type[6]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[1]*(cycles_clock[2]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[1], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[1]*(cycles_clock[2]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[1]*cycles_clock[2], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR2-'+str((clock_speed[1]*cycles_clock[2]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[1]*cycles_clock[2]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[1]*cycles_clock[2]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr2_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==9:
        time.sleep(myt)
        print('DDR2 Module: ', 'PC2-' + module_type[7]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[3]*(cycles_clock[2]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[3], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[3]*(cycles_clock[2]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[3]*cycles_clock[2], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR2-'+str((clock_speed[3]*cycles_clock[2]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[3]*cycles_clock[2]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[3]*cycles_clock[2]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr2_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==10:
        time.sleep(myt)
        print('DDR2 Module: ', 'PC2-' + module_type[8]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[5]*(cycles_clock[2]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[5], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[5]*(cycles_clock[2]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[5]*cycles_clock[2], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR2-'+str((clock_speed[5]*cycles_clock[2]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[5]*cycles_clock[2]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[5]*cycles_clock[2]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr2_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==11:
        time.sleep(myt)
        print('DDR2 Module: ', 'PC2-' + module_type[9]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[6]*(cycles_clock[2]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[6], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[6]*(cycles_clock[2]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[6]*cycles_clock[2], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR2-'+str((clock_speed[6]*cycles_clock[2]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[6]*cycles_clock[2]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[6]*cycles_clock[2]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr2_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==12:
        time.sleep(myt)
        print('DDR2 Module: ', 'PC2-' + module_type[10]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[8]*(cycles_clock[2]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[8], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[8]*(cycles_clock[2]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[8]*cycles_clock[2], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR2-'+str((clock_speed[8]*cycles_clock[2]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[8]*cycles_clock[2]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[8]*cycles_clock[2]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr2_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==13: # DDR3 Memory Module
        time.sleep(myt)
        print('DDR3 Module: ', 'PC3-' + module_type[9]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[1]*(cycles_clock[3]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[1], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[1]*(cycles_clock[3]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[1]*cycles_clock[3], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR3-'+str((clock_speed[1]*cycles_clock[3]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[1]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[1]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Tri-Channel Transfer Rate: ', 3*clock_speed[1]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr3_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==14:
        time.sleep(myt)
        print('DDR3 Module: ', 'PC3-' + module_type[10]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[3]*(cycles_clock[3]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[3], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[3]*(cycles_clock[3]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[3]*cycles_clock[3], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR3-'+str((clock_speed[3]*cycles_clock[3]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[3]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[3]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Tri-Channel Transfer Rate: ', 3*clock_speed[3]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr3_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==15:
        time.sleep(myt)
        print('DDR3 Module: ', 'PC3-' + module_type[11]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[5]*(cycles_clock[3]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[5], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[5]*(cycles_clock[3]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[5]*cycles_clock[3], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR3-'+str((clock_speed[5]*cycles_clock[3]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[5]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[5]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Tri-Channel Transfer Rate: ', 3*clock_speed[5]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr3_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==16:
        time.sleep(myt)
        print('DDR3 Module: ', 'PC3-' + module_type[12]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[6]*(cycles_clock[3]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[6], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[6]*(cycles_clock[3]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[6]*cycles_clock[3], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR3-'+str((clock_speed[6]*cycles_clock[3]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[6]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[6]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Tri-Channel Transfer Rate: ', 3*clock_speed[6]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr3_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==17:
        time.sleep(myt)
        print('DDR3 Module: ', 'PC3-' + module_type[13]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[7]*(cycles_clock[3]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[7], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[7]*(cycles_clock[3]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[7]*cycles_clock[3], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR3-'+str((clock_speed[7]*cycles_clock[3]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[7]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[7]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Tri-Channel Transfer Rate: ', 3*clock_speed[7]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr3_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==18:
        time.sleep(myt)
        print('DDR3 Module: ', 'PC3-' + module_type[14]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[8]*(cycles_clock[3]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[8], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[8]*(cycles_clock[3]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[8]*cycles_clock[3], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR3-'+str((clock_speed[8]*cycles_clock[3]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[8]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[8]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Tri-Channel Transfer Rate: ', 3*clock_speed[8]*cycles_clock[3]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr3_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==19: # DDR4 Memory Module
        time.sleep(myt)
        print('DDR4 Module: ', 'PC4-' + module_type[12]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[1]*(cycles_clock[4]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[1], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[1]*(cycles_clock[4]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[1]*cycles_clock[4], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR4-'+str((clock_speed[1]*cycles_clock[4]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[1]*cycles_clock[4]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[1]*cycles_clock[4]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr4_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==20:
        time.sleep(myt)
        print('DDR4 Module: ', 'PC4-' + module_type[13]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[2]*(cycles_clock[4]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[2], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[2]*(cycles_clock[4]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[2]*cycles_clock[4], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR4-'+str((clock_speed[2]*cycles_clock[4]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[2]*cycles_clock[4]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[2]*cycles_clock[4]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr4_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==21:
        time.sleep(myt)
        print('DDR4 Module: ', 'PC4-' + module_type[14]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[3]*(cycles_clock[4]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[3], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[3]*(cycles_clock[4]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[3]*cycles_clock[4], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR4-'+str((clock_speed[3]*cycles_clock[4]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[3]*cycles_clock[4]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[3]*cycles_clock[4]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr4_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==22:
        time.sleep(myt)
        print('DDR4 Module: ', 'PC4-' + module_type[15]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[4]*(cycles_clock[4]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[4], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[4]*(cycles_clock[4]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[4]*cycles_clock[4], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR4-'+str((clock_speed[4]*cycles_clock[4]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[4]*cycles_clock[4]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[4]*cycles_clock[4]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr4_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==23:
        time.sleep(myt)
        print('DDR4 Module: ', 'PC4-' + module_type[16]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[5]*(cycles_clock[4]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[5], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[5]*(cycles_clock[4]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[5]*cycles_clock[4], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR4-'+str((clock_speed[5]*cycles_clock[4]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[5]*cycles_clock[4]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[5]*cycles_clock[4]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr4_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==24:
        time.sleep(myt)
        print('DDR4 Module: ', 'PC4-' + module_type[17]); time.sleep(myt)
        print('Cycle Time: %0.2f' %((1/(clock_speed[6]*(cycles_clock[4]/2)*10**6))*10**9), 'ns'); time.sleep(myt)
        print('Memory Clock Speed: ', clock_speed[6], 'MHz'); time.sleep(myt)
        print('I/O Bus Clock Speed: ', clock_speed[6]*(cycles_clock[4]/2), 'MHz')
        print('Cycles per Clock: ', cycles_clock[1]); time.sleep(myt)
        print('Bus Speed: ', clock_speed[6]*cycles_clock[4], 'MTps'); time.sleep(myt)
        print('Bus Width: ', bus_width[0], 'Bytes'); time.sleep(myt)
        print('Chip Type: ', 'DDR4-'+str((clock_speed[6]*cycles_clock[4]))); time.sleep(myt)
        print('Module Transfer Rate: ', clock_speed[6]*cycles_clock[4]*bus_width[0], 'MBps'); time.sleep(myt)
        print('Dual-Channel Transfer Rate: ', 2*clock_speed[6]*cycles_clock[4]*bus_width[0], 'MBps'); time.sleep(myt)
        print()
        ddr4_ram(); time.sleep(myt)
        print()
        end_prog=input('Press \'y\' to continue or any key to exit...')
        if end_prog=='y':
            continue
        else:
            break
    elif mtype==0:
        break
    else:
        print()
        print('Bad or incorrect entry, please repeat...\n')
