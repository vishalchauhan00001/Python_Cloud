import time


class BinarySearch:

    def __init__(self, data, search):
        self.data = data
        self.search = int(search)

    def binary_search(self, draw_data, time_tick):
        data = self.data
        search = self.search
        low = 0
        high = len(data) - 1
        # mid = 0

        found = False

        while low <= high:
            mid = (high + low) // 2
            draw_data(self.data, ['blue' if (x == mid or x == low or x == high) else 'green' for x in range(len(self.data))],0)
            time.sleep(time_tick)

            if data[mid] == search:
                draw_data(self.data, ['blue' if x == mid else 'green' for x in range(len(self.data))],2)
                found = True
                break
            elif data[mid] < search:
                low = mid + 1
            else:
                high = mid - 1

        if not found:
            draw_data(self.data, ['red' for _ in range(len(self.data))],1)
            


