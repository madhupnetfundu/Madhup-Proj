# class Solution:


#     def __init__(self, low, high):
#         self.low = low
#         self.high = high
#         self.oddnoslist = []

#     def countOdds(self):
#         for i in range(self.low, self.high+1):
#             if i % 2 == 1:
#                 self.oddnoslist.append(i)
#         # print(oddnoslist)

#     def get_list(self):
#         return self.oddnoslist
    
#     def get_list_length(self):
#         return len(self.oddnoslist)

# sol1= Solution(5,15)
# sol1.countOdds()
# print(sol1.get_list())
# print(sol1.get_list_length())



# class ListManipulator:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.list = []

#     def push_odds(self):
#         for i in range(self.start, self.end+1):
#             if i % 2 == 1:
#                 self.list.append(i)

#     def get_list(self):
#         return self.list


# # Example usage
# list_manipulator = ListManipulator(1, 10)
# list_manipulator.push_odds()
# print(list_manipulator.get_list())


class Solution:

    def __init__(self, low: int, high: int) -> int: 

        # What does -> mean in Python function definitions?
        #The -> (arrow) is used to annotate the return value for a function in Python 3.0 or later. It does not affect the program but is intend to be consumed by other users or libraries as documentation for the function.
        self.low = low
        self.high = high
        self.mylist = []

    def odd_nos_list(self):
        for i in range(self.low, self.high+1):
            if i % 2 == 1:
                self.mylist.append(i)

    def get_list(self):
        return self.mylist

    def get_list_length(self):
        return len(self.mylist)

sol2=Solution(1,5)
sol2.odd_nos_list()
print(sol2.get_list())
print(sol2.get_list_length())
