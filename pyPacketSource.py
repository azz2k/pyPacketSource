import socket
import argparse
import time
from contextlib import closing

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="generate UDP packets")
  parser.add_argument("-s", help="source address", metavar="IP", type=str, required=True)
  parser.add_argument("-t", help="target address", metavar="IP", type=str, required=True)
  parser.add_argument("-p", help="port", metavar="PORT", type=int, required=True)
  parser.add_argument("-r", "--rate", help="packet rate", type=float, default=30.0)
  
  args = parser.parse_args()

  with closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as sock:
    sock.bind((args.s, args.p))
    try:
      while True:
        startTime = time.time()
        sock.sendto("", (args.t, args.p))
        endTime = time.time()
        if endTime - startTime < 1.0/args.rate:
          time.sleep(1.0/args.rate - (endTime - startTime))
    except KeyboardInterrupt:
      print "exiting.."
