# Mehendi Bot
#### Authors: Emma Mascillaro, Rucha Dave, Cherry Pahm, Vanni Bhatnagar, Phillip Post

## **Project Summary**:
This repository contains our Fall 2022 Principles of Integrated Engineering Final project.

This interactive application uses Speech Recognition to play sound effects as a user reads a story out loud.  Audio data is collected as a user speaks and is transcribed to text using Google's Speech Recognition API.  When keywords are recognized in the user's speech, corresponding sound effects are played through Pygame in order to enhance the reader's reading experience.

Some challenges faced in this project included the timeout and delay involved when using SpeechRecognition.  In the future, we plan to switch to using LiveSpeech from pocketsphinx in order to reduce this time delay. 

This project is a robot that can apply Mehndi (henna) to a user’s hand.  As a final product, we hope to have a user be able to insert their hand into our mechanism and get mehndi applied based on the location, shape, and elevation of their hand.  First, we will take an image of the user’s hand to determine their unique hand’s location and shape.  Then, we will have the user choose a design and have the design automatically mapped to their hand. Our mechanical system will then move a syringe in the x-y plane which follows the vector path of our design.  The syringe will be squeezed in locations where the design should be placed, and an additional z-axis motor will be used to account for the slight elevation changes in the user’s hand.
