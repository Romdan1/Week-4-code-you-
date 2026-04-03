def caesar_cipher(text, shift):
    
    result = ""
    
    for char in text:
      
        if char.isupper():
           
            number = ord(char) - ord('A')
           
            number = (number + shift) % 26
         
            new_char = chr(number + ord('A'))
            result += new_char
        
       
        elif char.islower():
          
            number = ord(char) - ord('a')
          
            number = (number + shift) % 26
            
            new_char = chr(number + ord('a'))
          
            result += new_char
        
        
        else:
           
            result += char
    
    return result



print(caesar_cipher("Hello, World!", 3))  
print(caesar_cipher("abcXYZ", 2))         
print(caesar_cipher("Python 3.9", 5))   