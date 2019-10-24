#!/usr/bin/env python3
import iNR
from datasave import filecreations
import gui.sh
from threading import Thread,Lock



def main():
  ptt1=iNR.ptt_and_norm_reader(24,18)
  ptt2=iNr.ptt_and_norm_reader(25,16)

  print(ptt1.ptt_and_norm())

main()
