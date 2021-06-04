# while loops
number = 1

while number < 5:
    print(number)
    number += 1


# for loops

for i in range(51):
    print(i)

# contraints(every other number, from 0-50)

for i in range(0,51,2):
    print(i)

# iterating through a collection of data

animals = ["cow", "pig", "duck"]

for animal in animals:
    print(animal)

# break ( print the numbers 1-20 then stop)

for i in range(101):
    print(i)
    if i == 20:
        break

# continue(This will print the numbers 1-20 except for the number 5. when i = 5 it will break out then continue with the next iteration
)
for i in range(20):
    if i == 5:
        continue
    print(i)

