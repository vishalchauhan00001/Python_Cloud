import time


class BubbleSort:

    def __init__(self, data):
        self.data = data

    def bubble_sort(self, draw_data, time_tick):
        for _ in range(len(self.data) - 1):
            for j in range(len(self.data) - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    draw_data(self.data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(self.data))],0)
                    time.sleep(time_tick)
        draw_data(self.data, ['green' for _ in range(len(self.data))],0)
