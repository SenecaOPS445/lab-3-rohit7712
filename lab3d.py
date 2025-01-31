#!/usr/bin/env python3

#Author ID: 145339222

import subprocess

def free_space():
     p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
     output, result = p.communicate()
     return output.decode('utf-8').strip()

if __name__ == "__main__":
     print(free_space())















