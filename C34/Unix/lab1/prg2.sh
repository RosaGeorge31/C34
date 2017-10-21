#!/bin/bash
echo "Enter the radius"
read r
area=$(echo "scale=3; 22 / 7 * $r * $r"|bc)
echo "Area = $area"

