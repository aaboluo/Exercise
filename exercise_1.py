"""
Write a Python program that…
    • Reads the file file_to_read.txt
    • Calculates the total times the word “terrible” appears (without quotes) and then
    displays it
    • Then replaces every EVEN occurrence of the word “terrible” with “pathetic”, and
    every ODD occurrence of the word “terrible” with “marvellous”.
    • The new text that you get after the above replacement of the word “terrible” must be
    written to a new file called result.txt
    • Commit your exercise solution to your GitHub account
    • Enter the URL of your exercise repository in the “Exercise 1 Submission Box”
NOTE: We are aware that solutions for the above exercise can be found quite easily online.
It is okay to look for ideas and syntax and some help with pieces of your code. However,
please try to put those pieces together to build your own code. Avoid using an already
available solution.
"""
import string


if __name__ == '__main__':
    with open("file_to_read.txt", "r") as f1:
        old_txt = f1.read().strip()

    # backup
    back_old_txt = old_txt

    # all punctuation
    for p in string.punctuation:
        back_old_txt = back_old_txt.replace(p, " ")

    # • Calculates the total times the word “terrible” appears (without quotes) and
    # then displays it
    terrible_count = len([i for i in back_old_txt.split(" ") if i == "terrible"])
    print("Calculates the total times the word “terrible” appears (without quotes) and then displays it:", terrible_count)

    # • Then replaces every EVEN occurrence of the word “terrible” with “pathetic”, and
    # every ODD occurrence of the word “terrible” with “marvellous”.
    index = 1
    old_txt_list = old_txt.split(" ")
    new_txt_list = []
    for word in old_txt_list:
        if "terrible" in word:
            new_word = "marvellous" if index % 2 == 1 else "pathetic"
            word = word.replace("terrible", new_word)
            index += 1
        new_txt_list.append(word)
    new_txt = " ".join(new_txt_list)

    # • The new text that you get after the above replacement of the word “terrible” must be
    # written to a new file called result.txt
    with open("result.txt", "w") as f2:
        f2.write(new_txt)
