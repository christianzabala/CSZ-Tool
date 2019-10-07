# CSZ-Tool
**Overview**
- This is a simple python script that automatically generate a OAM command for a NOKIA BNG for the process of showing a LAG ID, IP addresses and clearing the MSAP of a user connected on the BNG during the events when a customer was moved to a different OLT.  
- This script also looks(by sraping a file)  for IP address(IPv4 only) that will auto ping those IPs(without duplicate IPs) then return the result of the ping test to know what are the devices that are still down or has no IP address yet. 
- This script also has a duplicate network element(Customer port on the OLT) remover, script will only show unique network elements on a file.

**Note:**  The Script still requires some manual work since it doesn't not contain any Package or module to allow the script to ssh on a device since currently there are restrictions on my job role.

Possible Future revisions:
 1. Include a module to ssh on a network device then send specific commands needed. Perhaps make it multithreaded 
 2. Concert the codes to a class that can be reuse on future projects
 3. Add more Exception and Error Handling
 4. Detect what Address ID that has no IP address
 5. Option to show what are the duplicate network elements and network elements that don't have any duplicates.
 6. Option to remove specific network elements if the line card or PON is already included. ex. removed olt 1/1/2/3/2 if olt 1/1/2 or 1/1/2/3 is already on the file.
 
 **How to use:**
 Download the python script(CSZtool.py), Open it on a terminal by typing "python3 CSZtool.py"or change the file to an excutable file to just input the ./CSZtool.py
 ![Menu](https://github.com/christianzabala/CSZ-Tool/blob/master/Sample-Pics/p1.jpg)
 
 **Option #1:**
 - Paste the Customers Address IDs on the terminal(Ctrl+Shift+V) , then press ENTER(For the script to be able to read the last line or the last input address id) and hit Ctrl+C
  ![Option1a](https://github.com/christianzabala/CSZ-Tool/blob/master/Sample-Pics/p3.jpg)
  Copy all the result and paste it on the BNG where the customer is connected.
  ![Option1b](https://github.com/christianzabala/CSZ-Tool/blob/master/Sample-Pics/p4.jpg)  
 **Option #2:**
 -  Input or paste a list of IP addresses to auto-ping it
  ![Option2](https://github.com/christianzabala/CSZ-Tool/blob/master/Sample-Pics/p5.jpg)  
 **Option #3:**
 -  Open a file that has IP addresses for the script to gather the total IP address and auto-ping it
  ![Option3a](https://github.com/christianzabala/CSZ-Tool/blob/master/Sample-Pics/p6.jpg)
  ![Option3b](https://github.com/christianzabala/CSZ-Tool/blob/master/Sample-Pics/p7.jpg) 
 **Option #4:**
 -  Open a file that has LAG-IDs on it then generate a clear service command
  ![Option4](https://github.com/christianzabala/CSZ-Tool/blob/master/Sample-Pics/p8.jpg)
 **Option #5:**
 -  Open a file that has consolidated network elements from outage tickets then return a result without a duplicate network element
  ![Option5](https://github.com/christianzabala/CSZ-Tool/blob/master/Sample-Pics/p9.jpg)
