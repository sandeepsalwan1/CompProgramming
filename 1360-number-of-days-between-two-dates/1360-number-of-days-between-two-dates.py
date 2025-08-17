class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        months = [31,28,31,30,31,30,31, 31,30,31,30,31]
        def findDate(input):
            curNum = 0
            curList = []
            for i in input:
                if i.isdigit():
                    curNum = curNum * 10 + int(i)
                else:
                    curList.append(curNum)
                    curNum = 0
            curList.append(curNum)
            y,m,d = curList[0], curList[1], curList[2]

            cur, toDays, i = m, 0, 0
            while cur != 1:
                cur -= 1
                toDays += months[i]
                i += 1

            toDays += d
            toDays += 365 * y

            # minimal leap fix (two lines + 1 if):
            toDays += ( (y-1)//4 - (y-1)//100 + (y-1)//400 )   # leap days from *previous* full years
            if m > 2 and (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)):  # after Feb in a leap year
                toDays += 1

            return toDays

        return abs(abs(findDate(date1)) - abs(findDate(date2)))
