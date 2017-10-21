#!/bin/bash
echo "Enter p, r and t"
read p
read r
read t
Si=$(echo "scale=3; 0.01 * $p * $r * $t"|bc)
echo "Simple Interest : $Si"
