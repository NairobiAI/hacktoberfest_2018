# Create a function takes in a string and returns
# the reverse of that string

def reverse(string):
    output = ""
    for c in string:
        output = c + output
    return output


if __name__ == '__main__':
    s = "hello world"
    print("{} => {}".format(s, reverse(s)))
