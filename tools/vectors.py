from os import system

def clear():
	_ = system('cls')

vectors = []
vectors_name = []

clear()
print("This is a tool to create, add, subtract or multiply vectors. \n")

def add_vectors(a, b):
	result = []
	if (len(a) == len(b)):
		for i in range(len(a)):
			result.append(a[i] + b[i])
		return result
	else:
		ans = input("The two vectors are in different dimensions. Do you still want to add them? (Y/N)")
		if (ans == 'Y' or ans == 'y'):
			for i in range(len(a)):
				if(i >= len(b)): break
				result.append(a[i] + b[i])
			return result

def create_vector():
	result = []
	name = input("What is the vector called?  ")
	dim = input("How many dimensions?  ")
	for i in range(int(dim)):
		result.append(int(input("Dimension "+str(i+1)+": ")))
	vectors.append(result)
	vectors_name.append(name)

def show_all():
	print("\n")
	for x in range(len(vectors)):
		print("    " + vectors_name[x] + ": " + str(vectors[x]))
	print("\n")

while True:
	print("Controls: \n")
	print("Create vector ---- Press c")
	print("Show all vectors - Press s")
	print("Add two vectors -- Press a")
	print("Dot product -- Press dp (WIP)")
	print("Cross product -- Press cp (WIP)")
	print("Quit ------------- Press q\n")

	mode = input("What do you want?\n")
	

	if(mode == 'c'):
		create_vector()
		clear()
	elif(mode == 'q'):
		quit()
	elif(mode == 's'):
		clear()
		show_all()
	elif(mode == 'a'):
		x = input("First vector: ")
		y = input("Second vector: ")
		for i in range(len(vectors_name)):
			if(vectors_name[i] == x): a = vectors[i]
			if(vectors_name[i] == y): b = vectors[i]
		print("Result: " + str(add_vectors(a, b)) + "\n")
