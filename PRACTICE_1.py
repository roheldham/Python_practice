print ("Let's practice everything")
print ("You\'d need to know \'bout escapes \\")

print ('\n newlines and \t tabs')

poem = """
\t This is a poem to show
that we can use triple 
quotations to write multiple lines\n
Cool?
"""

print ("-----------")
print (poem)
print ("-"*10)

def formula(started):
    jellybeans = started/10
    jars = jellybeans*100
    crates = jars/1000
    return jellybeans, jars, crates

start_point = 40000
beans, jars, crates = formula(start_point)
print (f"The number of beans is {beans}\nThe number of jars is {jars}\nThe number of crates is {crates}")

