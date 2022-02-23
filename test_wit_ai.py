import requests
import json
import sounddevice as sd
import recorder
from recorder import Recorder
import pyaudio
fs = 44100  # Sample rate
seconds = 3  # Duration of recording
while(True):
    #audio = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    #sd.wait()  # Wait until recording is finished
    #r=Recorder()

    RECORD_SECONDS=5
    #--------- SETTING PARAMS FOR OUR AUDIO FILE ------------#
    FORMAT = pyaudio.paInt16    # format of wave
    CHANNELS = 1                # no. of audio channels
    RATE = 44100                # frame rate
    CHUNK = 1024                # frames per audio sample
    #--------------------------------------------------------#

    # creating PyAudio object
    audio = pyaudio.PyAudio()

    # open a new stream for microphone
    # It creates a PortAudio Stream Wrapper class object
    stream = audio.open(format=FORMAT,channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)


    #----------------- start of recording -------------------#
    print("Listening...")

    # list to save all audio frames
    frames = []

    for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
        # read audio stream from microphone
        data = stream.read(CHUNK)
        # append audio data to frames list
        frames.append(data)

    print(frames)

    '''import speech_recognition as sr
    r = sr.Recognizer()
    speach=""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)'''
    #audio=''
    #print(stream)

    #print(str(audio.all()))

    API_ENDPOINT = 'https://api.wit.ai/speech'
    ACCESS_TOKEN = 'UNYDMIHRNPDM53AKFKF4G3NSZNQIWXFZ'

    headers = {'authorization': 'Bearer ' + ACCESS_TOKEN, 'Content-Type': 'audio/raw'}

    # Send the text
    text = "Hi Mira"
    resp1 = requests.get('https://api.wit.ai/message?&q=(%s)' % text, headers = headers)

    resp = requests.post(API_ENDPOINT, headers = headers, data = frames)#).get_raw_data())

    #Get the text
    data = json.loads(resp.content)
    print(data)