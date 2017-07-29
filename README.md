# Genetic_Algorithm_Binary
Program made to learn about genetic algorithm by solving the challege proposed in http://www.ai-junkie.com/ga/intro/gat3.html 

The program tries to find a possible method of calculating a target value, using just number and operators (+, -, * and /)
The program randomizes an a string of 7, 4 digit binaries(we'll refer to as genes), with their values representing those shown below. The string alternates between
numbers and operators giving us a "chromosome". It should be noted that 1111 and 1110 aren't represented so the code will ignore them should
they arise.

0:         0000
1:         0001
2:         0010
3:         0011
4:         0100
5:         0101
6:         0110
7:         0111
8:         1000
9:         1001
+:         1010
-:          1011
*:          1100
/:          1101

The program is set to create 100 chromosomes and each one is split into its genes, translated to either a number or an operator and solved
to output a value. Each chromosome is given a fitness score, where the closer the chromosomes output is to the target value, the higher its
fitness. 

2 chromosomes are picked from a weigted randomization, giving chromosomes with a higher fitness a higher chance of getting picked. There is 
then a chance that a random number of bits in the two chromosomes are swapped. This process is repeated until a new array of 100 chromosomes
are created. 

The chromosomes are also given a 0.001% chance that they will mutate. In this context, mutation means that a random 0 within the chromosome 
could spontaneously flip to be a 1 and vice-versa. 

This sequence of randomization and awarding a fitness score is looped until the program finds a chromosome that gives us the target value
that we want.
