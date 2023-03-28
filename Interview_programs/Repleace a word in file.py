search_word= "index"
replace_word="testing"

with open("text_file.txt", 'r') as file:
    d=file.read()
    d=d.replace(search_word, replace_word)

with open("text_file.txt", 'w') as f:
    f.write(d)






