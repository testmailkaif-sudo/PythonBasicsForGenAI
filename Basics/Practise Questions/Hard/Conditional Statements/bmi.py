rank = 28.4
bmi ={
    rank >=30 :"Obese",
    25 <= rank <= 29.9 :"Over Weight",
    18.5 <= rank <= 24.9 : "Normnal",
    18.5 > rank : "Under Weight",
}

print(bmi[True])