def openfile():
    with open("/home/denningb/workspace/github.com/wrath39/bookbot/books/frankenstein") as f:
        # ...
        file_contents = f.read()
    return file_contents
    
def file_split(file_contents):
    file_word_split=file_contents.split()
    return file_word_split

def word_count(file_word_split):
    file_word_count=len(file_word_split)
    return file_word_count

def main():
    file_contents = ""
    file_word_split = ""
    file_word_count = 0

    file_contents = openfile()
    file_word_split = file_split(file_contents)
    file_word_count = word_count(file_word_split)
    
    print(file_word_count)
    #print(file_contents)

main()