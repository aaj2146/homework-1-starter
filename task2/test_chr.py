import io
def charcount(x):
    
    with io.open(x) as infile:
        words = 0
        characters = 0
        for lineo,line in enumerate(infile,1):
            wordslist = line.split()
            words += len(wordslist)
            characters += sum(len(word) for word in wordslist)
            
            
        return characters

def test_charcount():
    assert charac_count('input.txt') == 6