#Project3.py
#Shamsadean Mirghani
#This program will compute the time it takes an object to fall to earth
#from a particular distance along with its final velocity

# Define constants
ACCELERATION= 32.174
# Import math for the square root
import math

#Function to compute the time when the s is set as the formal parameters
def time(s):
    t= math.sqrt ((2 * s)/ACCELERATION)
    return t

# Function to compute the Velocity when it accepts t into the fromal
# parameters
def velocity(t):
    v= ACCELERATION*t
    return v

def main():

    # Handshake
    print("This program will compute the time it takes an object to")
    print("fall to earth from a particular distance along with its")
    print("final velocity.")
    print("Please enter a ending value less than your starting value.")
    
    # Asks the user for the starting, ending, and delta values
    starting= eval(input("Please enter the starting distance:   "))
    ending= eval(input("Please enter the ending distance value:   "))
    delta= eval(input("Please enter the value of the delta:   "))
    
    # Asks the user for the name of the file that the output will be
    # stored in
    my_file= input("Please enter your file name for the output:   ")
    # Writes on a new file the 
    newfile= open(my_file, "w")

    # Table headings
    print("Distance{0:11}Time{0:6}Velocity(ft/sec){0:1}Velocity(mph)"
          .format(" "))
    print("Distance{0:9}Time{0:6}Velocity(ft/sec){0:1}Velocity(mph)"
          .format(" ")
          ,file=newfile)
    # For loop that calculates the velocity in ft/sec to mph and then
    # Displays them in a table
    for i in range (starting, ending, -delta):
        my_time= time(i)
        My_velocity= velocity(my_time)
        my_velocity2= 0.681818 * My_velocity
        # Sends the information to a file that is named by the user 
        print('{0:10.4f}     {1:8.4f}     {2:10.4f}     {3:10.4f}'
            .format(i, my_time, My_velocity, my_velocity2), file=newfile)
        print('{0:10.4f}     {1:10.4f}     {2:10.4f}    {3:10.4f}'
            .format(i, my_time, My_velocity, my_velocity2))
    newfile= open(my_file)
    # Closing the file
    newfile.close()
        
main()

    
                
