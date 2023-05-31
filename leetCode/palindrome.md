    @param
    x [Number]
    check if the number is palindrome( read the same when reverse )
    return Boolean

# solution #1

- change to string and array
- reverse it and join it
- compare and return

# solution #2

```
originalNumber: 543
reverseNumber: 0
```

> Get the last digit of the original number

`original % 10 = 543 % 10 = 3`

> Put this digit as the last one in the reverse number

```reverse * 10 + digit = 0 * 10 + 3 = 0 + 3 = 3
reverse: 3
```

> Remove this digit from the original number

```
original / 10 = 543 / 10 = 54.3
~~54.3 = 54
original: 54
```

> > Repeat

```
original % 10 = 54 % 10 = 4
reverse * 10 + digit = 3 * 10 + 4 = 30 + 4 = 34
reverse: 34
original / 10 = 54 / 10 = 5.4
~~5.4 = 5
original: 5
```

> > Repeat

```
original % 10 = 5 % 10 = 5
reverse * 10 + digit = 34 * 10 + 5 = 340 + 5 = 345
reverse: 345
original / 10 = 5 / 10 = 0.5
~~0.5 = 0
original: 0

input: 543
output: 345
```

\*the core concept is this

the factor between 1000, 100, 10 is 10 so you can get every last digit of the number by modulo of 10 so by collecting the every last digit you can reverse it.\*
