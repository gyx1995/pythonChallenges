ACROSS = 0
DOWN = 1


# blanks = [(start_x, start_y, direction, length), ...]

def zip_sol(answer, blanks,vocab):
    for i in range(len(vocab)):
        filled_blank = blanks[i][0],blanks[i][1],blanks[i][2],vocab[i]
        answer.append(filled_blank)
    return answer


# fill the word into the blank, if success return 1, 0 otherwise
def check(blanks,vocab):
    size = max(x[3] for x in blanks ) + 1
    gird = [[' ']*size for n in range(size)]
    for i in range(len(vocab)):
        blank = blanks[i]
        word = vocab[i]
        start_x = blank[0]
        start_y = blank[1]
        direction = blank[2]
        for l in range(len(word)):
            if direction == 0:
                new_x, new_y = start_x + l , start_y
            else:
                new_x, new_y = start_x, start_y + l
            w = gird[new_x][new_y]
            if w != ' ' and w != word[l]:
                return False
            gird[new_x][new_y] = word[l]
    return True


def crossword_helper(answer,blanks, vocab, vocab_index):
    if answer:
        return answer
    if len(vocab) == vocab_index:
        if check(blanks, vocab):
            zip_sol(answer,blanks,vocab)

    for i in range(vocab_index, len(vocab)):
        if blanks[vocab_index][3] >= len(vocab[i]):
            vocab[i], vocab[vocab_index] = vocab[vocab_index], vocab[i]
            crossword_helper(answer, blanks, vocab, vocab_index + 1)
            vocab[i], vocab[vocab_index] = vocab[vocab_index], vocab[i]

    return None



def solve_crossword(vocab, blanks):
    # basic check
    vocab_lens = sorted([len(v) for v in vocab ])
    blanks_lens = sorted([b[3] for b in blanks])
    for i in range(len(vocab_lens)):
        try:
            blank_len = blanks_lens[i]
        except:
            return None
        if blank_len < vocab_lens[i]:
            return None

    # do recursion to fill in the words
    vocab = sorted(vocab, key=len)
    blanks = sorted(blanks, key=(lambda x:x[3]))
    vocab_index = 0
    answer = []
    crossword_helper(answer, blanks,vocab,vocab_index)
    if answer == []:
        return None
    else:
        return answer



# soln = solve_crossword(vocab=['next', 'time', 'expect', 'electric'],
#   blanks=[(0, 0, ACROSS, 4),(1, 0, DOWN, 6),(3, 0, DOWN, 4),(1, 3, ACROSS, 8)])
# print(soln)
