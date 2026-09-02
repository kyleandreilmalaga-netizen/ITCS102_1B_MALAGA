#code challenge

money = 19836

print("================== PH BANK DENOMINATION =================")
print(" MONEY TO DEPOSIT ------------->  ", money, "php")


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
bill_20 = money // 20
money  = money % 20
bill_10 = money // 10
money = money % 10
bill_5 = money // 5
money = money % 5

print("1000:", bill_1000)
print("500:", bill_500)
print("200:", bill_200)
print("100:", bill_100)
print("50:", bill_50)
print("20:", bill_20)
print("10:", bill_10)
print("5:", bill_5)
print("Remaining:", money)

