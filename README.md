# Tileconverter

##What does this programm do?
This programm converts 24x24 frames into 8x8 frame rows, that can be imported as animated tiles on the BPA layer in the Skytemple Rom Editor.

##How do I have to fromat my frames?
The individual frames should all be line up from first to last, from left to right, without any pixels inbetween the frames or around the frames.
Keep in mind that this programm only converts one 24x24 tile and its animation frames.
If this it's still unclear how exactly the fromated file should look, please take a look at the "example.png", which contains 8 frames of a rising white object.

##What does this programm not do?
The resulting image is not getting indexed.

##Requiered Libraries
Pillow
