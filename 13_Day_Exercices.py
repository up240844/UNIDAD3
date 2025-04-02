numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numNeg = [i for i in numbers if i <= 0]
print(numNeg)


list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [ number for row in list_of_lists for number in row]
flattened_list2 = [ number for row in flattened_list for number in row]
print(flattened_list2)


tuples = [(i,1, i**1 ,i**2,i**3,i**4,i**5,) for i in range(11)]
print(tuples)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] 
                       for sublist in countries for (country, capital) in sublist]
print(flattened_countries)


dicctionary_countries = [{'country':country.upper(),'city':city.upper()} for sublist in countries 
                         for (country,city) in sublist]
print(dicctionary_countries)


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_name = [[name + " " + lastname] for sublist in names for (name,lastname) in sublist]
full_name = [i for n in full_name for i in n]
print(full_name)


slope = lambda x1,y1,x2,y2 : (y2-y1)/(x2-x1)
print(slope(3,5,4,1))
