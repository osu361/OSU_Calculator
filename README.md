# OSU_Calculator

## **To run Tkinter GUI on the engineering servers** 


### For Windows 

*(reference: https://x.cygwin.com/docs/ug/using-remote-apps.html)*

Make sure you have an X-client installed eg via Cygwin for example

1. launch an Xterm in windows
2. Enter: export DISPLAY=:0.0
3. Enter: ssh -Y username@remote host

*To test if successful Enter:*  python3 -m tkinter

This should launch a tkinter test window

*To Launch multiple Xterms on the engineering server Enter:* xterm &
