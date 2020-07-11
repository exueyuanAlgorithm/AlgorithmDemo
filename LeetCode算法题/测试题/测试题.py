class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        mothList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        dateArray = date.split(" ")
        print(dateArray)
        year = dateArray[-1]
        day = dateArray[0][:-2]
        if len(day) == 1:
            day = "0" + day
        month = str(mothList.index(dateArray[1]) + 1)
        if len(month) == 1:
            month = "0" + month
        return year + "-" + month + "-" + day


solution = Solution()
print(solution.reformatDate("20th Oct 2052"))
