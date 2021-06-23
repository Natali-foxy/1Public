per_cent={}
per_cent['ТКБ']=5.6
per_cent['СКБ']=5.9
per_cent['ВТБ']=4.28
per_cent['СБЕР']=4.0
print(per_cent)

money=input('Введите сумму вклада:')
print("Ваша первоначальная сумма = ", money)
a=int(money)
deposit1=a*per_cent['СКБ']
deposit2=a*per_cent['ВТБ']
deposit3=a*per_cent['СБЕР']
deposit4=a*per_cent['ТКБ']
print('Ваши накопления за год в СКБ = ',deposit1,
      '\nВаши накопления за год в ВТБ =',deposit2,
      '\nВаши накопления за год в СБЕР =',deposit3,
      '\nВаши накопления за год в ТКБ =',deposit4)

deposit_all=(deposit1,deposit2,deposit3,deposit4)
a = list(deposit_all) #нужно теперь привести список к виду целые числа и найти там максимальное значениеint(deposit_all[])

map(int,a)
max_value = max(int(a) for a in deposit_all)

print('Максимальная сумма, которую вы можете заработать= ', max_value)





