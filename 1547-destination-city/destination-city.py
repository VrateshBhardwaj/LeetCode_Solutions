class Solution(object):
    def destCity(self, paths):
        has_outgoing = set()

        for i in range(len(paths)):
            has_outgoing.add(paths[i][0])

        for j in range(len(paths)):
            if paths[j][1] not in has_outgoing:
                return paths[j][1]

        return ''

                
        