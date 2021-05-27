# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.    # Any code taken from other sources is referenced within my code solution.  
  
# Student ID: 20191026 /W1790290               # Date:  17/04/2020  



def result():
 
    if pass_credits+defer_credits+fail_credits!=120:
         print("Total error")
         inputs()
    if pass_credits==120:    #grade system
             print("progress")
    elif pass_credits==100:
             print("Progress – module trailer")
    elif 0<=pass_credits<=80 and 0<=defer_credits<=120 and 0<=fail_credits<=60:
             print("Do not progress – module retriever")
    elif 0<=pass_credits<=40 and 0<=defer_credits<=40 and 0<=fail_credits<=120:
             print("Exclude")
      
def inputs():
 global pass_credits
 global defer_credits
 global fail_credits
 while True:
    pass_credits =input("Please enter pass_credit: ")   #Get pass_credits
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
  defer_credits =input("Please enter defer_credit: ")  #Get defer_credits
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
  fail_credits =input("Please enter fail_credit: ")    #Get fail_credits
  try:
     fail_credits =int(fail_credits)
     if fail_credits in [0,20,40,60,80,100,120]:
       break
     else:
         print("Range error")
         pass     
  except ValueError:
     print("Integers required!")
inputs()  #call functions
result()

