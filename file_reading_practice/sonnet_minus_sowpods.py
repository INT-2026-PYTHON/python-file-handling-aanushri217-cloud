"""
## 6. Words in sonnet_words.txt but NOT in sowpods.txt  *(Hard)*

=================================================
WORDS UNIQUE TO THE SONNET
=================================================

Problem Statement:
Read the text files `sowpods.txt` and
`sonnet_words.txt`. PRINT every word that
appears in `sonnet_words.txt` but does NOT
appear in `sowpods.txt`.

This problem is about CHOOSING THE RIGHT DATA
STRUCTURE. If you check each sonnet word
against the SOWPODS list with a nested loop,
the work is O(N*M). Using SETS turns the
membership check into O(1), giving you an
overall O(N + M) algorithm.

-------------------------------------------------
Input Example:
sowpods.txt sample:
   thee
   love
   summer
   day
   eyes
   shall
   more

sonnet_words.txt sample:
   shall
   i
   compare
   thee
   to
   a
   summer
   day

Output Example:
Words in sonnet but not in sowpods:
['a', 'compare', 'i', 'to']
Total: 4

-------------------------------------------------
Explanation:
sonnet words -> {'shall', 'i', 'compare',
                 'thee', 'to', 'a', 'summer',
                 'day'}
sowpods set   -> {'thee', 'love', 'summer',
                  'day', 'eyes', 'shall',
                  'more'}
Difference (sonnet - sowpods)
              -> {'i', 'compare', 'to', 'a'}
After sorting -> ['a', 'compare', 'i', 'to'].
=================================================

"""
def sonnet_not_in_sowpods(sowpods_file,sonnet_file):
    
    with open(sowpods_file, "r") as file:
        sowpods_set = set()

        for word in file:
            sowpods_set.add(word.strip().lower())

    with open(sonnet_file, "r") as file:
        sonnet_set = set()

        for word in file:
            sonnet_set.add(word.strip().lower())

    result = sorted(sonnet_set - sowpods_set)

    print("words in sonnet but not in sowpodas:")
    print(result)
    print("Total:", len(result))

sonnet_not_in_sowpods(
    "file_reading_practice/sowpods.txt",
    "file_reading_practice/sonnet_words.txt"
    )
