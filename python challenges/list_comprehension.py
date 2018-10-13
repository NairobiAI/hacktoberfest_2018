# Create a list comprehension that returns a list of even numbers
# from 1 - 20 (20 included)
l=[]
t=0
for i in range(1,21):
    if i%2==0:
        l[t]=i
        t=t+1
