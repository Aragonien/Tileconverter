# Tileconverter

## What does this program do?
This program converts 24x24pixel frames into 8x8pixel frame rows, that can be imported as animated tiles on the BPA layer in the Skytemple Rom Editor. Also it's recommended to use an empty folder as the output destination

## How do I have to format my frames?
The individual frames should all be line up from first to last, from left to right, without any pixels in between the frames or around the frames.
Keep in mind that this program only converts one 24x24 tile and its animation frames.
If this it's still unclear how exactly the formated file should look, please take a look at the "example.png", which contains 8 frames of a rising white object.

## What does this program not do?
The resulting image is not getting indexed.

## Required Libraries
Pillow
