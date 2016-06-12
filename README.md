
#Robots Communication Simulation

We design simulation that represents an arena of robots in Python language.  
Our arena size is 1000 X 1000.  
The color of all the arena is white and there is areas that are gray or black.  
On the arena we are creating robots, each robot has a number ID and a color.  

###Arena Details:
**Colors:**
* **White (light) area:** robot can move freely and his battery cherging.  
* **Gray (dark) area:** robot can move on this area but his battery running low.  
* **Black area:** robot can not move on this area.  

**Robots:**  
**1. Static Robots - red:** robots that know their location in the arena and can send and receive messages.  
**2. Moving Robots - green:** 
* Do not know their location in the arena.
* Battery running low as moving - whan the battery low the robot becomes to yellow color.
* Battery cherging only in white area.
* Once the battery is over the robot stops moving and becomes to black color.
* In gray area:   
1.Checking his last step - if was in white area he going step back.  
2.Checking his Neighbours - if one of his neighbors were in white area he going to there.
* Can send and receive messages only if knows more than 3 of his neighbors.
* knows his neighbors with the help of sending and receiving messages.

####The purpose of the project is: 
Moving Robots will discover their location using the Static Robots.  
As time goes by more messages will be sent and the Moving Robots will succeed to guess correctly their location.  
![Link to our Diagram](https://github.com/Most601/ThirdExercise/blob/master/newdiagram.JPG)


###Arena GUI:
![Link to our GUI](https://github.com/Most601/ThirdExercise/blob/master/Arena%20-%20GUI.jpg)
