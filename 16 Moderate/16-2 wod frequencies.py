def solution(book):
    # brute force way 
    wfht = {} # word frequency hash table
    start = 0
    end = 0
    while end < len(book):
        if book[end] == " " and book[start:end] in wfht:
            wfht[book[start:end]] += 1
            start = end+1
            end = end+2
            continue
        elif book[end] == " ":
            wfht[book[start:end]] = 1
            start = end+1
            end = end+2
            continue
        end += 1
    if book[start:end] in wfht:
        wfht[book[start:end]] += 1
    else:
        wfht[book[start:end]] = 1
    print(wfht)


if __name__ == '__main__':
    book = "is a nope is nop"
    solution(book)