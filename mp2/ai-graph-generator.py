number_of_nodes = int(input("Number of nodes: "))
start_node = int(input("Start node: "))
goal_node = int(input("Goal node: "))

fileString = str(number_of_nodes)+"\n"
fileString+= str(start_node)+" S\n"
fileString+= str(goal_node)+" G\n"
fileString+= "#list\n"

print("Enter a path cost between nodes if exists, else 0")
for i in range(0, number_of_nodes):
    for j in range (0, number_of_nodes):
        if i != j:
            cost = int(input("Path cost from " + str(i) + " to " + str(j) + " "))
            if(cost != 0):
                fileString+=str(j)+"."+str(cost)+" - "
    fileString+= "!\n"
print(fileString)

print("Enter heuristic value for each node...")

for i in range(0, number_of_nodes):
    fileString+= input("For node " + str(i) +" ") + "\n"

with open("Output.aig", "w") as aig_file:
    aig_file.write(fileString)
