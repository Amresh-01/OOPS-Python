# Ques:1= What is Python? What are the benefits of using Python?
# Ans: Python is a high-level, interpreted, and general-purpose programming language created by Guido van Rossum in 1991.

# It is designed to be simple, readable, and easy to learn, which makes it popular among beginners and professionals alike.

# Python is used in many fields like:

# Web development (e.g., Django, Flask)
# Data science & AI
# Automation & scripting
# Game development
# Cybersecurity

# Benefits of Using Python
# 1. Easy to Learn & Read

# Python has a clean syntax similar to English, so beginners can understand it quickly.

# 2. Interpreted Language

# No need to compile code — you can run it directly, which speeds up development.

# 3. Large Standard Library

# Python comes with many built-in modules (like math, file handling, etc.), so you don’t need to write everything from scratch.

# 4. Cross-Platform

# Python works on Windows, Linux, and macOS without major changes.

# 5. Huge Community Support

# Millions of developers use Python, so finding help, tutorials, and libraries is easy.

# 6. Versatile

# You can use Python for:

# Web apps
# Machine learning (TensorFlow, PyTorch)
# Data analysis (Pandas, NumPy)
# Automation scripts
# 7. Less Code, More Work

# Python allows you to do complex tasks in fewer lines compared to languages like Java or C++.

# 8. Strong Integration

# Python can easily integrate with other languages like C, C++, and Java.











# Question: 2 : What is Dynamically typed Language?
# Ans :  A dynamically typed language is a programming language where you don’t need to declare the data type of a variable explicitly.
# The type is determined automatically at runtime (when the program is running).

# x = 10      # x is an integer
# x = "hello" # now x becomes a string
# Here, the same variable x can store different types of values at different times.










# Question: 3 : What is Interpreted language?
# Ans : An interpreted language executes code line-by-line using an interpreter without prior compilation.
# It makes development faster and debugging easier, but execution is generally slower compared to compiled languages.









# Question: 4 : What is PEP(Python Enhancement Proposal) 8 and why iss it important?
# Ans : PEP 8 is the official style guide for writing Python code.
# It provides a set of rules and best practices to make Python code clean, readable, and consistent.

# Why is PEP 8 Important? (Interview Points)
# 1. Improves Readability
# Code written using PEP 8 is easy to read and understand for anyone.

# 2. Consistency Across Codebase
# All developers follow the same style, which avoids confusion in team projects.

# 3. Better Collaboration
# Makes it easier for teams to work together on large projects.

# 4. Easier Maintenance
# Clean and structured code is easier to debug and update later.

# 5. Professional Coding Standard
# Following PEP 8 shows good coding practices in interviews and real-world jobs.











# Question: 5 : What is Zen of Python?
# Ans : The Zen of Python is a set of guiding principles written by Tim Peters that define best practices for writing 
# clean, readable, and efficient Python code. It emphasizes simplicity, readability, and consistency in programming.










# Question: 6 : Identity Operator (is) vs ==?
# Ans : Identity opeator: The "is" and "is not" keywords are called identity operators that compare objects based on their identity.
#     Equality operator: The "==" and "!=" are called equality operators that compare the objects based on their values.





# List

L=[2,4,5,6,7,7,8,9]
print(L)
# print(sorted(L)) ye original list ko change nahi krega mtl agar print(L)->[2,4,5,6,7,7,8,9]
# but L.sort()  original List ko change kr dega...







# Tuple

# A tuple is similar to list.The difference between the two is that we cannot change the element of a tuple once it is assigned
# whereas we can change the elements of a list.

# ex. t1=(2,) this is single item

# Tupla are faster than List

# zipping tuple
# a=(1,2,3,4)
# b=(5,6,7,8)
# tuple(zip(a,b))







# Set 

# empty set ->  s=set()
# s1={1,2,3} 1d set 
# s2={1,'hello',4,5,(1,2,3)}
# s3=set([1,2,3,4])
# s4={1,2,[3,4]}

# s5={1,2,3}
# s6={3,2,1}
# print(s5==s6) -> true   item same hai