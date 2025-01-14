class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #subtract current gas with cost 
        #iterate to the split which is current. tank + gas 
        if sum(gas) < sum(cost):
            return -1
        
        start, tank = 0,0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start
        # diff = []
        # for i in range(len(gas)):
        #     diff.append(gas[i] - cost[i])
        # currVal = 0
        # for i in range(len(gas)):
        #     curVal += gas[i] 
        # total_gas = 0
        # start, current_gas = 0,0
        # for i in range(len(gas)):
        #     fuel_gain = gas[i] - cost[i]
        #     total_gas += fuel_gain
        #     current_gas += fuel_gain

        #     if current_gas < 0:
        #         current_gas = 0
        #         start = i + 1

        # return -1 if total_gas < 0 else start