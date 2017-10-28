
from channel import Channel
from queue import Queue
import math
import random

l = 0.5
m = 1
v = 0.01
y = 0.1
n = 5

N = 1000000

incoming_requests = []
channel_breakages = []

def statistics(disc):
    Q = 1 - disc
    A = Q * l
    print("A: %f" %A)
    print("Q: %f" %Q)

def main():
    queue = Queue(n)
    channel = Channel(m,v,y)

    incoming_requests_time = 0
    channel_break_time = 0

    for i in range(N):
        incoming_requests_time += -math.log(random.random()) / l
        incoming_requests.append(incoming_requests_time)
        channel_break_time += -math.log(random.random()) / v
        channel_breakages.append(channel_break_time)


    channel_time = 0
    process_i = 0
    broken_i = 0
    is_channel_broken = False

    while process_i < N:
        if channel_breakages[broken_i] <= channel_time:
            channel_time += -math.log(random.random()) / y
            broken_i += 1
            is_channel_broken = True
        else:
            is_channel_broken = False
            if incoming_requests[process_i] >= channel_time:
                channel_time += -math.log(random.random()) / m
                channel.add_out()
            else:
                queue.add_item()

        process_i += 1

    statistics(queue.get_discards() / N)

if __name__ == "__main__":
    main()
