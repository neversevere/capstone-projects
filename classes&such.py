# -*- coding: utf-8 -*-
"""classes&such.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11IMJDjRUZaZ3ONtuUFgPZ-0otSAMRLsj

## Analyses of project with multiple file comparison
"""

import os
import re
import sys
import time

"""
Utilize decorator for try-except for all methods"""

def catch_exception(func):
  def errorCatcher(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except Exception as e:
      print(f'Caught an exception in {func._name_}{e}')
  return errorCatcher

"""Utilize decorator to add time-out function"""

def timeit(func):
  def timed(*args, **kwargs):
    ts = time.time()
    result = func(*args, **kwargs)
    te = time.time()
    print('Function', func._name_, 'time:', round((te- ts)*1000,1), 'ms')
    print()
    return result
  return timed

"""Define class with init and main()"""

class Subject_A:
  def __init__(self, question, files, dir_path, abc_path):
    self.question = question
    self.files = files
    self.dir_path = dir_path
    self.abc_path = abc_path

@timeit

def main(self):
  self.checkItem()
  self.comparefiles()

"""Define first function"""

@catch_exception
def checkItem(self):
  re_name = r'ItemName\d{2}'
  question = self.question
  if re.match(re_name, question):
      x = input('You have entered ' + question + '. Is this correct?\n')
      if x.lower() == ('yes'):
        print('Continue.\n')
      elif x.lower() == ('no'):
        print('Stop!Please enter correct value.\n')
        sys.exit()
      else:
        sys.exit()
  elif question != re.match(re_name, question):
    print('This the incorrect format.')
    sys.exit()

"""Define second function"""

@catch_exception
def comparefiles(self):

  pattern = re.compile('^\S{1,}ABCD\d.*.')
  list1 = os.listdir(self.dir_path)

  newlist = []
  for file in list1:
    if re.match(pattern, file):
      clean_file = file.strip('.txt').removeprefix('ABC_')
      newlist1.append(clean_file)

  list2 = os.listdir(self.abc_path)
  newlist2 = []
  for file in list2:
    if re.match(pattern, file):
      newlist2.append(file)

  list2files = ''.join(newlist2)
  other_list = [file for file in newlist1 if file not in list2files]
  if other_list:
    print('Abort!Abort!')
    sys.exit()
  else:
    print('Ready for lift off!')

"""Call and Define main() function"""

if __name__ == "__main__":
  dir_path = input('Please load first file.\n').strip().strip("'")
  abc_path = input('Please load second file.\n').strip().strip("'")
  question = input('Which project are you analyzing?\n')

  abc = Subject_A(question, dir_path, abc_path)

  abc.main()