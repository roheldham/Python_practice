Personal_info ={
    'Name' : 'Rohel',
    'Age' : 22,
    'Height' : '181'

}

print (Personal_info)
print (Personal_info['Age'])
print (Personal_info.items())
print (list(Personal_info.items()))
for key, value in list(Personal_info.items()):
    print (key,':' ,value)
