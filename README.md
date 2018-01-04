# pyPerformanceTimer
Functionality Performance Timer

# Introduction
The `pyPerformanceTimer` is used to find the function execution time. So it will use which function takes more time when execute and helps to find out the performance issue. So this is beginning and the more updated coming soon.

# Installation
It's very simple install and use, I will show two types of installation manual and PIP installation.

__Manual Installation__

First you need to clone the package or download the latest release.

``` bash
https://github.com/PraveenJP/pyPerformanceTimer.git
cd 'path to the package'
python setup.py sdist
python setup.py install
```
__PIP Installation__

``` bash
pip install pref_timer
```

# Usage

It's very easy to use, Please follow the setps.

```bash
  from pref_timer.timer import timer
  
  @timer
  def main():
      for i in range(50000):
          print ("Execution:", i)

  if __name__ == '__main__':
      main()
```

Finally run the python file.

# Result

The Result of the above simple loop method
``` bash
Execution: 19998
Execution: 19999
main Taken: 0.3 Seconds
```
It shows the functionality name and time which is taken.

_If any suggestion or doubts please let me know via below email._

__Email:__ _praveen.josephmasilamani@outlook.com_

- - - -

### Happy Coding. :)
