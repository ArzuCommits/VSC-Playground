import random
class kbc:
   a = "1: The International Literacy Day is observed on:\nA) Sep 8\nB) Nov 28\nC) May 2\nD) Sep 22"
   b = "2: What is the capital of Australia?- \na) Sydney\nb) Melbourne \nc) Canberra \nD) Brisbane"
   c = "3: Which river flows through Egypt? -\na) Nile \nb) Amazon \nc) Mississippi \nd) Ganges"
   d = "4: What is the chemical symbol for gold? - \na) Go \nb) Au \nc) Ag \nd) Pt"
   e = "5: Which planet is known as the 'Red Planet'? - \na) Venus \nb) Mars \nc) Jupiter \nd) Saturn"
 
   qns = [a , b , c , d , e]
   ans = { 0 : "a" , 1 : "a" , 2 : "a" , 3 : " b" , 4 : "b"}
   sc = 0
   print("Enter the option number only and we will let you know whether it it was corect or not: \n")
   
   for i in range (len(qns)):
       print("\n"+qns[i])
       user_input = input("\nEnter your option: ")
       if user_input.isdigit() == True:
           print("PLease type only options/letters")
           sc -= 1
           continue
       else:
           user_input.lower()
           
       if user_input == ans[i]:
            print("\ncorrect!\n")
            sc += 1
       else:
           print("\nNo,\nAns= option "+ans[i])
           
   print("You got "+str(sc)+" questions right out of "+str(len(qns)))
       