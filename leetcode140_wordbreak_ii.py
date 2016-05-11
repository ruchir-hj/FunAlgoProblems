class Solution(object):
    
    def wordBreak(self, s, wordDict):
         """
         :type s: str
         :type wordDict: Set[str]
         :rtype: List[str]
         """
 
         stringLength = len(s)
         possible = [False for _ in xrange(stringLength)]
         valid = [[False] * stringLength for _ in xrange(stringLength)]

         for i in xrange(stringLength):
              if s[:i+1] in wordDict:
                  possible[i] = True
                  valid[0][i] = True

              for j in xrange(i):
                   if possible[j] and s[j+1:i+1] in wordDict:
                       valid[j+1][i] = True
                       possible[i] = True

         result = []

         if possible[stringLength - 1]:
             self.genPath(s, valid, 0, [], result)
         return result


    def genPath(self, s, valid, start, path, result):
        if start == len(s):
            result.append(" ".join(path))
            return

        for i in xrange(start, len(s)):
              if valid[start][i]:
                  path += [s[start:i+1]]
                  self.genPath(s, valid, i + 1, path, result)
                  path.pop()

 
