import time


class LinearSearch:

    def __init__(self, data, search):
        self.data = data
        self.search = int(search)

    def linear_search(self, draw_data, time_tick):
        for i in range(len(self.data)):
            draw_data(self.data, ['blue' if x == i else 'green' for x in range(len(self.data))],0)
            if self.data[i] == self.search:
                draw_data(self.data, ['blue' if x == i else 'green' for x in range(len(self.data))],2)
                return
            time.sleep(time_tick)
        draw_data(self.data, ['red' for _ in range(len(self.data))],1)
