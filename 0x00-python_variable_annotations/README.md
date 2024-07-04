Python Variable Annotations Project
Introduction
This project is focused on understanding and utilizing type annotations in Python 3. The tasks involve creating functions with specific type annotations, defining variables with type annotations, and using type annotations with more complex data structures like lists and tuples. Additionally, we will explore duck typing and validating code using mypy.

Requirements
Allowed editors: vi, vim, emacs
Environment: All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
Code style: All code should adhere to the pycodestyle style (version 2.5)
File format:
All files must end with a new line
The first line of all files should be exactly #!/usr/bin/env python3
All files must be executable
The length of files will be tested using wc
Documentation:
Each module should have a documentation string (__doc__)
Each class should have a documentation string
Each function (inside and outside of a class) should have a documentation string
Documentation should be a real sentence explaining the purpose of the module, class, or function
Tasks
Task 0: Basic Annotations - Add
Write a type-annotated function add that takes two floats a and b as arguments and returns their sum as a float.

File: 0-add.py

Task 1: Basic Annotations - Concat
Write a type-annotated function concat that takes two strings str1 and str2 as arguments and returns a concatenated string.

File: 1-concat.py

Task 2: Basic Annotations - Floor
Write a type-annotated function floor which takes a float n as an argument and returns the floor of the float.

File: 2-floor.py

Task 3: Basic Annotations - To String
Write a type-annotated function to_str that takes a float n as an argument and returns the string representation of the float.

File: 3-to_str.py

Task 4: Define Variables
Define and annotate the following variables with the specified values:

a: an integer with a value of 1
pi: a float with a value of 3.14
i_understand_annotations: a boolean with a value of True
school: a string with a value of "Holberton"
File: 4-define_variables.py

Task 5: Complex Types - List of Floats
Write a type-annotated function sum_list which takes a list input_list of floats as an argument and returns their sum as a float.

File: 5-sum_list.py

Task 6: Complex Types - Mixed List
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.

File: 6-sum_mixed_list.py

Task 7: Complex Types - String and Int/Float to Tuple
Write a type-annotated function to_kv that takes a string k and an int or float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.

File: 7-to_kv.py

Task 8: Complex Types - Functions
Write a type-annotated function make_multiplier that takes a float multiplier as an argument and returns a function that multiplies a float by multiplier.

File: 8-make_multiplier.py

Task 9: Let's Duck Type an Iterable Object
Annotate the function element_length’s parameters and return values with the appropriate types.

python
Copy code
def element_length(lst):
    return [(i, len(i)) for i in lst]
File: 9-element_length.py

Validation
Use mypy to validate the type annotations in your code.
Ensure all files are executable.
Verify that all code adheres to pycodestyle style guidelines.
Ensure all modules, classes, and functions have appropriate documentation.
Usage
To run the provided examples, ensure your Python environment is set up and execute the main script for each task:

bash
chmod +x <filename>.py
./<filename>.py
For example, to run the script for Task 0:

bash
chmod +x 0-main.py
./0-main.py

Conclusion
By completing this project, you will gain a deeper understanding of type annotations in Python, how to specify function signatures and variable types, and how to use mypy for type validation.#alx-backend-python
