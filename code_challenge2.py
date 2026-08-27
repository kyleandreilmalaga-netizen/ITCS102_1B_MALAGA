#code challenge

money = 19836

bill_1000 = money // 1000
money = money % 1000
bill_500 = money // 500
money = money % 500
bill_200 = money // 200
money = money % 200
bill_100 = money // 100
money = money % 100
bill_50 = money // 50
money = money % 50
bill_10 = money // 10
money = money % 10

print("1000:", bill_1000)
print("500:", bill_500)
print("200:", bill_200)
print("100:", bill_100)
print("50:", bill_50)
print("10:", bill_10)
print("Remaining:", money)