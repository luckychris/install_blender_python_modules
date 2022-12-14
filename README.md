# Install any python module for Blender python


If you are a Blender user you might also wonder why the module you just installed for python didn't work in the Blender python console or in the python script you wrote in Blender.

The reason for this is that Blender has its own python version and python libraries "inside" which it is using. 

So to make it work in Blender too, you have to install the modules you are using for the python version in Blender as well.

This little script shall simplify this task for you.

Just copy and paste the code in your text editor in Blender, then just change this one line here:

    installModule("pandas")
    
and replace "pandas" with whatever module you want to install.

Then run the script.





Small remark:

I am working on MacOS. So i am pretty sure it works on MacOS. I tried to implement the functionality for Linux and Windows as well. Unfortunately i couldn't test that. If there are errors, please open an issue and i try to fix that. Thank you.





If you want to support my work or buy me a coffee:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/paypalme/christophduyster)

