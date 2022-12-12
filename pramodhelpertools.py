import librosa
import numpy
import os

x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\440a.wav", sr = 44100)
with open("440a.hex", "w") as f:
    sine_int = numpy.zeros(101).astype(int)
    for i in range(101):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\394b.wav", sr = 44100)
with open("394b.hex", "w") as f:
    sine_int = numpy.zeros(90).astype(int)
    for i in range(90):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\525c.wav", sr = 44100)
with open("525c.hex", "w") as f:
    sine_int = numpy.zeros(85).astype(int)
    for i in range(85):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\588d.wav", sr = 44100)
with open("d88d.hex", "w") as f:
    sine_int = numpy.zeros(75).astype(int)
    for i in range(75):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\660e.wav", sr = 44100)
with open("660e.hex", "w") as f:
    sine_int = numpy.zeros(67).astype(int)
    for i in range(67):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\440a.wav", sr = 44100)
i=0
with open("699f.hex", "w") as f:
    sine_int = numpy.zeros(63).astype(int)
    for i in range(62):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\440a.wav", sr = 44100)
with open("784g.hex", "w") as f:
    sine_int = numpy.zeros(56).astype(int)
    for i in range(56):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
x, Fs = librosa.load(r"C:\Users\matte\Documents\Audacity\880a.wav", sr = 44100)
with open("880a.hex", "w") as f:
    sine_int = numpy.zeros(50).astype(int)
    for i in range(50):
        sine_int[i] += int(x[i] * 128)
        if sine_int[i] < 0:
            sine_int[i] = ~sine_int[i] + 1
        f.write("{:02x}\n".format(sine_int[i]))
