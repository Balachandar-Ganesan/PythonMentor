# -*- coding: utf-8 -*-
"""PythonIntro-001.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nghQFrwJOO0aomhcj5eSMlWcGPzjoITI
"""

###-1
#Python not strongly Typed
NoDataTypeVar =1
print(type(NoDataTypeVar))
NoDataTypeVar = "String"
print(type(NoDataTypeVar))
NoDataTypeVar = 3.14
print(type(NoDataTypeVar))
#print function for generating the output
#type function is used for identifying the inferred data type by Python

###-2

# the function statement starts with def function name and parameters followed by :
#: colon used instead of { like other languages alignment decides where the "code" ends

###-3

def gcd(a,b):
    while b!=0:
      a,b =b, a%b
    return a
print(gcd(42,9))
#beware of while loops... need to ensure the condition becomes true inside the loop at some point of time
#align return to be in line with previous line and see difference in output

###-4

def gcd(a,b):
   if b == 0:  # Base case: if b is 0, a is the GCD
        return a
   else:  # Recursive step: call gcd with b and the remainder of a divided by b
        return gcd(b, a % b)
print(gcd(42,9))
#same function implemented via recursion

###-5

coins =[1,5,10,25]
amount =63
def make_change(coins,amount):
    coins.sort(reverse=True) #Ensure High denominations come first
    selCoins=[]
    for coin in coins: #Highest denomination comes first in the loop
        while amount >= coin:
            amount -= coin #selecting the coin and decreasing the amount
            selCoins.append(coin) #adding the selected coin to collection
    return selCoins
print(make_change(coins,amount))
#What if we do not sort the data .. Try and check
#What if there are constraints on denominations quantity like 25 can not be used more than once.. Play around

###-6 Data Structure - Array
#Create an array for the date 01/01/2000
import array as arr
Y2KArray=arr.array('i',[1,1,2000])

#First element will be accessed via pointer 0. Because The pointer counts how many positions away from first element.
print(Y2KArray[2])
print(Y2KArray[1])
print(Y2KArray[0])
Y2KArray[2]=3000
print(Y2KArray) # output appears as array('i', [1, 1, 3000]) because array implements __str__ method.. Such methods we can see later

###-7 Data Structure - List
primes = []
primes = [2, 3, 5, 7, 11],
print(primes)

###-8 Data Structure - List Addition
items = ['C', 'O', 'G']
total_items=[]
total_items = items + ['N', 'I','Z','A','N','T']
print(total_items)

###-9 Data Structure - List Addition add an Element

total_items.append('AIA')
total_items.append('AIA')
print(total_items)
total_items.remove('AIA')
print(total_items)

###-9 Data Structure - 2D List
MajorPlayers = [["Leander", "Paes"], ["Usha", "PT"], ["Abinav", "Bindra"]]

MajorPlayers[0][1] = "Paes : Bronze Medal"
MajorPlayers[2][1] = "Bindra : Gold Medal"
print(MajorPlayers)

###-9 Data Structure - Dictionary .. Column Name is called Key with the value
student_grades = {"LittleMaster": "Sachin", "Pigeon": "Glen Mcgrath", "Death Whispering": "Michael Holding"}
print(student_grades["Pigeon"])  # Fast access by key
#throws Value Error
print(student_grades["White Lightening"])

###-10 Compare implementation with list with the above using dictionary
Names = [("LittleMaster", "Sachin"), ("Pigeon", "Glen Mcgrath"), ("Death Whispering", "Michael Holding")]
for Name in Names:
    if Name[0] == "Pigeon":
        print(Name[1])

###-11 List Zipping and Unzipping
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

# Zipping two lists
combined_data = list(zip(names, ages))
print("Combined data:", combined_data)

# Unzipping a list of tuples
unzipped_names, unzipped_ages = zip(*combined_data)
print("Unzipped names:", unzipped_names)
print("Unzipped ages:", unzipped_ages)

###-12 List Comprehension

squared_numbers = [x**2 for x in range(1, 6)]

print("Squared numbers:", squared_numbers)

###-13 Dictionary Application
text ="Don’t count the days. Make the days count"
words = text.lower().split()

word_counts = {}  # Initialize an empty dictionary
for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
print(word_counts)

###-13 Reverse Engineer Infix to PostFix (a+b)*c  to  abc*+ ... This is a Class Room Exercise
def infix_to_postfix(infix_expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operator_stack = []
    postfix_output = []

    for char in infix_expression:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
            postfix_output.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix_output.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()  # Discard '('
            else:
                raise ValueError("Mismatched parentheses")
        elif char in precedence:
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence.get(operator_stack[-1], 0) >= precedence[char]):
                postfix_output.append(operator_stack.pop())
            operator_stack.append(char)
        # Handle other characters (like spaces) if necessary, or raise error for invalid characters

    while operator_stack:
        if operator_stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        postfix_output.append(operator_stack.pop())

    return "".join(postfix_output)

# Example usage:
infix_expr = "a+b*c"
postfix_expr = infix_to_postfix(infix_expr)
print(f"Infix: {infix_expr}")
print(f"Postfix: {postfix_expr}")

###-13 While Loop... repeat till true.. Careful Else infinite loop and StackOverFlow
count = 5

while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print(count)

###-13 While Loop... repeat till break
while True:
    name = input("Enter your name (or type 'exit' to quit): ")
    if name == "exit":
        print("Goodbye!")
        break
    print(f"Hello, {name}!")

###-13 While Loop... skip step with continue
num = 0

while num < 10:
    num += 1
    if num % 2 == 0:
        continue  #go to while loop again
    print(f"Odd number: {num}")

###-14 if
strAboutMe="Batsman"
if strAboutMe == "Batsman":
    print("I am a Batsman")

###-15 if  Else
strAboutMe="Bowler" #replace Bowler with Fielder and run one more time
if strAboutMe == "Batsman":
    print("I am a Batsman")
else:
   if strAboutMe == "Bowler":
    print("I am a Bowler")
   else:
    print("Who am I")

###-16 if else elif
#elif is nothing but else: if seen above
strAboutMe="Akash Raj" #replace Bowler with Fielder and run one more time
if strAboutMe == "Batsman":
    print("I am a Batsman")
elif strAboutMe == "Bowler":
    print("I am a Bowler")
elif strAboutMe == "Fielder":
    print("I am a Fielder")
elif strAboutMe == "All-Rounder":
    print("I am a All-Rounder")
elif strAboutMe == "Wicket Keeper":
    print("I am a Wicket Keeper")
elif strAboutMe == "Captain":
    print("I am a Captain")
elif strAboutMe == "Vice-Captain":
    print("I am a Vice-Captain")
else:
    print("Who am I")

#17 Can you moduralize above example .. Reference below
def green_function(color):
    # Execute some code, for example print the color + number "1"
    print(f"{color} 1")
def blue_function(color):
    # Execute some code, for example print the color + number "1"
    print(f"{color} 1")
def red_function(color):
    # Execute some code, for example print the color + number "1"
    print(f"{color} 1")
def pink_function(color):
    # Execute some code, for example print the color + number "1"
    print(f"{color} 1")

colors_dict = {
    "green": green_function,
    "blue": blue_function,
    "red": red_function,
    "pink": pink_function,
}

user_input = input("")
colors_dict.get(user_input)(user_input)

#18 Mutable
name = "Jim"
student = name
name = "Tim"
print(student)  # Jim (immutable)

scores = ["A", "B"]
grades = scores
scores[1] = "C"
print(grades)  # ['A', 'C'] (mutable)

#19 Sets ..Set is Set in Set Theory
citrusfruit:set = {"oranges", "lemons", "limes", "satsumas", "nectarines"}
treefruit:set = {"apples", "pears", "cherries", "plums", "peaches", "plums", "cherries", "oranges", "lemons", "limes"}
stonefruit:set = {"cherries", "plums", "peaches", "nectarines"}

#tree fruit with stones
print(treefruit.intersection(stonefruit))

#tree fruit which are citrus
print(treefruit.intersection(citrusfruit))

#citrus fruit with stones
print(citrusfruit.intersection(stonefruit))

#all stone and all tree fruits
print(stonefruit.union(treefruit))

#all fruit except citrus fruit
print(stonefruit.union(treefruit).difference(citrusfruit))

#19 Tuple.. Data post initialization can not be modified
geolocation = (3.00727, 80.20371)
print(f"Latitude: {geolocation[0]} Longitude: {geolocation[1]}")

#19 Tuple.. Data post initialization can not be modified
geolocation[0] = 50.0000

#19 Tuple.. Data post initialization can not be modified
import collections

geolocation = collections.namedtuple("geolocation", ["latitude", "longitude"])
KathiparaFlyover = geolocation(48.858093, 2.294694)

print(KathiparaFlyover.latitude)
print(KathiparaFlyover.longitude)

#21 Higher Order Function
#function with in function... intEnterNumber simply gathers the number defined with in start
def start(lstStudentsFullList):
    def intEnterNumber():
        intNumber=int(input("Enter Number Of Students"))
        return intNumber
    intNoOfStudents = intEnterNumber()
    lstStudents=lstStudentsFullList

    for intCounter in range(intNoOfStudents):
        strName=input("Enter Name of Student")
        lstStudents.append(strName)
    strContinue =input("Do You Want to Continue Y/N ?")
    if(strContinue=="Y"):
            start(lstStudents)
    else:
        return lstStudents
    return lstStudents

lstStudents=[]
start(lstStudents)
print(lstStudents)

#21 Decorators
def add(x, y):

    return x + y
def multiply(x, y,z):

    return x * y*z
print(add(4,5))
print(multiply(4,5,6))

#21 Decorators
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called with {args} and {kwargs}") #please watch out the double underscore!!!!...Python has plenty of them
        return func(*args, **kwargs)
    return wrapper
@log_args
def add(x, y):

    return x + y
@log_args
def multiply(x, y,z):

    return x * y*z
print(add(4,5))
print(multiply(4,5,6))

#21 Lambda Functions .. Puzzle requires practice
# function name = lambda arguments: expression
lambdaadd = lambda x, y: x + y
print(lambdaadd(5, 3))

#21 Lambda Function
# Traditional approach to generate squares
squares = []
for x in range(1, 6):
    squares.append(x * x)
print(squares)  # Output: [1, 4, 9, 16, 25]

# Using list comprehension for the same task
squares = [x * x for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

#21 Lambda Function
square = lambda x: x * x
print(square(5))  # Output: 25

# Using list comprehension with lambda function to generate squares
squares = [(lambda x: x * x)(x) for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

#21 Lambda Functions
people = [
    ('A', 25),
    ('B', 30),
    ('C', 20)
]

# Sort by age
sorted_people = sorted(people, key=lambda person: person[1])
print(sorted_people)
# Output: [('Cutie', 20), ('Arsh', 25), ('Balli', 30)]

#21 Lambda Functions
num = [1, 2, 3, 4, 5, 6]
# We want to keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, num))
print(evens)
# Output: [2, 4, 6]

#22 Dunder Methods
class TransactionHistory:
    def __init__(self, transactions):
        self.transactions = transactions
        self.index = 0

history = TransactionHistory(["Deposit $100", "Withdraw $50", "Deposit $200"])
for transaction in history:
    print(transaction)

#22 Dunder Methods __iter ,__next
class TransactionHistory:
    def __init__(self, transactions):
        self.transactions = transactions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.transactions):
            raise StopIteration
        transaction = self.transactions[self.index]
        self.index += 1
        return transaction
    def __str__(self) :
      intCounter=0
      strMessage=""
      for transaction in self.transactions:
        intCounter=intCounter+1
        strMessage=strMessage+"transaction" + str(intCounter) + " " +transaction +";"
      return strMessage



history = TransactionHistory(["Deposit $100", "Withdraw $50", "Deposit $200"])
for transaction in history:
    print(transaction)
print(history)

#22 Error Handling
number = 10
divider = 0
result = number / divider

#22 Error Handling
#Exceptions are errors that Python reports when syntactically correct code executes. In python exceptions are derived from BaseExceptionClass
#AssertionError, AttributeError, EOFError, FloatingPointError, ImportError, ModuleNotFoundError, IndexError, MemoryError, and NotImplementedError.

try:
    number = 10
    divider = 0
    result = number / divider
except ZeroDivisionError as error:
    print(error)

#23 Error Handling
try:
    number = 10
    divider = int(input("Please enter the number to use for division? "))
    result = number / divider
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter a number. Data Type Not Integer For Earlier Value. Run Again")
except Exception as error:
    print(f"An exception occurred {error}")
finally:
    if result is not None:
        print(f"The result is {result}")
    else:
        print("Check Error Messages. What Went Wrong?.")
    result =None

#24 Logging
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

players = {
    'Messi': 85,
    'Ronaldo': 78,
    'Mbappé': 90,
    'Neymar': None,  # Missing data
}

for player, passes in players.items():
    if passes is None:
        logging.warning(f"Missing passing data for {player}")
    elif passes < 50:
        logging.info(f"{player} had a low number of passes: {passes}")
    else:
        logging.info(f"{player} had {passes} completed passes.")
#Level | Purpose
#DEBUG | Detailed info for debugging.
#INFO | Confirmation that things work.
#WARNING | Something unexpected happened.
#ERROR | A serious problem occurred.
#CRITICAL | Serious error, program may not continue.

#24 Logging
import logging

logging.basicConfig(
    filename='content/sample_data/match_report.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def analyze_passes(players):
    for player, passes in players.items():
        if passes is None:
            logging.warning(f"Missing data for {player}.")
        elif passes < 50:
            logging.info(f"{player} had low passes: {passes}.")
        else:
            logging.info(f"{player} recorded {passes} passes.")

players = {
        'Messi': 85,
        'Ronaldo': 78,
        'Mbappé': 90,
        'Neymar': None,
    }
logging.info("Starting match analysis...")
analyze_passes(players)
logging.info("Finished match analysis.")

#25 Class Type Safety
# pylint: disable = line-too-long, trailing-whitespace, trailing-newlines, line-too-long, missing-module-docstring, import-error, too-few-public-methods, too-many-instance-attributes, too-many-locals

from typing import List
import re


class Chunker:
    """
    This class provides a way to chunk a given text using different strategies.
    """

    def __init__(self, strategy: dict):
        """
        Initializes the Chunker with a specified strategy.

        :param strategy: a dictionary containing the chunking mode (paragraph or sliding_window)
                         and optional window_size and overlap values for sliding_window mode.
        """
        self.strategy = strategy["mode"]
        if self.strategy not in {"paragraph", "sliding_window"}:
            raise ValueError(f"Invalid chunking strategy: {self.strategy}")

        self.window_size = strategy.get("window_size", 240)
        self.overlap = strategy.get("overlap", 8)

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Removes extra whitespaces from the input text.

        :param text: a string containing the text to be cleaned.
        :return: a cleaned version of the input text.
        """
        # Remove extra whitespaces
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def __call__(self, text: str) -> List[str]:
        if self.strategy == "paragraph":
            return self.paragraph_chunking(text)

        return self.sliding_window_chunking(text)

    def paragraph_chunking(self, text: str) -> List[str]:
        """
        Splits the input text into paragraphs.

        :param text: a string containing the text to be chunked.
        :return: a list of paragraphs extracted from the input text.
        """
        paragraphs = text.split("\n\n")
        cleaned_paragraphs = []
        for paragraph in paragraphs:
            cleaned_paragraph = self.clean_text(paragraph)
            if cleaned_paragraph:
                cleaned_paragraphs.append(cleaned_paragraph)
        return cleaned_paragraphs

    def sliding_window_chunking(self, text: str) -> List[str]:
        """
        Splits the input text into chunks using the sliding window technique.

        :param text: a string containing the text to be chunked.
        :return: a list of chunks generated from the input text.
        """
        if self.window_size is None or self.overlap is None:
            raise ValueError(
                "Window size and overlap must be specified for sliding window chunking."
            )

        text = self.clean_text(text)

        tokens = text.split()

        # If the text contains fewer tokens than window_size, return the text as a single chunk.
        if len(tokens) < self.window_size:
            return [text]

        # Use a list comprehension to create chunks from windows
        step = self.window_size - self.overlap
        # Ensure the range covers the entire length of the tokens
        chunks = [
            " ".join(tokens[i : i + self.window_size])
            for i in range(0, len(tokens) - self.window_size + step, step)
        ]

        return chunks

#25 Type Safety
txtChunker = Chunker({"mode": "sliding_window","window_size":5,"overlap":4})
print(txtChunker(" I am here where are you?. Can you meet me"))

#26 Case Study : Reverse Engineer (Understand the code below) . This is the Code For AVL Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
    def __str__(self):
         return "<Node Properties = " + str(self.key) + "; left = " + str(self.left) + "; right = " + str(self.right) + ">"

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):

        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def pre_order(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def print_tree_visual(self, node, level=0, prefix="Root: "):
        """
        Recursively prints the AVL tree in a visual format with indentation.
        """
        if node is not None:
            print("    " * level + prefix + str(node.key) + f" (H: {node.height})")
            if node.left:
                self.print_tree_visual(node.left, level + 1, "L-- ")
            if node.right:
                self.print_tree_visual(node.right, level + 1, "R-- ")

    def visualize(self):
        """
        Initiates the visual printing of the AVL tree.
        """
        #if self.root:
        self.print_tree_visual(root)
        #else:
            #print("Tree is empty.")

#26 Case Study .. Inserting data into above AVL Tree
# Example usage
tree = AVLTree()
root = None

#26 Case Study .. Inserting data into above AVL Tree
for key in [10,20,30,70,60]:
    root = tree.insert(root, key)
    print(root)

print("Preorder traversal of the constructed AVL tree:")
tree.pre_order(root)

#26 Case Study ..See the End Result
tree.visualize()

#26 Case Study ..Reverse Engineer
# 1. Find How many times insert method is called (insert function has calls to itself in two places). Where will you declare variable and increment it for
#doing this
#2 Node has dunder method __str ... This method prints the tree
#Tree also printed by calling tree.pre_order(root) . pre_order calls itself twice..
#compare __str implementation and pre_order method . discuss pros ,cons,flexibility etc.

#27 Pandas
import pandas as pd
pd.__version__

#28 Pandas Intro
import pandas as pd
#dictionary with column names and the correspoding values as list
data = {'Name': ['John', 'Alice', 'Bob','John','GenC'],
        'Age': [25, 30, 35,25,21],
        'City': ['New York', 'London', 'Paris','New York',None]}

df = pd.DataFrame(data)
print(df)

#29 Pandas Intro-Select Specific columns
selected_columns = df[['Age', 'City']]
selected_columns

#30 Pandas Intro -filter Rows -- refer the column name and specifiy the condition
filtered_df = df[df['Age'] > 30]
filtered_df

#31 Pandas Intro-Sort the data
sorted_df = df.sort_values(by='Age', ascending=False)
sorted_df

#30 Pandas Intro-Sort the data
df.drop_duplicates(inplace=True)
df

#32 Pandas Intro-aggregate
grouped_df = df.groupby('City')['Age'].mean()
grouped_df

#33 Pandas Intro-Apply a Function to Each Element in a Column
df['AgeSquare'] = df['Age'].apply(lambda x: x**2)
df

#34 Pandas Intro-Merge
Country = {'City': ['New York', 'London', 'Paris'],
             'Country': ['USA', 'UK', 'France']}

dfCountry = pd.DataFrame(Country)
df=pd.merge(df,dfCountry,on='City')
df

#35 Pandas Intro-Pivot
pivot_df = df.pivot(index='Country', columns='City', values='Age')
pivot_df

#35 Pandas Intro-Fix Null ... Remove?
df.dropna(inplace=True)
df

#36 Pandas Intro-Fix Null ... replace?
#run 28 Pandas Intro code again and run this
#df['City'].fillna('Unknown City', inplace=True)
df.fillna({'City':'Unknown City'})
df

#37 Pandas Intro -- Create new columns
df['narrative'] = df['Name'] + ' From ' +df['City']
df

#37 Pandas Intro -- Create new columns
df['narrative'] = df['narrative'].str.upper()
df

#38 Pandas Intro -- Create new columns
df.rename(columns={'narrative': 'Narrative'}, inplace=True)
df

#37 Pandas Intro -- using Custom Function
def custom_function(row):
    return row['Age'] * 2

df['Age'] = df.apply(custom_function, axis=1)
df

#38 Pandas Intro -- What about the info()?.
# Count the number of rows and columns
num_rows = df.shape[0]
num_columns = df.shape[1]

# Print the results
print("Number of rows:", num_rows)
print("Number of columns:", num_columns)

!pip install d3blocks

#39 Pandas Intro -retrieve via indices
indices = [0, 2, 1]  # List of indices to extract.. The Row Identifier

# Extract rows based on the list of indices
extracted_rows = df.iloc[indices]

# Print the extracted rows
print(extracted_rows)

#40 Python Visualization
!pip install d3blocks

#40  Python Visualization
# Load library
from d3blocks import D3Blocks

# Initialize
d3 = D3Blocks()
# Import example
df = d3.import_example('energy')
# Create network using default
d3.d3graph(df, filepath='/content/d3graph.html', color='cluster', showfig=True)

#41 Python Visualization
# Initialize
d3 = D3Blocks()
# Import example
df = d3.import_example('energy')
# Create Chart
d3.elasticgraph(df, filepath='/content/elastic.html')



