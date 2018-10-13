# Create a function takes in a string and returns
# the reverse of that string

def stringReversal(str):
    chars = list(str)
    for i in range(len(str) // 2):
        temp = chars[i]
        chars[i] = chars[len(str) - i - 1]
        chars[len(s) - i - 1] = temp
    return ''.join(chars)
