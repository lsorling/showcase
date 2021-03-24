# Password Module

Write a password module named "Password.py"

Need 2 functions:

----

## generate()
return generated password as a String

* a function that will generate a random password
of length 10 characters using alphabets, digits
and special characters like ~!@#$%^&*()
return this random string

For example: generate() -> "b395cdh#%c"

----

## strength_checker()
takes in 1 input parameter: a password

* a function that will check the strength of the
given password string using these rules:
<ol>
<li>"invalid" if length of password is less than
10 characters</li>
<li>"weak" if password is all alphabets
"medium" if password contains both alphabets
         and digits (or alphabets and special characters)</li>
<li>"strong" if password contains either alphabets,
         digits or special characters.</li>
</ol>

For example: strength_checker('Pass~!@#4567') -> "strong"

----
End of Document
