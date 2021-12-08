lines = []
with open("input.txt") as my_file:
    for line in my_file:
        lines.append(line.strip().split("| "))

total = 0

for line in lines:
    signal_patterns = line[0].split()
    output_values = line[1].split()
    eight = set("abcdefg")
    
    for signal_pattern in signal_patterns:
        if len(signal_pattern) == 2:
            one = set(signal_pattern)
        elif len(signal_pattern) == 3:
            seven = set(signal_pattern)
        elif len(signal_pattern) == 4:
            four = set(signal_pattern)
    
    bovenstelijn = seven - one
    linksboven_midden = four - one

    
    # throw signal patterns we know away.
    signal_patterns = [set(signal_pattern) for signal_pattern in signal_patterns if set(signal_pattern) != one and set(signal_pattern) != four and set(signal_pattern) != seven and set(signal_pattern) != eight]

    # deduce 3 from the fact length 5 and contains everything from 7
    for signal_pattern in signal_patterns:
        if len(signal_pattern) == 5 and seven.issubset(signal_pattern):
            three = signal_pattern
            onderstelijn = three - four.union(seven)
            linksonder = eight - three.union(four)
            linksboven = four - three
            midden = linksboven_midden - linksboven
            #deduce nine from 8 - linksonder
            nine = eight - linksonder
            zero = eight - midden
            break
    
    signal_patterns.remove(three)
    signal_patterns.remove(nine)
    signal_patterns.remove(zero)

    for signal_pattern in signal_patterns:
        if len(signal_pattern) == 6:
            six = signal_pattern
            rechtsboven = eight - six
            rechtsonder = one - rechtsboven
            five = eight - rechtsboven - linksonder
            two = eight - linksboven - rechtsonder
            break

    subtotal = ""
    print(len(output_values))
    for output_value in output_values:
        
        output_value = set(output_value)
        if output_value == zero:
            subtotal += "0"
        elif output_value == one:
            subtotal += "1"
        elif output_value == two:
            subtotal += "2"
        elif output_value == three:
            subtotal += "3"
        elif output_value == four:
            subtotal += "4"
        elif output_value == five:
            subtotal += "5"
        elif output_value == six:
            subtotal += "6"
        elif output_value == seven:
            subtotal += "7"
        elif output_value == eight:
            subtotal += "8"
        if output_value == nine:
            subtotal += "9"
    print(subtotal)
    total += int(subtotal)
print(total)