
largest = None
smallest = None
while True:
    enum = 0
    entered = None

    try:
        entered=raw_input("enter a number bizatch")
        if entered == "done":
            break
        else:
            enum = int(entered)
            if smallest == None:
                smallest = enum
            if enum < smallest:
            	smallest = enum
            if enum > largest:
            	largest = enum
            
    except:
        
        print 'Invalid input'
        entered=float(raw_input())
        
        
print 'Maximum is', largest
print 'Minimum is', smallest

