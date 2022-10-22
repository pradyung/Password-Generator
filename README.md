# Password Generator

## Introduction
This module provides a simple password generating algorithm that can be used with the ```generatePassword()``` function.

## Details
```generatePassword()``` takes three arguments:
* ```length```: The length of the password generated. Defaults to ```10```.

* ```caseSensitive```: If this is set to ```True```, the password will contain uppercase letters, lowercase letters, and numbers. If it is ```False```, the password will only contain uppercase letters and numbers. Defaults to ```True```.

* ```keywords```: A list of words or phrases that the password will contain. If the total length of all words in this list is greater than ```length```, none of the keywords will be in the password. If any of the words contain spaces, the spaces will be ignored. Defaults to ```[]```.

The function can be called with any or all of the parameters omitted, and will still return a password with the default parameters.

## Purpose
This module is a simple way to generate random strings of characters. Its intended use is for creating secure passwords for logins, but it can also be implemented in encryption algorithms to safely transmit sensitive information over the Internet.