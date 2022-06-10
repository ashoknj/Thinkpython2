######       Exercise  2.1 1 
# The volume of a sphere with radius r is 4/3 pi r3 . What is the volume of a sphere with
#radius 5?
print(4/3*3.141*(5**3))

#####        Exercise 2.1  question 2
price=24.95-(24.95*0.4)
print(price)
total_order=60
# whole sale price for 60 copies
whole_price=price*total_order+3+(total_order-1)*0.75
print("Total whole sale price :"+str(whole_price))

######        Exercice 2.1 question 3
easy_min=8*2
easy_sec=15*2
tempo_min=7*3
tempo_sec=12*3
final_sec=(easy_sec+tempo_sec)-60
final_min=easy_min+tempo_min+1
reach_min=52+final_min-60
reach_hour=6+1
print("Reaching home at "+str(reach_hour)+":"+str(reach_min)+ " am")


