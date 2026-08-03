class Solution:

    def ishappy(self, n: int) -> bool:
        record = set()

        while True:
            n = self.get_sum(n)
            if n == 1:
                return True

            if n in record:
                return False
            else:
                record.add(n)

    def get_sum(self, n: int) -> int:
        new_sum = 0
        while n:
            n, r = divmod(n, 10)
            new_sum += r ** 2
        return new_sum