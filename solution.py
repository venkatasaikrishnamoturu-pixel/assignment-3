class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        # cost[i] = cheapest price to reach city i
        cost = [float('inf')] * n

        # Starting city has cost 0
        cost[src] = 0

        # At most k stops = k + 1 flights
        for _ in range(k + 1):

            # Copy the previous costs
            # This prevents using more than one flight in one iteration
            temp = cost.copy()

            # Check every flight
            for from_city, to_city, price in flights:

                # If from_city is reachable
                if cost[from_city] != float('inf'):

                    # Try taking this flight
                    temp[to_city] = min(
                        temp[to_city],
                        cost[from_city] + price
                    )

            # Update costs
            cost = temp

        # Destination cannot be reached
        if cost[dst] == float('inf'):
            return -1

        return cost[dst]