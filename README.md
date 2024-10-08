[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SkD24yV8)
# 1.1.4Spirographs

*Complete the following.*

1. Compare and contrast zero-iteration conditions and infinite loops.
2. A link to your code where you solve the following problem. Take the screen size of 800px. Create code or algorithm that always places the object(s), up to 5, in the center an equal distance from one another and from the edges of the screen.
3. Concentric Squares -- Add a screenshot of your result and the code to create it on your repo.
Objective: Write a Python program using the turtle module to draw a pattern of concentric squares. The pattern should be created using nested loops.

Instructions:

Setup the Turtle Environment:
Import the turtle module.
Create a turtle object.
Set the turtle speed to the fastest setting.
Draw Concentric Squares:
Use a nested loop to draw multiple squares.
The outer loop should control the number of squares.
The inner loop should draw each square.
Each square should be slightly larger than the previous one.
Customize the Pattern:
Use different colors for each square.
Ensure the squares are centered on the screen.
Example Output:

The turtle should draw a series of squares, each one larger than the last, creating a pattern of concentric squares.

Hints:

Use the penup() and pendown() methods to move the turtle without drawing.
Use the color() method to change the turtle’s color.
Use the forward() and right() methods to draw the sides of the squares.


4. Complete the steps 17, 18 and 19 from [mypltw use clever to sign on](https://pltw.read.inkling.com/a/b/5310c007377c46e28d745961310f0c2e/p/728c751a6c4145bea0ea83c5058fb9f9#44b0003a2ee14fcc9865e7bb5faec747)
5. Answer to step 21
6. Insert a screenshot or picture of the algorith you used for your tokenizer on the previous activity.
7. Give an example of an undecidable problem, attach code.
   
1 A zero iteration condition is a condition where the code will run zero times while an infinite loop will continuously run forever. In a zero iteration condition, a certain condition is not met which causes the program not to run. However, an infinite loop, the condition is met which causes the program to run continuously. Similarly, both zero iteration conditions and infinite loops use loops and is based on a condition.

2 Link to code: [Link](https://replit.com/@yip0376/step2?v=1)

3 

<img width="467" alt="Screen Shot 2024-09-13 at 8 42 40 PM" src="https://github.com/user-attachments/assets/050d5fa7-6c5d-41e5-af40-f8d3db486b79">

4 Pltw Work:

Step 17:

![image](https://github.com/user-attachments/assets/7b1bd5a8-75d2-4389-b8fa-e8d20b9f28f7)

Step 18 & 19:

<img width="476" alt="Screen Shot 2024-09-13 at 7 11 05 PM" src="https://github.com/user-attachments/assets/c29532f2-d5fd-4d6d-8465-be9035e682d7">

5 Step 21: This flowchart represents a zero iteration, where sometimes the loop doesn't start, and other times it will be an infinite loop and continue.

6 Tokenization code from last activity:

<img width="235" alt="Screen Shot 2024-09-13 at 7 31 29 PM" src="https://github.com/user-attachments/assets/0ca3f0fa-0795-49e1-9f17-7495dc34733c">
<img width="276" alt="Screen Shot 2024-09-13 at 7 31 37 PM" src="https://github.com/user-attachments/assets/53e909a0-effe-4c52-a4fa-f377611b8fe9">

In this image, the tokenizer will check if any other flower words are typed into the users response. If the tokenizer detects a word, it will draw that flower. However, if the user does not input a word that the tokenizer picks up on, then it will tell the user that we are out of those specific flowers, and they will have to select a different kind.

7 Example of undecidable problem: One example of an undecidable problem is a problem where it asks for the user input and uses the input through a function. This function will determine what happens depending on the user input. If the user input is 0, then the function will end or halt. If the user input is any other number, the function will run infinitely.
