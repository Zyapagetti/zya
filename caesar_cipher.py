import string

step = int(input("몇단계?: "))%26
quiz = input("문장을입력: ").upper()
print("Input: " + quiz)

arr = list(string.ascii_uppercase)
print("AtoZ array:")
print(arr)

key = []
result = []

for i in range(len(arr)):
    if i < step:
        key.append(arr[i+len(arr)-step])
    else:
        key.append(arr[i-step])

print("encryption key:")
print(key)

arr_quiz = list(quiz)

print("Input array:")
print(arr_quiz)

for i in range(len(arr_quiz)):
    ind = arr.index(arr_quiz[i])
    result.append(key[ind])

print("Output array:")
print(result)

print("Output: " + ''.join(result))
