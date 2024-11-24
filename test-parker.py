accz_values=[]

# Open the file (replace 'your_data_file.txt' with the actual filename)
with open('data/20241110173358.txt', 'r') as file:
    counter=0
    # Read each line
    for line in file:
       # print(line)
        # Split the line into columns (assuming space or tab separation)
        columns = line.split()

        accz_values.append(columns[5])


        # # Check if the line has enough columns (ensure it has AsZ(°/s) data)
        # if len(columns) > 6:  # Adjust this number based on the actual number of columns
        #     try:
        #         # Extract the value for AsZ(°/s) from the 7th column (index 6)
        #         AsZ_value = float(columns[6])  # Convert the value to a float if it's numeric
        #         print(AsZ_value)  # Print only the numeric value
        #     except ValueError:
        #         # Skip rows where the AsZ value is not a valid number
        #         continue
        # print(counter)
        # counter=counter+1
        # # if counter > 4:
        #     break
        ########################the first column is 1 whitespace to far, be careful about which numbers you choose.

removed_element=accz_values.pop(0)
print(accz_values)
print(removed_element)