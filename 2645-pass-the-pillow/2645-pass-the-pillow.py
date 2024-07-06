class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        position = 1 # By default pillow at 1

        num_of_round = time // (n - 1)

        movement = time % (n - 1)

        if num_of_round % 2 == 0:
            position += movement
        else:
            position = n - movement

        return position
        