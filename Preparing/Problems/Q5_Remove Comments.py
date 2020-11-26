class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        return filter(None, re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n'))
