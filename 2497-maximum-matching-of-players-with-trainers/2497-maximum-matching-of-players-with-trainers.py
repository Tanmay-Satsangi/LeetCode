class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p = len(players)
        t = len(trainers)

        players.sort()
        trainers.sort()

        l = 0
        r = 0

        while (l < p and r <  t):
            if players[l] <= trainers[r]:
                l += 1
            r += 1

        return l