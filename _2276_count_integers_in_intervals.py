class CountIntervals:

    def __init__(self):
        self.intervals = []

    def add(self, left: int, right: int) -> None:
        if len(self.intervals) == 0:
            self.intervals.append([left, right])
        else:
            st_idx = ed_idx = None
            for idx in range(len(self.intervals)):
                interval = self.intervals[idx]
                if interval[0]

    def count(self) -> int:
        s = set()
        for i in self.intervals:
            s |= set(i)
        return len(s)



# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

if __name__ == "__main__":
    obj = CountIntervals()
    obj.add(2, 3)
    obj.add(7, 10)
    print(obj.count())
    obj.add(5, 8)
    print(obj.count())
