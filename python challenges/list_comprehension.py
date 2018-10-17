# Create a list comprehension that returns a list of even numbers
# from 1 - 20 (20 included)

# function to include end number in range
def rangeToEnd(start,end):
    return range(start, end+1)

#list comprehension
evenNumberList = [x for x in rangeToEnd(1,20) if x % 2 == 0]

#print even numbers
print(evenNumberList)


