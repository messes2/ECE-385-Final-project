import librosa
import numpy
import os

x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\394g.wav", sr = 44100)
with open("394g.hex", "w") as f:
    sine_int = numpy.zeros(112).astype(int)
    for i in range(112):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\350f.wav", sr = 44100)
with open("350f.hex", "w") as f:
    sine_int = numpy.zeros(126).astype(int)
    for i in range(126):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\329e.wav", sr = 44100)
with open("329e.hex", "w") as f:
    sine_int = numpy.zeros(134).astype(int)
    for i in range(134):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\293d.wav", sr = 44100)
with open("293d.hex", "w") as f:
    sine_int = numpy.zeros(150).astype(int)
    for i in range(150):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\261c.wav", sr = 44100)
with open("261c.hex", "w") as f:
    sine_int = numpy.zeros(168).astype(int)
    for i in range(168):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\247b.wav", sr = 44100)
with open("247b.hex", "w") as f:
    sine_int = numpy.zeros(178).astype(int)
    for i in range(178):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\220a.wav", sr = 44100)
with open("220a.hex", "w") as f:
    sine_int = numpy.zeros(200).astype(int)
    for i in range(200):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\196g.wav", sr = 44100)
with open("196g.hex", "w") as f:
    sine_int = numpy.zeros(224).astype(int)
    for i in range(224):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))    
