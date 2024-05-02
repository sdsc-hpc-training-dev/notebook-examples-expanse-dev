# SDSC Expanse Notebook: Boring_Python
## Import Module:
- pathlib
- os 
- pyinputplus
- pyip
- pyperclip
- re
- sys
- pprint 
- random
- copy

## Launch Galyleo:
For specific information about launching Galyleo, please refer to [this GitHub repository](https://github.com/mkandes/galyleo).

## Environment Modules:
By utilizing `--env-modules`, we can load any software installed in Expanse. 
For instance, executing this command line will load CPU modules and Anaconda3 within the Jupyter session.
  - CPU:
`--env-modules cpu/0.17.3b,anaconda3`
- GPU:
This is the following command.
```
galyleo launch --account abc123 --partition shared --cpus 2 --memory 4 --time-limit 00:30:00 --env-modules cpu/0.17.3b,anaconda3/2021.05
```
## Install Modules
To run Boring Python Notebooks you'll need to install 'pyinputplus' and 'pyperclip', as Python3 doesn't include these modules by default.
 * pyinputplus
 * pyperclip

##Location 

Boring_Python
├── [boring_python_chapter_1.ipynb](./boring_python_chapter_1.ipynb)\
├── [boring_python_chapter_2.ipynb](./boring_python_chapter_2.ipynb)\
├── [boring_python_chapter_3.ipynb](./boring_python_chapter_3.ipynb)\
├── [boring_python_chapter_4.ipynb](./boring_python_chapter_4.ipynb)\
├── [boring_python_chapter_5.ipynb](./boring_python_chapter_5.ipynb)\
├── [boring_python_chapter_6.ipynb](./boring_python_chapter_6.ipynb)\
├── [boring_python_chapter_7.ipynb](./boring_python_chapter_7.ipynb)\
├── [boring_python_chapter_8.ipynb](./boring_python_chapter_8.ipynb)\
├── [boring_python_chapter_9.ipynb](./boring_python_chapter_9.ipynb)\
├── README.md

##Table of Contents
| Chapter   | Package Dependencies  | Keywords                                | Short Description |
| --------- | --------------------  | --------                                       | ----------------- |
| Chapter 1: Python Basics   | N/A                   | basic, data types, math, operator              | This notebook begins with running expressions into the interactive shell, python math operations, and variable types. It also includes basic string functions and concatenation. |
| Chapter 2: Flow Control    | math, os, random, sys | basic, flow control, flowchart, loops, modules | This notebook dives into booleans, comparison and logic operators, and the elements of flow control, including if/else conditionals and while and for loops. Importing python modules is also explained.                  |
| Chapter 3: Functions       | random                | basic, exceptions, functions, variable scope   | This notebook discusses the basics of functions, parameters, and return statements. It also explains the local and global scope of variables and how to handle exceptions and errors in code. |
| Chapter 4: Lists           | N/A                   | basic, index, lists, loops, slice, tuples      | This notebook overviews all topics related to lists: indexes, slicing, length, concatenation, removing values. It provides examples for how to implement lists with inputs and loops. |
| Chapter 5: Dictionaries and Structuring Data | pprint                | basic, data structures, dictionaries, lists, nested data| This notebook explains dictionaries and the methods associated with them. It implements the pprint module to demonstrate how to "pretty print" dictionary values. The chapter also includes examples for utilizing lists and dictionaries to model real-world applications. |
| Chapter 6: Manipulating Strings | pyperclip, sys        | basic, strings, index, slice                   | This notebook explores all things for strings, including indexing, spliting, justifying, removing whitespace, and many more methods. Chapter 6 also has 2 project examples to show the use of the pyperclip module.|
| Chapter 7: Pattern Matching with Regular Expressions | pyperclip, regular expressions/re|patterrns, text processing, webscraping|This notebook examines how to find text patterns with and without regular expressions. Additional topics include matching multiple groups, matching specific repetitions, character classes, substitutin strings, and more with the regex module.|
| Chapter 8: Input Validation | pyinputplus          |input/output, input validation, keys, keywords| This notebook reviews input validation that checks values entered by a user. The PyInputPlus module methods are used to verify text inputs, set a limit to user inputs, create custom validation logic, etc. |
| Chapter 9: Reading and Writing Files | pathlib, os, shelve, pprint, myCats|file processing, reading, writing|This notebook examines the basics of file paths and how to use the interactive shell on various operating systems. It goes over how to open, read, and write to files, as well as how to save and format variables with the shelve and pprint modules.|

# Sources
These notebooks are adapted from the e-book *Automate the Boring Stuff* by Al Sweigart. The original ebook can be found [here](https://automatetheboringstuff.com/). 
These are adapted to run on HPC systems. They contain fundemental Python knowledge, projects and examples included. Enjoy!


