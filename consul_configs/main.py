#!/usr/bin/env python3


import consul_kv


def main():
  TESTJSON = { 'TESTVALUE': 'blahblah', 'TESTVALUE2': 'blahblah2' }
  return TESTJSON

if __name__ == '__main__':
  TEST = main()
  print(TEST)
