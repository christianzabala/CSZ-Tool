# CSZ-Tool
**Overview**
- This is a simple python script that automatically generate a OAM command for a NOKIA BNG for the process of showing a LAG ID, IP addresses and clearing the MSAP of a user connected on the BNG during the events when a customer was moved to a different OLT.  
- This script also looks(by sraping a file)  for IP address(IPv4 only) that will auto ping those IPs(without duplicate IPs) then return the result of the ping test to know what are the devices that are still down or has no IP address yet. 
- This script also has a duplicate network element(Customer port on the OLT) remover, script will only show unique network elements on a file.

**Note:** - The Script still requires some manual work since it doesn't not contain any Package or module to allow the script to ssh on a device since currently there are restrictions on my job role.

Possible Future revisions:
 1. Include a module to ssh on a network device then send specific commands needed. Perhaps make it multithreaded 
 2. Concert the codes to a class that can be reuse on future projects
 3. Add more Exception and Error Handling
 4. Detect what Address ID that has no IP address
 5. Option to show what are the duplicate network elements and network elements that don't have any duplicates.
 6. Option to remove specific network elements if the line card or PON is already included. ex. removed olt 1/1/2/3/2 if olt 1/1/2 or 1/1/2/3 is already on the file.
 
 **How to use:**
 1. Download the python script(CSZtool.py)
 2. Open it on a terminal by typing "python3 CSZtool.py"or change the file to an excutable file to just input the ./CSZtool.py
 ![Menu](https://github.com/christianzabala/CSZ-Tool/blob/master/sample-pics/p1.jpg)
 
