progression=0
progress=0
trailer=0
retriever=0
excluded=0

def stars():
    print("    *     ", "\t",end="")

def blank():
    print("          ","\t", end="")

def result():
    global progression  #count of students
    global progress     #count of progress
    global trailer      #count of Progress – module trailer
    global retriever    #count of Do not progress – module retriever
    global excluded     #Excluded
    if pass_credits+defer_credits+fail_credits!=120:
         print("Total error")
    else:
        progression+=1
        if pass_credits==120:
             print("progress")
             progress+=1
        elif pass_credits==100:
             print("Progress – module trailer")
             trailer+=1
        elif 0<=pass_credits<=80 and 0<=defer_credits<=120 and 0<=fail_credits<=60:
             print("Do not progress – module retriever")
             retriever+=1
        elif 0<=pass_credits<=40 and 0<=defer_credits<=40 and 0<=fail_credits<=120:
             print("Excluded")
             excluded+=1


   

while True:      
    while True:
        pass_credits =input("Please enter pass_credit: ")
        try:
            pass_credits =int(pass_credits)
            if pass_credits in [0,20,40,60,80,100,120]:
                break
            else:
                print("Range error")
                pass
                             
        except ValueError:
            print("Integers required!")
    while True:
      defer_credits =input("Please enter defer_credit: ")
      try:
         defer_credits =int(defer_credits)
         if defer_credits in [0,20,40,60,80,100,120]:
           break
         else:
             print("Range error")
             pass
         
      except ValueError:
         print("Integers required!")

    while True:
      fail_credits =input("Please enter fail_credit: ")
      try:
         fail_credits =int(fail_credits)
         if fail_credits in [0,20,40,60,80,100,120]:
           break
         else:
             print("Range error")
             pass     
      except ValueError:
         print("Integers required!")

    result()
    decision=input("Enter 'q' to quit or else to repeat:")
    if decision=='q':      #exit
        print(progression,"outcomes in total.")
        break
    
list=[progress,trailer,retriever,excluded]   # display histogram
max_count=max(list)
print("progress\ttrailer \tretriever\texcluded")
while max_count>0:
    if progress!=0:
       stars()
       progress-=1
    else:
        blank()
    if trailer!=0:
        stars()
        trailer-=1
    else:
        blank()
    if retriever!=0:
       stars() 
       retriever-=1
    else:
        blank()
    if excluded!=0:
        stars()
        excluded-=1
    else:
        blank()
    max_count=max_count-1
    print()
    
        







   




                            
