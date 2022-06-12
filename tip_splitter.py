#print welcome
print ("Tip calculator \n")
#scrivere il conto totale
bill = float(input("What was the toal bill ? $"))
#inserire l'ammontare della mancia
tip = int(input("How much tip would you like to give? 10,12 or 15? "))
#inserire il numero di persone con cui dividere il conto
people = int(input("How many people to split the bill ?"))

tip_as_a_percent= tip / 100
#calcolo totale della mancia
total_tip_amount= bill * tip_as_a_percent
total_bill= bill + total_tip_amount
bill_per_person= total_bill / people
#totale arrotondato
final_amount=round(bill_per_person,2)
#stampa del totale 
print(f"Each person must pay ${final_amount}")
#f all'inizio serve per inserire una variabile all'interno dell virgolette
#a patto che sia scritta nelle parentesi graffe
