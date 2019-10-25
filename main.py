#!/usr/bin/env python3
import iNR
from datasave import filecreations
import gui.sh
from threading import Thread,Lock



def main():
  ptt1=iNR.pttAndNormReader(24, 18)
  ptt2=iNR.ptt_and_norm_reader(25,16)

  print(ptt1.ptt_and_norm())

main()
