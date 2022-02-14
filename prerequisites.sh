#!/bin/bash

#disable screen going to sleep

xset s 0
xset -dpms
xset q




#Install linux packages

sudo apt-get install libatlas-base-dev -y
sudo apt-get install libjasper-dev -y
sudo apt-get install libqtgui4 -y
sudo apt-get install python3-pyqt5 -y
sudo apt-get install python3-tk -y
sudo apt-get install portaudio19-dev python-pyaudio -y
sudo apt-get install espeak -y
sudo apt-get install flac -y # import form speech_recognition
sudo apt-get install libgtk2.0-dev -y

#Install python packages
pip3 install setuptools

pip3 install sys
pip3 install os

pip3 install requests

pip3 install signal


pip3 install matplotlib
pip3 install youtube_dl
pip3 install numpy
pip3 install Pillow
pip3 install face-recognition
pip3 install SpeechRecognition


pip3 install urllib3



pip3 install DateTime
pip3 install youtube-search
pip3 install pyttsx3
pip3 install python-vlc
pip3 install pafy

pip3 install goose3

pip3 install svglib

pip3 install PyAudio

pip3 install putils
pip3 install opencv-contrib-python

#create folder for user pictures
cd ..
mkdir Users
sudo chmod -R 777 smart-mirror # if we would do 766 then we could only access directory with sudo




