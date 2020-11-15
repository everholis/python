
# example_001


# list
names = ["david", "jack", "bob"]
lst = [1, 2, "hello", "hi"]
lst[0] = 10
lst.append("bye")


# tuple 
# data of tuple is not modified
tp1 = ()
tp2 = (1,)
tp3 = (10,20,30)
tp4 = 100,200,300


# dictionary
user = {}
user["age"] = 32
user["address"] = "indiana"


#
print("names:", names)
print("names[0]:", names[0])
print("names[1]:", names[1])
print("names[2]:", names[2])

print("lst:", lst)
print("lst[2]:", lst[2])

#
print("tp2:", tp2)
print("tp2[0]:", tp2[0])
print("tp3:", tp3)
print("tp4:", tp4[1])

#
print("user:", user)
print("user[age]:", user["age"])
print("user[address]:", user["address"])


print("done")


"""
[output]

('names:', ['david', 'jack', 'bob'])
('names[0]:', 'david')
('names[1]:', 'jack')
('names[2]:', 'bob')
('lst:', [10, 2, 'hello', 'hi', 'bye'])
('lst[2]:', 'hello')
('tp2:', (1,))
('tp2[0]:', 1)
('tp3:', (10, 20, 30))
('tp4:', 200)
('user:', {'age': 32, 'address': 'indiana'})
('user[age]:', 32)
('user[address]:', 'indiana')
done
"""