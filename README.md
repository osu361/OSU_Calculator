# OSU_Calculator

## **To run Tkinter GUI on the engineering servers need to be able to open X11 terminal remotely** 


### To Open X11 Terminal Remotely From Windows Using Cygwin 

*(reference: https://x.cygwin.com/docs/ug/using-remote-apps.html)*

Make sure you have an X-client installed eg via Cygwin for example

1. modify cygwin/etc/sshd_config file so the following variables are:
* X11Forwarding yes
* X11DisplayOffset 10
* X11UseLocalhost yes
2. launch an Xterm in windows
3. Enter: export DISPLAY=:0.0
4. Enter: ssh -Y username@remote host

*To test if successful Enter:*  python3 -m tkinter

This should launch a tkinter test window

*To Launch multiple Xterms on the engineering server Enter:* xterm &
