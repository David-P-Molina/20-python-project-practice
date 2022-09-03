def replace_word(): #how to define a method
    #indentation defines open and closing of function/methods
    str = "Hi guys, I am David, and hi hi hi hi" #Create variables regardless of datatypes
    word_to_replace = input("Enter the word you wish to replace")#input is a function that takes user input
    word_replacer = input("Enter new word taking place")
    print(str.replace(word_to_replace, word_replacer))#use print() instead of console.log()-JavaScript or System.out.println()-Java

replace_word()#Lack of indentation means exit previous method ##Call method created