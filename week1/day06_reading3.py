"""Reading lab 3 - a Caesar cipher.

New here: strings are iterated character by character, indexing puts a
character back on the end of a new string, and `% 26` makes the alphabet
wrap around. No dates this time.

How to use (25 minutes, ladder steps 1 + 2):
  1. Read everything below the header WITHOUT running it.
  2. Answer the 5 questions at the bottom in reading-notes.md.
  3. Only then run:  python day06_reading3.py
  4. Trace encode("xyz", 3) by hand before you check it.

Question I should be able to answer afterwards:
   decode() is just encode() with a negative shift. Which line makes that
   work, and why does it need no special case for negative numbers?
"""

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = LOWER.upper()


def shift_char(ch, shift):
    "ch, shift -> ch moved `shift` letters along; anything else unchanged."
    if ch in LOWER:
        return LOWER[(LOWER.index(ch) + shift) % 26]
    if ch in UPPER:
        return UPPER[(UPPER.index(ch) + shift) % 26]
    return ch


def encode(text, shift):
    "text, shift -> every letter moved, punctuation and spacing kept."
    result = ""
    for ch in text:
        result += shift_char(ch, shift)
    return result


def decode(text, shift):
    return encode(text, -shift)


# ---------------------------------------------------------------- answer 5
# Write these in reading-notes.md BEFORE running the file.
if __name__ == "__main__":
    print("1) encode('abc', 1) =", repr(encode("abc", 1)))
    print("2) encode('xyz', 3) =", repr(encode("xyz", 3)))
    print("3) encode('Hello, World!', 1) =", repr(encode("Hello, World!", 1)))
    print("4) decode(encode('Week 1', 5), 5) =", repr(decode(encode("Week 1", 5), 5)))
    print("5) shift_char('a', -1) =", repr(shift_char("a", -1)),
          "   shift_char('a', -27) =", repr(shift_char("a", -27)))

'''prediction
i already know caesar cipher but i will analyse it in code
(1)  encode('abc', 1)
     for ch in abc-->result=shift_char(a,1)+shift_char(b,1)+shift_char(c,1)
     a,b,c are LOWER
     LOWER[(LOWER.index(a/b/c) + 1) % 26]
     LOWER(1)+LOWER(2)+LOWER(3)
     answer is bcd

(2)  encode('xyz', 3)
     for ch in xyz-->result=shift_char(x,3)+shift_char(y,3)+shift_char(z,3)
      x,y,z are LOWER
      LOWER[(LOWER.index(x/y/z) + 3) % 26]
      LOWER(0)+LOWER(1)+LOWER(2)
      answer is abc
    
(3) encode('Hello, World!', 1)
    so according to (1) (2) letters always become LOWER[(LOWER.index(ch) + shift) % 26] or upper version
    so Hello, World! in a1z26 is 8-5-12-12-15-0-23-15-18-12-4 then miuns 1 because index start with 0
    7,4,11,11,14,-1,22,14,11,3  then shift is 1 so add 1
    8-5-12-12-15-0-23-15-18-12-4 in LOWER[]
    answer is Ifmmp, Xpsme!

(4)decode(encode('Week 1', 5), 5) 
     decode(text, shift)=return encode(text, -shift)
     so encode(encode('Week 1', 5), -5) 
     shift 5 then back 5=shift 0
     answer is Week 1
    
(5)  shift_char('a', -1) and  shift_char('a', -27)
     a=LOWER[0]
     shift_char('a', -1) =LOWER[-1%26]  shift_char('a', -27)=LOWER[-27%26]
     both=LOWER[25]
     Both answer is z

prediction:
(1)bcd
(2)abc
(3)Ifmmp, Xpsme!
(4)Week 1
(5)z,z

Actual:
1) encode('abc', 1) = 'bcd'
2) encode('xyz', 3) = 'abc'
3) encode('Hello, World!', 1) = 'Ifmmp, Xpsme!'
4) decode(encode('Week 1', 5), 5) = 'Week 1'
5) shift_char('a', -1) = 'z'    shift_char('a', -27) = 'z'    


'''
