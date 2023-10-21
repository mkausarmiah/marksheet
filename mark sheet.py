
bangla = int(input('Give Bangla mark= '))
english = int(input('Give English mark= '))
math = int(input('Give Math mark= '))

#For bangla grate:
if bangla >= 80 and bangla <= 100:
    print('Bangla= A+')
elif bangla >= 70 and bangla <= 79:
    print('Bangla= A')
elif bangla >= 60 and bangla <= 69:
    print('Bangla= A-')
elif bangla >= 50 and bangla <= 59:
    print('Bangla= B')
elif bangla >= 33 and bangla <= 49:
    print('Bangla= c')
elif bangla >= 1 and bangla <= 32:
    print('Bangla= F')
else:
	print('Enter the correct number in Bangla subject')

#For English grate:
if english >= 80 and english <= 100:
    print('Engliah= A+')
elif english >= 70 and english <= 79:
    print('Engliah= A')
elif english >= 60 and english <= 69:
    print('English= A-')
elif english >= 50 and english <= 59:
    print('English= B')
elif english >= 33 and english <= 49:
    print('Engliah= C')
elif english >= 1 and english <= 32:
    print('English= F')        
else:
	print('Enter the correct number in English subject')
	
# For math grate   
if math >= 80 and math <= 100:
    print('Math= A+')
elif math >= 70 and math <= 79:
    print('Math= A')
elif math >= 60 and math <= 69:
    print('Math= A-')
elif math >= 50 and math <= 59:
    print('Math= B')
elif math >= 33 and math <= 49:
    print('Math= C')
elif math >= 1 and math <= 32:
    print('Math= F')        
else:
	print('Enter the correct number in Math subject')                