
# example_001

# for [variable] in [string, list, tuple] :

s = "helloworld"
for i in s:
    if i == "e":
        print("e is found, break")
        break

ary = [1,2,3]
for i in ary:
    if i == 2:
        continue

    print(i)


for i in range(0, 3):
    print(i)


print("done")


"""
[output]

e is found, break
1
3
0
1
2
done
"""