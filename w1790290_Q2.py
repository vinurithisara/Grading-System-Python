# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.    # Any code taken from other sources is referenced within my code solution.  
  
# Student ID: 20191026/w1790290             # Date: 17/04/2019





progression=0  #count of total students
progress=0    #count of progress
trailer=0      #count of Progress – module trailer
retriever=0    #count of Do not progress – module retriever
excluded=0     #count of Excluded

def result():
    global progression
    global progress
    global trailer
    global retriever
    global excluded
    if pass_credits+defer_credits+fail_credits!=120:
         print("Total error")
         inputs()
    
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

def histogram():
    print("Progress ",progress,":",(progress)*"*")
    print("Trailer  ",trailer,":",(trailer)*"*")
    print("Retriever",retriever,":",(retriever)*"*")
    print("Excluded ",excluded,":",(excluded)*"*")
    print(progression,"outcomes in total.")

def inputs():     #Get inputs
 global pass_credits
 global defer_credits
 global fail_credits
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
inputs()     #functions call
result()
decision=input("Enter 'q' to quit or else to repeat")
while True:
 if decision=='q':   #exit
        histogram()
        print("Program will quit...")
        break
 else:
     inputs()
     result()
     decision=input("Enter 'q' to quit or else to repeat")










