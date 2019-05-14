import sys
from difflib import Differ, SequenceMatcher, HtmlDiff
from path_manager import StorePath, Inventory_file
from models.sqlite_connect import select_query
from models.document_table import (NEW, STAGED, COMMIT, MERGED)
from models.stage_table import staging_create_or_update, get_staging_data
from pprint import pprint
import re


# pattern1 +  ^^^^^^^
# pattern2 ++  ++++++
# pattern3    ^^^^^^^

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

def start_end_position(sr, regex):
    positions_list = list()
    start_position = end_position = -1
    pattern = re.compile(regex)
    while True :
        l = pattern.search(sr, end_position)
        if l is None :
            break
        start_position = l.start()
        end_position = l.end()
        positions_list.append((start_position, end_position))

    print(positions_list)
    return positions_list

def CheckOldVersion(file_path):
    query = 'SELECT * FROM document WHERE file_path = "{}"'.format(file_path)
    rows = select_query(sql=query)
    if rows:
        if (rows[0][4] == str(NEW)):
            return rows[0][4], None
        elif rows[0][4] == str(STAGED):
            return rows[0][4], rows[0][0] 
        elif rows[0][4] == str(COMMIT):
            return rows[0][4], rows[0][0]
    else:
        raise ("Something went wrong")

def fileCompare2(new_file_input):
    
    status, doc_id = CheckOldVersion(new_file_input)
    print(status)
    if status == str(STAGED):
        content = get_staging_data(doc_id)[0][2]
        with open(new_file_input, 'r') as new_file:
            new_data = new_file.read()
            ds = list(Differ().compare(new_data.splitlines(), content.splitlines()))
        print(create_output(ds))
    elif status == str(COMMIT):
        pass
    else:
        # with open(old_file_input, 'r') as old_file:
        pass
        # with open(new_file_input, 'r') as new_file:
        #     ds = list(Differ().compare(old_file.readlines(),new_file.readlines()))
        #     # sq = SequenceMatcher(None,'qabxcd', 'abycdf')
        # return ds

def create_output(diff_list):
    pprint(diff_list)
    print("\n\n")
    output_list = list()
    for count, line in enumerate(diff_list):
        new_line = str()
        if line[0] == '-':            
            new_line = line.replace('- ', '')
            new_line = new_line.replace('<p>', '<p><span style="background-color: dimgrey;">')
            new_line = new_line.replace('</p>','</span></p>')
            output_list.append(new_line)
        elif line[0] == '+':
            try:
                if diff_list[count+1][0] == '?':
                    changed_line = question_mark(diff_list[count+1], line)
                    changed_line = changed_line.replace('+ ', '')
                    # i = 0
                    # while True:
                    #     if diff_list[count-i][0] == '-':
                    #         break
                    #     i += 1
                    output_list[len(output_list) - 1] = changed_line
            except IndexError as e:
                new_line = line.replace('+ ', '')
                new_line = new_line.replace('<p>', '<p><span style="background-color: darkseagreen;">')
                new_line = new_line.replace('</p>','</span></p>')
        elif line[0] == '?':
            pass
        else:
            output_list.append(diff_list[count].strip())

    return list_to_string(output_list)

def question_mark(line1, line2):
    line1 = line1.replace('?', '')
    marking_list_1 = start_end_position(line1, r"[\+]+")
    marking_list_2 = start_end_position(line1, r"[\^]+")
    above_line = line2
    new_line = str()
    end = -1
    if marking_list_1:
        start = marking_list_1[0][0]
        if marking_list_2: 
            end = marking_list_2[-1][1]
        else:
            end = marking_list_1[-1][1]
        new_line += above_line[0:start+1] + '<span style="text-decoration: underline dashed darkgreen;">' + above_line[(start+1):(end+1)]
        new_line += '</span>' + above_line[(end+1):]
    if marking_list_2 and end != marking_list_2[-1][1]:
        start = marking_list_2[0][0]
        end = marking_list_2[-1][1]
        new_line += above_line[0:start+1] + '<span style="text-decoration: underline dashed darkgreen;">' + above_line[(start+1):(end+1)]
        new_line += '</span>' + above_line[(end+1):]
    return new_line

def list_to_string(list):
    data = str()
    for line in list:
        data += line
    return data

if __name__ == "__main__":
    # arguments = sys.argv[1:]
    # if len(arguments) != 1:
    #     print('please enter two digits')
    # else:
        # fileCompare2('/Users/vs/Documents/page1.txt', arguments[0])
    fileCompare2('/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/test1.txt')
    # print(CheckOldVersion('/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/text1.txt'))
    # diff_list = ['- <p>hey</p>','  <p>this will be line 1</p>','- <p>this is line 2</p>','?          ^\n','+ <p>this will be line 2</p>','?         + ^^^^^\n']
    # diff_list = ['  <p>this will be line 1</p>','- <p>this will be line 2</p>','?              ^^\n','+ <p>this will word line 2</p>','?              ^^^^\n','- <p>this line a word</p>','+ <p>this line has word missing</p>','?              + +     ++++++++\n','+ <p>this line missing</p>']
    # create_output(diff_list)
    # start_end_position('?              + +     ++++++++\n',r'[\+]+')