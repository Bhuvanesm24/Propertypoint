name = input(str("enter the name"))
vowels = "aeiouAEIOU"
# vowel_list = [char for char in name if char in vowels]
# print(vowel_list)


for char in name:  # Loop through each character in the name
    if char in vowels:  # Check if the character is a vowel
        print(char)
        # vowel_list.append(char)  # Add vowel to the list
