import time


class QuickSort:

    def __init__(self, data):
        self.data = data

    def partition(self, data, head, tail, draw_data, time_tick):
        border = head
        pivot = data[tail]

        draw_data(data, self.get_color_array(len(data), head, tail, border, border),0)
        time.sleep(time_tick)

        for j in range(head, tail):
            if data[j] < pivot:
                draw_data(data, self.get_color_array(len(data), head, tail, border, j, True),0)
                time.sleep(time_tick)

                data[border], data[j] = data[j], data[border]
                border += 1

            draw_data(data, self.get_color_array(len(data), head, tail, border, j))
            time.sleep(time_tick)

        # swap pivot with border value
        draw_data(data, self.get_color_array(len(data), head, tail, border, tail, True),0)
        time.sleep(time_tick)

        data[border], data[tail] = data[tail], data[border]

        return border

    def quick_sort(self, data, head, tail, draw_data, time_tick):
        if head < tail:
            partition_idx = self.partition(data, head, tail, draw_data, time_tick)

            # LEFT PARTITION
            self.quick_sort(data, head, partition_idx - 1, draw_data, time_tick)

            # RIGHT PARTITION
            self.quick_sort(data, partition_idx + 1, tail, draw_data, time_tick)

    @staticmethod
    def get_color_array(data_len, head, tail, border, curr_idx, is_swaping=False):
        color_array = []
        for i in range(data_len):
            # base coloring
            if head <= i <= tail:
                color_array.append('gray')
            else:
                color_array.append('white')

            if i == tail:
                color_array[i] = 'blue'
            elif i == border:
                color_array[i] = 'red'
            elif i == curr_idx:
                color_array[i] = 'yellow'

            if is_swaping:
                if i == border or i == curr_idx:
                    color_array[i] = 'green'

        return color_array
