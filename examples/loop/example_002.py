
# example_001

# while loop-continuation-condition:

sum = 0
i = 0
while i <= 3:
    sum += i
    i += 1

print("sum:", sum)

i = 0
while i < 5:
    if i < 3:
        print("continue, i:", i)
        i += 1
        continue
    else:
        print("break, i:", i)
        break


print("done")


"""
[output]

('sum:', 6)
('continue, i:', 0)
('continue, i:', 1)
('continue, i:', 2)
('break, i:', 3)
done
"""