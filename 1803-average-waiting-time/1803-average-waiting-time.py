class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        chef_busy = customers[0][0] + customers[0][1]
        customer_waiting = customers[0][1]

        for i in range(1, n):
            if chef_busy < customers[i][0]:
                chef_busy = customers[i][0]

            chef_busy += customers[i][1]
            customer_waiting += (chef_busy - customers[i][0])

        print(customer_waiting)

        return customer_waiting / n