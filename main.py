#!/usr/bin/env python3
import iNR
from datasave import filecreations
import gui.sh



def main():
  ptt1=iNR.ptt_and_norm_reader(24,18)
  print(ptt1.ptt_and_norm())

main()
