# Create a list comprehension that returns a list of even numbers
# from 1 - 20 (20 included)

if __name__ == '__main__':
    my_list = [i for i in range(0, 21) if i % 2 == 0]
    print(my_list)
