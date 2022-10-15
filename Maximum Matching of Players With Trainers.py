class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count=0
        point1=0
        point2=0
        while point1<len(players) and point2<len(trainers):
            temp1=players[point1]
            temp2=trainers[point2]
            if temp1>temp2:
                point2+=1
            if temp2>=temp1:
                count+=1
                point1+=1
                point2+=1
        return count
            