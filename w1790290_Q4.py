# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.    # Any code taken from other sources is referenced within my code solution.  
  
# Student ID: 20191026 / W1790290               # Date:  17/04/2020



progress=0
trailer=0
retriever=0
exclude=0

x=[120,100,100,80,80,80,60,60,60,60]  #List of pass_credits
y=[0,20,0,40,20,0,60,40,20,0]         #List of defer_credits
z=[0,0,20,0,20,40,0,20,40,60]         #List of fail_credits


count=0
for i in range(0,len(x)):
      if x[i]==120:
        print("progress")
        progress+=1
        count+=1
for i in range(0,len(x)):
      if x[i]==100:
         print("progress-module trailer")
         trailer+=1
         count+=1
for i in range(0,len(x)) and range(0,len(z)):
      if x[i]<=80 and z[i]<=60:
         print("Do not progress-module retriever")
         retriever+=1
         count+=1
for i in range(0,len(z)):
      if z[i]>=80:
          print("Exclude")
          exclude+=1
          count+=1
         
         


print("Progress ",progress,":",(progress)*"*")
print("Trailer  ",trailer,":",(trailer)*"*")
print("Retriever",retriever,":",(retriever)*"*")
print("Exclude ",exclude,":",(exclude)*"*")
print(count,"outcomes in total.")
