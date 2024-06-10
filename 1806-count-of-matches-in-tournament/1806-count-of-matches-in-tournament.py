class Solution:
    def numberOfMatches(self, n: int) -> int:
        return self.countMatches(n, 0)

    def countMatches(self, team, match_count):
        if team == 1:
            return match_count

        match_count += team // 2

        if team % 2 != 0:  #odd
            return self.countMatches(team //2 + 1, match_count)

        else:   #even
            return self.countMatches(team // 2, match_count)
        