class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openers_to_closers_mapping = {
	    '{' : '}',
	    '[' : ']',
	    '(' : ')'
        }
        
        openers = frozenset(openers_to_closers_mapping.keys())
        closers = frozenset(openers_to_closers_mapping.values())

    	openers_stack = []
    
        for char in s:
		    if char in openers:
			    openers_stack.append(char)

		    elif char in closers:
			    #edge case : if stack is empty
			    if not openers_stack:
				    return False
			    else:
				    last_unclosed_opener = openers_stack.pop()
				    
				    if not openers_to_closers_mapping[last_unclosed_opener] == char:
				    	return False
        return openers_stack == []

