def count_letters(text: str) -> dict[str, int]:
    result = {}
    text = text.lower()

    for char in text:
        if char.isalpha():          
            if char not in result:
                result[char] = 0
            result[char] += 1

    return result
    
text = 'assalomu alaykum'
print(count_letters(text))
