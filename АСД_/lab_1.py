string = '()[({}())]'
right = True
stack = []
for i in string:
    if i in '([{':
        stack.append(i)
    elif i in ')]}':
        if not stack:
            right = False
            break   
        openbracket = stack.pop()
        if openbracket == '(' and i ==')' or '[' and i ==']' or '{' and i =='}':
            continue
        right = False
        break
if right and len(stack)==0:
    print('Yes')
else:
    print ('No')
                
            
          

    
