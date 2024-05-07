import random
a = ['C','F','Bb','Eb','G','D','A']
# level 1
scale = ['root','2','3','4','5','6','7']
triad = ['Maj','Min','Aug','Dim']
fpart = ['Maj7','Min7','Dom7','Min7b5','Dom7sus4','7#5','Dim7','Maj6','Min6','Min9','9','7b9','7#9','13']
arp1 = ['Maj7','Min7','Dom7','Min7b5','Dom7sus4','7#5','Dim7']
# level 2
scale2 = ['root','2','b3','4','5','6','7']
invtriad = ['Root','1st inv','2nd inv']
fpart2 = ['Min(maj7)','Maj7#5','Maj7b5','Min7#5','7b5','Dim(maj7)','Maj(9/7)','Maj(9/6)','Min9(maj7)','7(b9/b13)','13(b9)','9(b13)']
arp4 = ['Min(maj7)','Maj7#5','Maj7b5','Min7#5','7b5','Dim(maj7)']
#level 3
scale3 = ['1','2','b3','4','5','b6','7']
striad = ['Maj','Min']
invfour = ['root','1st inv','2nd inv','3rd inv']
# level 4
scale4 = ['1','2','3','4','5','b6','7']


firstq = []
for i in range(len(a)): # first question list with all posibilities
        for j in range(len(scale)):
            firstq.extend([a[i], scale[j]])

b = a[:] # second question list

thirdq = []
for i in range(len(a)): # third question list with all posibilities
        for j in range(len(triad)):
            thirdq.extend([a[i], triad[j]])

fourq = thirdq[:] # fourth

fifq = []
for i in range(len(a)): # fifth question list with all posibilities
        for j in range(len(fpart)):
            fifq.extend([a[i], fpart[j]])

sixq = []
for i in range(len(a)): # sixsth question list with all posibilities
        for j in range(len(arp1)):
            sixq.extend([a[i], arp1[j]])

# ************************************************* level 2

firstq2 = []
for i in range(len(a)): # first question list with all posibilities
        for j in range(len(scale2)):
            firstq2.extend([a[i], scale2[j]])

b2 = a[:] # second question list

thirdq2 = []
for i in range(len(a)): # third question list with all posibilities
        for j in range(len(triad)):
            thirdq2.extend([a[i], triad[j]])

fourq2 = thirdq2[:] # fourth

fifq2 = []
for i in range(len(a)): # fifth question list with all posibilities
        for j in range(len(fpart2)):
            fifq2.extend([a[i], fpart2[j]])

sixq2 = []
for i in range(len(a)): # sixsth question list with all posibilities
        for j in range(len(arp4)):
            sixq2.extend([a[i], arp4[j]])

# ************************************************** level 3

firstq3 = []
for i in range(len(a)): # first question list with all posibilities
        for j in range(len(scale3)):
            firstq3.extend([a[i], scale3[j]])

b3 = a[:] # second question list

thirdq3 = []
for i in range(len(a)): # third question list with all posibilities
        for j in range(len(triad)):
            for k in range(len(invtriad)):
                thirdq3.extend([a[i], triad[j], invtriad[k]])

fourq3 = [] # fourth quesiton list
for i in range(len(a)):
     for j in range(len(triad)):
          for k in range(len(invtriad)):
            fourq3.extend([a[i], triad[j], invtriad[k]])

fifq3 = []
for i in range(len(a)): # fifth question list with all posibilities
        for j in range(len(fpart)):
            fifq3.extend([a[i], fpart[j]])

sixq3 = []
for i in range(len(a)): # sixsth question list with all posibilities
        for j in range(len(arp1)):
            for k in range(len(invfour)):
                sixq3.extend([a[i], arp1[j], invfour[k]])

# ************************************************* level 4

firstq4 = []
for i in range(len(a)): # first question list with all posibilities
        for j in range(len(scale4)):
            firstq4.extend([a[i], scale4[j]])

b4 = [] # second question list
for i in range(len(a)):
     for j in range(len(striad)):
          b4.extend([a[i], striad[j]])

thirdq4 = []
for i in range(len(a)): # third question list with all posibilities
        for j in range(len(triad)):
            for k in range(len(invtriad)):
                thirdq4.extend([a[i], triad[j], invtriad[k]])

fourq4 = [] # fourth quesiton list
for i in range(len(a)):
     for j in range(len(triad)):
          for k in range(len(invtriad)):
            fourq4.extend([a[i], triad[j], invtriad[k]])

fifq4 = []
for i in range(len(a)): # fifth question list with all posibilities
        for j in range(len(fpart2)):
            fifq4.extend([a[i], fpart2[j]])

sixq4 = []
for i in range(len(a)): # sixsth question list with all posibilities
        for j in range(len(arp4)):
            for k in range(len(invfour)):
                sixq4.extend([a[i], arp4[j], invfour[k]])
   
x = 1000
while x != 'stop':
    x = input('Input your level or type "clear" to reset or type "stop" to stop: ')
    if x.isdigit():

        x = int(x)

    if x == 1:
        if len(firstq) != 0:
            r = random.randrange(0, len(firstq), 2)                    #first question
            print('\n1. Play', firstq[r], 'major from the', firstq[r+1], ',two octaves.\n')
            del firstq[r]
            del firstq[r]
    
        else:
            print('\nAll done! =)\n')
        
        if len(b) != 0:
            r = random.randrange(0, len(b))                             # second question
            print('2. Play', b[r],'chromatic scale, two octaves.\n')
            del b[r]
        else:
            print('All done! =)\n')

        if len(thirdq) != 0:
            r = random.randrange(0, len(thirdq), 2)                     # third question
            print('3. Play', thirdq[r], thirdq[r+1], 'starting from root position, across fingerboard, one octave.\n')
            del thirdq[r]
            del thirdq[r]
        else:
            print('All done! =)\n')

        if len(fourq) != 0:
            r = random.randrange(0, len(fourq), 2)                       # fourth question
            print('4. Play', fourq[r], fourq[r+1], 'arpeggio one octave from the root.\n')
            del fourq[r]
            del fourq[r]
        else:
            print('All done! =)\n')

        if len(fifq) != 0:
            r = random.randrange(0, len(fifq), 2) #fifth question
            print('5. Play', fifq[r], fifq[r+1], 'one form.\n')
            del fifq[r]
            del fifq[r]
        else:
            print('All done! =)\n')
            
        if len(sixq) != 0:
            r = random.randrange(0, len(sixq), 2) #sixth question
            print('6. Play', sixq[r], sixq[r+1], 'arpeggio one octave from the root.\n')
            del sixq[r]
            del sixq[r]
        else:
            print('All done! =)\n')

    elif x == 2:                                                          # level 2

        if len(firstq2) != 0:
            r = random.randrange(0, len(firstq2), 2)                      #first question
            print('\n1. Play', firstq2[r], 'melodic minor from the', firstq2[r+1], ',two octaves.\n')
            del firstq2[r]
            del firstq2[r]
        else:
            print('\nAll done! =)\n')

        if len(b2) != 0:
            r = random.randrange(0, len(b2))                             # second question
            print('2. Play', b2[r],'whole-tone scale, two octaves.\n')
            del b2[r]
        else:
            print('All done! =)\n')

        if len(thirdq2) != 0:
            r = random.randrange(0, len(thirdq2), 2)                     # third question
            print('3. Play', thirdq2[r], thirdq2[r+1],'starting from any inversion, one octave up and down all string sets.\n')
            del thirdq2[r]
            del thirdq2[r]
        else:
            print('All done! =)\n')

        if len(fourq2) != 0:
            r = random.randrange(0, len(fourq2), 2)                      # fourth question
            print('4. Play', fourq2[r], fourq2[r+1], 'arpeggio two octaves from the root.\n')
            del fourq2[r]
            del fourq2[r]
        else:
            print('All done! =)\n')

        if len(fifq2) != 0:
            r = random.randrange(0, len(fifq2), 2)                       #fifth question
            print('5. Play', fifq2[r], fifq2[r+1], 'one form.\n')
            del fifq2[r]
            del fifq2[r]
        else:
            print('All done! =)\n')

        if len(sixq2) != 0:
            r = random.randrange(0, len(sixq2), 2)                       #sixth question
            print('6. Play', sixq2[r], sixq2[r+1], 'arpeggio one octave from the root.\n')
            del sixq2[r]
            del sixq2[r]
        else:
            print('All done! =)\n')

    elif x == 3:                                                          # level 3
        if len(firstq3) != 0:
            r = random.randrange(0, len(firstq3), 2)                      #first question
            print('\n1. Play', firstq3[r], 'harmonic minor from the', firstq3[r+1], ',two octaves.\n')
            del firstq3[r]
            del firstq3[r]
        else:
            print('\nAll done! =)\n')

        if len(b3) != 0:
            r = random.randrange(0, len(b3))                             # second question
            print('2. Play', b3[r],'diminished scale, two octaves.\n')
            del b3[r]
        else:
            print('All done! =)\n')

        if len(thirdq3) != 0:
            r = random.randrange(0, len(thirdq3), 3)                     # third question
            print('3. Play', thirdq3[r], thirdq3[r+1],'spread voicing starting from', thirdq3[r+2], ',one octave.\n')
            del thirdq3[r]
            del thirdq3[r]
            del thirdq3[r]
        else:
            print('All done! =)\n')

        if len(fourq3) != 0:
            r = random.randrange(0, len(fourq3), 3)                      # fourth question
            print('4. Play', fourq3[r], fourq3[r+1], 'arpeggio from', fourq3[r+2],'one octave.\n')
            del fourq3[r]
            del fourq3[r]
            del fourq3[r]
        else:
            print('All done! =)\n')

        if len(fifq3) != 0:
            r = random.randrange(0, len(fifq3), 2)                       #fifth question
            print('5. Play', fifq3[r], fifq3[r+1], 'two forms.\n')
            del fifq3[r]
            del fifq3[r]
        else:
            print('All done! =)\n')

        if len(sixq3) != 0:
            r = random.randrange(0, len(sixq3), 3)                       #sixth question
            print('6. Play', sixq3[r], sixq3[r+1], 'arpeggio one octave',sixq3[r+2],'.\n')
            del sixq3[r]
            del sixq3[r]
            del sixq3[r]
        else:
            print('All done! =)\n')
    
    elif x == 4:                                                          #level 4
        if len(firstq4) != 0:
            r = random.randrange(0, len(firstq4), 2)                      #first question
            print('\n1. Play', firstq4[r], 'harmonic major from the', firstq4[r+1], ',two octaves.\n')
            del firstq4[r]
            del firstq4[r]
        else:
            print('\nAll done! =)\n')

        if len(b4) != 0:
            r = random.randrange(0, len(b4), 2)                             # second question
            print('2. Play', b4[r], b4[r+1], 'pentatonic scale, two octaves.\n')
            del b4[r]
            del b4[r]
        else:
            print('All done! =)\n')

        if len(thirdq4) != 0:
            r = random.randrange(0, len(thirdq4), 3)                     # third question
            print('3. Play', thirdq4[r], thirdq4[r+1],'spread voicing starting from', thirdq4[r+2], ',one octave.\n')
            del thirdq4[r]
            del thirdq4[r]
            del thirdq4[r]
        else:
            print('All done! =)\n')

        if len(fourq4) != 0:
            r = random.randrange(0, len(fourq4), 3)                      # fourth question
            print('4. Play', fourq4[r], fourq4[r+1], 'arpeggio from', fourq4[r+2],'two octaves.\n')
            del fourq4[r]
            del fourq4[r]
            del fourq4[r]
        else:
            print('All done! =)\n')

        if len(fifq4) != 0:
            r = random.randrange(0, len(fifq4), 2)                       #fifth question
            print('5. Play', fifq4[r], fifq4[r+1], 'two forms.\n')
            del fifq4[r]
            del fifq4[r]
        else:
            print('All done! =)\n')

        if len(sixq4) != 0:
            r = random.randrange(0, len(sixq4), 3)                       #sixth question
            print('6. Play', sixq4[r], sixq4[r+1], 'arpeggio one octave',sixq4[r+2],'.\n')
            del sixq4[r]
            del sixq4[r]
            del sixq4[r]
        else:
            print('All done! =)\n')
        
    elif x == 'clear':

        firstq = []
        for i in range(len(a)): # first question list with all posibilities
                for j in range(len(scale)):
                    firstq.extend([a[i], scale[j]])

        b = a[:] # second question list

        thirdq = []
        for i in range(len(a)): # third question list with all posibilities
                for j in range(len(triad)):
                    thirdq.extend([a[i], triad[j]])

        fourq = thirdq[:] # fourth

        fifq = []
        for i in range(len(a)): # fifth question list with all posibilities
                for j in range(len(fpart)):
                    fifq.extend([a[i], fpart[j]])

        sixq = []
        for i in range(len(a)): # sixsth question list with all posibilities
                for j in range(len(arp1)):
                    sixq.extend([a[i], arp1[j]])

        # ************************************************* level 2

        firstq2 = []
        for i in range(len(a)): # first question list with all posibilities
                for j in range(len(scale2)):
                    firstq2.extend([a[i], scale2[j]])

        b2 = a[:] # second question list

        thirdq2 = []
        for i in range(len(a)): # third question list with all posibilities
                for j in range(len(triad)):
                    thirdq2.extend([a[i], triad[j]])

        fourq2 = thirdq2[:] # fourth

        fifq2 = []
        for i in range(len(a)): # fifth question list with all posibilities
                for j in range(len(fpart2)):
                    fifq2.extend([a[i], fpart2[j]])

        sixq2 = []
        for i in range(len(a)): # sixsth question list with all posibilities
                for j in range(len(arp4)):
                    sixq2.extend([a[i], arp4[j]])

        # ************************************************** level 3

        firstq3 = []
        for i in range(len(a)): # first question list with all posibilities
                for j in range(len(scale3)):
                    firstq3.extend([a[i], scale3[j]])

        b3 = a[:] # second question list

        thirdq3 = []
        for i in range(len(a)): # third question list with all posibilities
                for j in range(len(triad)):
                    for k in range(len(invtriad)):
                        thirdq3.extend([a[i], triad[j], invtriad[k]])

        fourq3 = [] # fourth quesiton list
        for i in range(len(a)):
            for j in range(len(triad)):
                for k in range(len(invtriad)):
                    fourq3.extend([a[i], triad[j], invtriad[k]])

        fifq3 = []
        for i in range(len(a)): # fifth question list with all posibilities
                for j in range(len(fpart)):
                    fifq3.extend([a[i], fpart[j]])

        sixq3 = []
        for i in range(len(a)): # sixsth question list with all posibilities
                for j in range(len(arp1)):
                    for k in range(len(invfour)):
                        sixq3.extend([a[i], arp1[j], invfour[k]])

        # ************************************************* level 4

        firstq4 = []
        for i in range(len(a)): # first question list with all posibilities
                for j in range(len(scale4)):
                    firstq4.extend([a[i], scale4[j]])

        b4 = [] # second question list
        for i in range(len(a)):
            for j in range(len(striad)):
                b4.extend([a[i], striad[j]])

        thirdq4 = []
        for i in range(len(a)): # third question list with all posibilities
                for j in range(len(triad)):
                    for k in range(len(invtriad)):
                        thirdq4.extend([a[i], triad[j], invtriad[k]])

        fourq4 = [] # fourth quesiton list
        for i in range(len(a)):
            for j in range(len(triad)):
                for k in range(len(invtriad)):
                    fourq4.extend([a[i], triad[j], invtriad[k]])

        fifq4 = []
        for i in range(len(a)): # fifth question list with all posibilities
                for j in range(len(fpart2)):
                    fifq4.extend([a[i], fpart2[j]])

        sixq4 = []
        for i in range(len(a)): # sixsth question list with all posibilities
                for j in range(len(arp4)):
                    for k in range(len(invfour)):
                        sixq4.extend([a[i], arp4[j], invfour[k]])
        
        print('\nMemory Reset\n')
           
    elif x == 'stop':

        print('\nProgram terminated.\n')
    
    elif x == 'demo':
         
         firstq = []
         b  = []
         thirdq =[]
         fourq =[]
         fifq =[]
         sixq =[]
         firstq2 = []
         b2  = []
         thirdq2 =[]
         fourq2 =[]
         fifq2 =[]
         sixq2 =[]
         firstq3 = []
         b3  = []
         thirdq3 =[]
         fourq3 =[]
         fifq3 =[]
         sixq3 =[]
         firstq4 = []
         b4  = []
         thirdq4 =[]
         fourq4 =[]
         fifq4 =[]
         sixq4 =[]

    else:

        print('\nLevel entered is invalid. Please enter a level from 1-4 or type "clear" to reset the memory.\n')

