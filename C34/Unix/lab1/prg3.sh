#!/bin/bash
echo "Enter the basic salary"
read basic
dp=$(echo "scale=3; 0.50 * $basic"|bc)
val=$(echo "scale=3; $basic + $dp"|bc)
da=$(echo "scale=3; 0.35 * $val"|bc)
hra=$(echo "scale=3; 0.08 * $val"|bc)
ma=$(echo "scale=3; 0.03 * $val"|bc)
pf=$(echo "scale=3; 0.10 * $val"|bc)
salary=$(echo "scale=3; $basic + $dp + $da + $hra + $ma - $pf"|bc)
echo "Total salary = $salary"

