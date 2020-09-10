#!/bin/bash
T="$(date +%s%N)"
echo $1 | nc 143.0.100.198 60123 >> output.txt 2>&1 ;
T="$(($(date +%s%N)-T))"
echo $T