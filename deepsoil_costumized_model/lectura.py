import re

# Data reading

mylines = []
with open ('test1.dp', 'rt') as myfile:
    for myline in myfile:
        mylines.append(myline)
#print(mylines)

# String game

# Searching number of layers
## Obtaining the row of the target
row_searched = [index for index, line in enumerate(mylines) for i in range(len(line)) if line.startswith("[NUM_LAYERS]", i)]

## Obtaining the number of layers
n_layers = re.findall(r'\d+', mylines[row_searched[0]])[0]

## Replace the value with a new value of n_layers
n_layers_new = str(int(n_layers) + 1)
mylines[row_searched[0]] = mylines[row_searched[0]].replace(n_layers, n_layers_new)

print(mylines[row_searched[0]])
