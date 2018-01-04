from __future__ import print_function
from pref_timer.timer import timer


@timer
def main():
    for i in range(60000):
        print ("Execution:", i)

if __name__ == '__main__':
    main()