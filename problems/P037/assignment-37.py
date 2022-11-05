answer=input("Would you like to run this with sample input(y/n)?")
if answer=="y":
    passage="""Today is president resignation date, a vantage point in history of 
    our country.You, the next generation of this soil, will decide who should take
     control of your country."""
    stop_words=["soil","president","vantage","country"]
else:
    passage=input("Enter a passage:")
    stop_words=input("Enter stop words").split()    
for i in stop_words:
    passage=passage.replace(i,"")
print(passage)        
