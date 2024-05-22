# Virtual-Paint
<h3>Introduction</h3>
Hi<br>
This project is made using OpenCV.<br>
The laptop camera records video and we can write and draw any thing on the screen by detecting contours. The project has features like eraser which clears the screen on pressing  '<b>e</b>' on keyboard. Also pressing '<b>q</b>' on keyboard stops the program execution and closes all the windows.
<br>
<h3>General Idea</h3>
First we choose a colour to write with. Using Stack Overflow, we can find the HSV min and max values to detect it.<br>
Then using <b>HSV_Chooser</b> we will set the trackbar to the values found on Stack Overflow and optimize it so it can cleary detect the particular shade. Then we will note down the values.<br>
Now coming to <b>virtual_paint</b> we will start the camera and then start taking images. The images are then converted to HSV and we will apply the previously noted values to get the mask.<br>
Then we will find the contours of the object we want to draw with. As there will be same background colour distrubing our mask, we will avoid it by considering only the objects which has more pixels. Then we will draw the rectangle around it and take the x,y,width,height of the object. Now using (x+w)//2 we will get the bisector of the object and using it will draw a circle on the tip of the object and return the co ordinates.<br>
The coordinates are stored in a list. The list is then printed at every execution of the video loop eventually forming a line. The final resulant image is flipped so that it can get easy to write. <br>
Inside the loop we give a condition that if letter 'e' is pressed, the list becomes empty giving us the effect of an eraser. If 'q' is pressed, the program execution is stoped and all windows are closed.
