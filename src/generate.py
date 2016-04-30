#!/usr/bin/env python

from subprocess import call



def main():
    call(["make"])
    call(["make", "clean"])

if __name__ == '__main__':
    main()
