# importing the dbm package
import dbm

# using the open function
# to create a new database named
# 'mydb' in 'n' mode, object
# returned in db variable.
db = dbm.open('mydb','n')

# inserting the new key and
# values in the database.
db['name'] = 'GeeksforGeeks'
db['phone'] = '8888'
db['Short name'] = 'GfG'
db['Date'] = '01/01/2000'

# getting and printing
# the value through get method.
print(db.get('name'))
print()

# printing the values of
# database through values()
# method (iterator).
for value in db.values():
	print(value)
print()

# printing the values through
# key iterator.
for key in db.keys():
	print(db.get(key))
print()

# poping out the key, value
# pair corresponding to
# 'phone' key.
db.pop('phone')

# printing the key, value
# pairs present in database.
for key, value in db.items():
	print(key, value)

# clearing all the key values
# in database.
db.clear()

# Below loop will print nothing
# as database is cleared above.
for key, value in db.items():
	print(key, value)

# closing the database.
db.close()

# This code is contributed by Amit Mangal.
