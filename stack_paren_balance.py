from stack import Stack

def is_match_paren(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False
    

def is_paren_balanced(paren_string):
    s = Stack()
    is_paren_balanced = True
    for paren in paren_string:
        if paren in "({[":
            s.push(paren)
        else:
            print("else : ", paren)
            if s.is_empty():
                is_paren_balanced = False
                break;
            else:
                top = s.pop()            
                print("match  : ", is_match_paren(top, paren))
                if is_match_paren(top, paren) is False:
                    print("falseinnnn")
                    is_paren_balanced = False
                    break;

    if is_paren_balanced and s.is_empty():
        return "String is balanced"
    else:
        return "String is not balanced"


str = "{(([])[])[]]}"
print(is_paren_balanced(str)) 