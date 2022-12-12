# ECE-385-Final-project
I made a motion controlled digital synthesizer known as a puppeteer theremin with full onboard audio processing that uses AI to get motion control data from two different lan network servers hosted on two different android phones onto an FPGA to which control the note and the pitch.

This project has a lot of moving parts (Motion source, PadTest, Tesseract, eclipse, Audacity, Visual studio code, window switching, Quartus), which can be very overwhelming to deal with. Because of this the readme is broken into parts, external software, custom software, hardware, then implementation. Please note the phone can only be Android OS and the computer being used must be Windows OS. Nothing else will work.

Partial credit for the code in this final project goes to ECE department for the lab 62 code, the anonymous creators of motion source and padtest, the entire team responsible for tesseract, and the python  libraries I used, and Pramod and Ian the CAs who created small helper tools for wave table synthesis,  and python JTAG connection respectively. Special thanks for help with debugging goes out to the TA’s Phil and Zayd, could not have done it without them. All the  love and emotional support goes out to Pramod though.

Read the pdf to figure out more of the stuff

Order to go in for implementation while running is

1. Complete partial program setup shown in readme.PDF

2. JTAG Programmer for Lab6b.sof

3. Nios ii Eclipse Flash programming

4. End the JTAG connection with Eclipse

5. Run windowactivation.py

6. Run ece385finaldemo.py

7. Move the phones as you wish to play notes.

