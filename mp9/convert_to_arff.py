

def convert_to_arff(filename, write_name):
    """This utility converts data from a csv dataset into the arff format."""

    # first read in data
    with open(filename, 'r') as F:
        lines = F.readlines()

    # write the header
    s = '% header\n'

    # write the name of the relation
    s += '@RELATION   ' + 'navigation\n'

    # loop through the data first to get class info
    data = ''
    classes = []
    for line in lines:
        data += line
        classes.append(line.split(',')[-1])

    # create a string for the different classes
    classes = set(classes)
    class_str = '{'
    for i, c in enumerate(classes):
        class_str += c.replace('\n', '')
        class_str += ',' if i != len(classes) - 1 else '}'

    # write the attributes
    n = len(lines[0].split(','))
    for i in range(n):
        if i != n - 1:
            s += '@ATTRIBUTE\tUS{}  \tNUMERIC\n'.format(i+1)
        else:
            s += '@ATTRIBUTE\tclass\t{}\n'.format(class_str)

    # here we'll write the @data
    s += '@DATA\n'
    s += data

    # finally, write the data to a file
    with open(write_name, 'w') as F:
        F.write(s)


if __name__ == '__main__':
    convert_to_arff('all_data/sensor_readings_24.data', 'MP9-1.arff')
