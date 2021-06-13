# File-Encrypter
![felogo](https://user-images.githubusercontent.com/33039708/121789540-847a5300-cbf4-11eb-83b8-adc0c5321c39.JPG)

A Small Program in Python used to Encrypt an Decrypt all files(* . *) Using AES256-CBC Algorithm.

Give a star if you liked it!!

# How To Use
1. Install pyAesCrypt using "pip install pyAesCrypt".
2. Browse for the File and then Encrypt or Decrypt it.

# Screenshot

![feoutput1](https://user-images.githubusercontent.com/33039708/121799625-c8984280-cc4a-11eb-9e72-fdc2dd8e6965.JPG)

# How it Works
1. First you Browse for a file (* . * ) and then you Enter the Buffer Size which has been set for 64Kb Default Value. Buffer size is used for Encrypting very big Files Wherein you specify the size and the Big File is Encrypted in Chunks of the Specified Size Otherwise whole Text/Binary Data will be Loaded in the Memory Overloading it and Eventually Crashing your PC. Now it doesnt bother you for Small Files but Lets Suppose you want to Encrypt a 4GB file and you Have 4GB RAM then whole Binary Data of the 4GB File will be Loaded into the Memory at Once Causing Problems.
2. Then You Specify a Password (12345  - Default) which will be needed to Decrypt the File. 
3. You can Check the CheckButton if you Want the Original File to Be Deleted while Encrypting or if you want the Encrypted File To Be Deleted while Decrypting.

# Algorithm
1. The Algorithm used is AES256-CBC Algorithm
2. AES is a mathematical function called pseudo-random permutation. It works on a block of fixed size and produces another block of the same size that is computationally indistinguishable from random data.
3. AES in CBC mode splits the stream into 16-byte blocks. Each block is encrypted using AES and the result is sent to output and XORed with the following block before it gets encrypted.

# Request a Feature
If you want me to add a Particular Feature in the Source then

1. Goto Issues and Create a New Issue
2. There Select a Feature Request Template and Click Get Started
3. Write Accordingly
4. OR Contact me at hrithikraj137@gmail.com

# V2
1. To Add Functionality of Encrypting Folders.
2. To Add Functionality To Shred Data so that it Cannot be Recovered.
