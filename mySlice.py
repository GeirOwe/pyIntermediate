class XIter:
    def __getitem__(self, index):
        if isinstance(index, int):
            return index
        elif isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            return start, stop, step

x = XIter()
x[5]
#  5
x[::]
#  (None, None, None)
x[3:100:8]
#  (3, 100, 8)