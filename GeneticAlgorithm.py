'''
Input a target number, the algorithm gives a 'fitness level' to solutions,
which are higher the closer it is to the target value. 
Digits and +, -, * and / are all represented by 4 digit binaries.
These are strung together to form a 'chromosome'
Follows the system (number -> operator -> number ->operator ->number)

Algorithm should find a way to represent the target number
'''
from __future__ import division
from decimal import Decimal
from matplotlib import pyplot as plt
import random
import numpy as np
import sys


# Function to merge lists
def merge(*things):
	newlist = []
	for elem in things:
		newlist += elem
	return newlist
	
# Checks if two lists are equal	
def checkEqual(lst):
   return lst[1:] == lst[:-1]

# Create a list of random chromosomes with length 28
def RandomChromosomeGen(binary_list):
	
	x = ''
	# Create 1000 random chromosomes of length 28
	N = 100
	while len(binary_list) < N:

		x = (random.choice(digits.values()) + random.choice(operators.values()) + random.choice(digits.values()) 
			+ random.choice(operators.values()) + random.choice(digits.values())+ random.choice(operators.values()) + random.choice(digits.values()))
		binary_list.append(x)
		x = ''
	
	
	return binary_list

# Split chromosomes into groups of 4 so we can compare them to our dictionaries
def ManipulateGene(gene, binary_gene_list):
	
	gene = list(gene) # Convert to list
	
	# Merge every 4 digits to get dictionary items into new list
	for i in range(0, len(gene), 4):
		binary_gene_list.append(gene[i] + gene[i + 1]+ gene[i + 2]+ gene[i + 3])
		
	return binary_gene_list
	
# Main algorithm to take in binary strings, calculate fitness values, and then select 2 members of the group giving members with a higher fitness a higher
# chance of getting picked, and give them a 70% chance of swapping a random number of digits. Keep picking and swapping until 1000 chromosomes are created 
def CalculateFitness(gene, target_value, binary_gene, TargetSolution, max_list):
	
	equation = []
	
	# Convert each binary block to actual values and save to list
	for i in binary_gene:
		for j in digits2.keys():
			if i == j: 
				equation.append(digits2[j])
		for k in operators2.keys():
			if i == k:
				equation.append(operators2[i])
				
	if i != j and i != k:
		equation.append(' ')
	
	# Merge equation list then strip value to leave digits and operators
	equation = [str(x) for x in equation]
	eqn = (''.join(equation))
	# print eqn
	
	# Logic that dictates what to do if the entire chromosome series doesn't make sense
	try:
		eqn_solution =  eval(eqn)
		
	
	except:
		eqn_solution = 0
		# fitness_score = abs(1/(target_value - eqn_solution))
		fitness_score = 0
		
		
	else:
		# Create fitness value for gene (Higher the better)
		if eqn_solution == target_value:
			TargetSolution = True
			print "A Solution was found after: ", Num_of_generations,' Generations'
			print eqn , '=', eqn_solution
			
			# print 'Maximum of each generation: 'max_list

			sys.exit()
		
			#print 'A solution is: ', eqn
		else:
			try:
				fitness_score = abs(1/(target_value - eqn_solution))
			
			except:
				Decimal(fitness_score = abs(1/(target_value - eqn_solution)))
	
	return fitness_score

	

''' RUN ALGORITHM '''
'''
Put everything into a function and run function in a loop until target is found'''


digits = {0 : '0000', 1 : '0001', 2 : '0010', 3 : '0011', 4 : '0100', 5 : '0101', 6 : '0110', 7 : '0111', 8 : '1000', 9 : '1001'}
digits2 = {'0000': 0, '0001': 1, '0010': 2, '0011': 3,'0100': 4,  '0101': 5, '0110': 6, '0111': 7, '1000': 8, '1001': 9}
operators = {'+' : '1010', '-' : '1011', '*' : '1100', '/' : '1101'} # The binary digits 1110 and 1111 are unused
operators2 = {'1010' : '+',  '1011' : '-',  '1100' : '*',  '1101' : '/'}

# Create random initial 'chromosome'
initial_gene = (random.choice(digits.values()) + random.choice(operators.values()) + random.choice(digits.values()) 
	+ random.choice(operators.values()) + random.choice(digits.values())+ random.choice(operators.values()) + random.choice(digits.values()))

# Create list of chromosomes
chromosomes = []
RandomChromosomeGen(chromosomes)


# Use randomised chromosomes to find fitness values by manipulating the binaries then passing it through the Algorithm function
TargetSolution = False
max_list = []
Num_of_generations = 1
while TargetSolution == False:
	
	fitness = []
	target_val = 300.0
	for eachThing in chromosomes:

		binary_gene = []
		ManipulateGene(eachThing, binary_gene) # Convert each chromosome into 4 digit binary blocks
		
		# Save output of CalculateFitness to list 'fitness'
		fitness.append(CalculateFitness(eachThing, target_val, binary_gene, TargetSolution, max_list))
	percentage = []	
	eqn_solution_list = []
	total_fitness = np.sum(fitness) # sum all fitness values	
	for val in fitness:
		percentage.append(val/total_fitness)
		if val != 0:
			eqn_solution_list.append(target_val - (1/val))
	
	max_list.append(np.max(eqn_solution_list))
	# Create new set of chromosomes by weigted random selection of chromosomes and swapping genes
	list_of_new_binaries = []
	# N = 100
	while len(list_of_new_binaries) < len(fitness):
		# Random weighted choices of chromosomes
		choice_1 = list(np.random.choice(chromosomes, p = percentage)) 
		choice_2 = list(np.random.choice(chromosomes, p = percentage))
		
		choice_1 = [str(x) for x in choice_1]
		choice_2 = [str(x) for x in choice_2]
				
		numSwap = random.randint(1,28)
		
		Random_Swapping = random.randint(1,1000)
		
		# Possibility of mutation, i.e. a bit randomly swapping from a 1 to a 0, and vice-versa
		if Random_Swapping == 1:
			mutation = choice_2[numSwap-1] 
			print 'MUTATION!'
			
			if mutation == '1':
				choice_2[numSwap-1] = '0'
			else:
				choice_2[numSwap-1] = '1'
				
		elif Random_Swapping < 700:
			# 70% chance of swapping genes between two weigthed choices of chromosomes
			choice_1_x = []
			choice_2_x = []
			
			choice_1_x = choice_1[numSwap:]
			choice_2_x = choice_2[numSwap:]
			del choice_1[numSwap:]
			del choice_2[numSwap:]
			
			choice_1 = merge(choice_1, choice_2_x)
			choice_2 = merge(choice_2, choice_1_x)
			
			choice_1 = (''.join(choice_1))
			choice_2 = (''.join(choice_2))
			list_of_new_binaries.append(choice_1)
			list_of_new_binaries.append(choice_2)
			
		else:
			# If genes don't get swapped
			choice_1 = (''.join(choice_1))
			choice_2 = (''.join(choice_2))
			list_of_new_binaries.append(choice_1)
			list_of_new_binaries.append(choice_2)
	
	if checkEqual(fitness) == True:
		# TargetSolution = True
		print " ENDED WITH ALL SIMILAR VALUES, WAIT FOR MUTATION"
		
		list_of_new_binaries = []
		RandomChromosomeGen(list_of_new_binaries)
		
	#print chromosomes
	
	Num_of_generations += 1
	chromosomes = list_of_new_binaries

