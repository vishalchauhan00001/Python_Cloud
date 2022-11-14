import time


class MergeSort:

    def __init__(self, data):
        self.data = data

    def merge_sort(self, draw_data, time_tick):
        self.merge_sort_alg(self.data, 0, len(self.data) - 1, draw_data, time_tick)

    def merge_sort_alg(self, data, left, right, drawData, timeTick):
        if left < right:
            middle = (left + right) // 2
            self.merge_sort_alg(data, left, middle, drawData, timeTick)
            self.merge_sort_alg(data, middle + 1, right, drawData, timeTick)
            self.merge(data, left, middle, right, drawData, timeTick)

    def merge(self, data, left, middle, right, draw_data, time_tick):
        draw_data(data, self.get_color_array(len(data), left, middle, right),0)
        time.sleep(time_tick)

        left_part = data[left:middle + 1]
        right_part = data[middle + 1: right + 1]

        left_idx = right_idx = 0

        for dataIdx in range(left, right + 1):
            if left_idx < len(left_part) and right_idx < len(right_part):
                if left_part[left_idx] <= right_part[right_idx]:
                    data[dataIdx] = left_part[left_idx]
                    left_idx += 1
                else:
                    data[dataIdx] = right_part[right_idx]
                    right_idx += 1

            elif left_idx < len(left_part):
                data[dataIdx] = left_part[left_idx]
                left_idx += 1
            else:
                data[dataIdx] = right_part[right_idx]
                right_idx += 1

        draw_data(data, ["green" if left <= x <= right else "white" for x in range(len(data))],0)
        time.sleep(time_tick)

    @staticmethod
    def get_color_array(length, left, middle, right):
        color_array = []

        for i in range(length):
            if left <= i <= right:
                if left <= i <= middle:
                    color_array.append("yellow")
                else:
                    color_array.append("pink")
            else:
                color_array.append("white")

        return color_array
