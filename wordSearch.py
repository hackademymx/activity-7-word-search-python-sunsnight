from textwrap import wrap

def wordSearch(letters, words):
    
    letters = list(map(list, wrap(letters, 8)))
    rowLength = len(letters[0])
    colLength = len(letters)
   
    # Builds a string with the same length of the word and compares both, returns false or True
    def buildWord(row, col, move, word):
        charactInGrid = ''
        while(len(charactInGrid) < len(word)):
            charactInGrid += letters[row][col]
            row += move[0]
            col += move[1]
        return charactInGrid == word
    
    # After th position where the first character was found, verifies that there are the necessary number of characters to form the word being searched
    def compareLengthAndBuild(lengthInGrid, lengthOfWord, r, c, move, word):
        if(lengthInGrid >= lengthOfWord):
            if(buildWord(r, c, move, word)):
                return True
   
   # Function to make a search horizontally, vertically and diagonally
    def checkWord(word):
        wordLength = len(word)
        
        # Search in grid for the first char of the string 
        for row in range(0, rowLength):
            for col in range(0, colLength):
                if(letters[row][col] == word[0]):
                    # Right
                    if(compareLengthAndBuild(rowLength - col, wordLength, row, col, (0, 1), word)):
                        return True
                    # Left
                    if(compareLengthAndBuild(col + 1, wordLength, row, col, (0, -1), word)):
                        return True
                    # Up
                    if(compareLengthAndBuild(row + 1, wordLength, row, col, (-1, 0), word)):
                        return True
                    # Down
                    if(compareLengthAndBuild(colLength - row, wordLength, row, col, (1, 0), word)):
                        return True
                    # Diagonally up
                    if(row + 1 >= wordLength):
                        # Diagonally up-right
                        if(compareLengthAndBuild(rowLength - col, wordLength, row, col, (-1, 1), word)):
                            return True
                        # Diagonally up-left
                        if(compareLengthAndBuild(col + 1, wordLength, row, col, (-1, -1), word)):
                            return True
                    # Diagonally down
                    if(colLength - row >= wordLength):
                        # Diagonally down right
                        if(compareLengthAndBuild(rowLength - col, wordLength, row, col, (1, 1), word)):
                            return True
                        # Diagonally down left
                        if(compareLengthAndBuild(col + 1, wordLength, row, col, (1, -1), word)):
                            return True
        return False
    
    #Loops through the list of strings to be searched
    for word in words:
        word = word.upper()
        if(not checkWord(word)):
            return False
    return True