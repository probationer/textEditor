import sys
from difflib import Differ, SequenceMatcher, HtmlDiff
from .path_manager import StorePath, Inventory_file

def fileCompare(old_file_input, new_file_input):
    with open("/Users/vs/Documents/output.html", 'w') as output_file:
        with open(old_file_input, 'r') as old_file:
            with open(new_file_input,'r') as new_file:
                while True:
                    old_line_size = len(old_file.readline())
                    new_line_size = len(new_file.readline())
                    if (old_line_size == 0 or new_line_size == 0 ):
                        break
                    flag = True
                    while flag:
                        new_line = new_file.read(new_line_size)
                        print(new_line)
                        if new_line == '':
                            break
                        while True:
                            old_line = old_file.read(old_line_size)
                            print(old_line)
                            if old_line == '':
                                flag = False
                                break
                            if old_line == new_line:
                                output_file.write(old_line)
                                break
                            else:
                                string = old_line.replace("<p>", "<p><strong>")
                                string = string.replace("</p>","</strong></p>")
                                output_file.write(string)
                        if flag is False:
                            string = old_line.replace("<p>", "<p><e>")
                            string = string.replace("</p>","</e></p>")
                            output_file.write(string)
                            
                            
                    

            # same = file_for_inetersetion.intersection(new_file)
            
            
            
            
            # diff = old_file_set.symmetric_difference(new_file_set)
            # diff.discard('\n')
            # print(diff)

            # with open("/Users/vs/Documents/output.html", 'w') as output_file:
            #     for l in new_file_set:
            #         print(l)
            #         if l in diff:
            #             string = str("<strong>"+l+"</strong>").replace("<p>", "<p><strong>")
            #             string = string.replace("</p>","</strong></p>")
            #             output_file.write(string)
            #         else:
            #             output_file.write(l)
            # output_file.close()

def LCS(word1, word2):
    print(word1, word2)
    word1 = list(word1)
    word2 = list(word2)
    len1 = len(word1)
    len2 = len(word2)

    #initialize 2d array:
    matrix = [[0 for x in range(len1+1)] for y in range(len2+1)] 
    print(matrix)
    for i in range(1, len1):
        for j in range(1, len2):
            if (word1[i] == word2[j]):
                matrix[i][j] = matrix[i-1][j-1] +1
            else:
                matrix[i][j] = matrix[i-1][j] if matrix[i-1][j]>matrix[i][j-1] else matrix[i][j-1]  
            
    changes = getSubsequence(matrix, len1, len2)
    print(changes)

def getSubsequence(matrix, word_len1, word_len2):
    r = word_len1
    c = word_len2
    changes = list()
    print(r,c)
    for i in matrix:
        print(i)
    while(r>0 and c>0):
        if (matrix[r][c] > matrix[r-1][c] and matrix[r-1][c] == matrix[r][c-1]):
            changes.append((r,c))
            r-=1
            c-=1
        elif (matrix[r][c] == matrix[r-1][c] and matrix[r][c] == matrix[r][c-1]):
            r-=1
        elif (matrix[r-1][c] > matrix[r][c-1]):
            r-=1
        elif (matrix[r-1][c] < matrix[r][c-1]):
            c-=1 
    return changes

def fileCompare1(old_file_input, new_file_input):
    
    output_str = ""
    # with open("/Users/vs/Documents/output.html", 'w') as output_file:
    old_file = open(old_file_input, 'r')
    old_file_set = set(old_file)
    new_file = open(new_file_input, 'r')
    diff = old_file_set.symmetric_difference(new_file)
    # print(diff)
    old_file = open(old_file_input, 'r')
    new_file = open(new_file_input, 'r')
    Flag = True
    while Flag:
        old_line = old_file.readline()   
        if old_line == '':
            break
        if old_line in diff:
            diff.remove(old_line)
            output_str += (old_line.replace("<p>","<p>-"))
        else: 
            while True:
                new_line = new_file.readline()
                if new_line == '':
                    Flag = False
                    break
                if old_line == new_line:
                    output_str += (old_line)
                    break
                if new_line in diff:
                    diff.remove(new_line)
                    output_str += (new_line.replace("<p>","<p>+"))

    print(output_str)


def CheckOldVersion(file_path):
    pass

def fileCompare2(new_file_input):
    if Inventory_file(new_file_input):
        return True
    else:
        StorePath(path_json = '/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/.meta/', file_path)
        return False

    if CheckOldVersion(new_file_input):
        with open(old_file_input, 'r') as old_file:
            with open(new_file_input, 'r') as new_file:
                ds = list(Differ().compare(old_file.readlines(),new_file.readlines()))
                sq = SequenceMatcher(None,'qabxcd', 'abycdf')
        return ds
    else:
        return False

    

if __name__ == "__main__":
    # arguments = sys.argv[1:]
    # if len(arguments) != 1:
    #     print('please enter two digits')
    # else:
        # fileCompare2('/Users/vs/Documents/page1.txt', arguments[0])
    fileCompare2('/Users/vs/Documents/page1.txt', '/Users/vs/Documents/page2.txt')