
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Initialize the iterator from the iterable
        self.count = 0  # Counter for items iterated

    def __next__(self):
        # Increment the count and get the next item
        self.count += 1
        return next(self.iterator)  # Fetch the next item

    def get_count(self):
        return self.count  # Return the count of items iterated
    