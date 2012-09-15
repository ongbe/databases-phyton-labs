import sys, os;
from dataset.AutoResizedMappedFile import AutoResizedMappedFile as MF;
import mmap;

f = os.open('d:\\1.txt', os.O_RDWR)
m = MF(f, 1)
m.write("hi")

