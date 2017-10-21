from channel import Channel
from queue import Queue
from request import Request

p = 0.5
p1 = 0.45
p2 = 0.35

iterations = 1000000

def calculate(channel_1, channel_2, queue, request):
    if channel_2.get_value() == 1:
        channel_2.generate()
        if channel_2.get_processed():
            channel_2.add_out()
            channel_2.set_value(0)
            if channel_1.get_value() == 1:
                channel_1.generate()
                if channel_1.get_processed():
                    channel_1.set_value(0)
                    channel_2.set_value(1)
                    if not queue.is_empty():
                        channel_1.set_value(1)
                        queue.remove_item()

            else:
                if not queue.is_empty():
                    channel_1.set_value(1)
                    queue.remove_item()
        else:
            if channel_1.get_value() == 1:
                channel_1.generate()
                if channel_1.get_processed():
                    channel_1.add_discard()
                    channel_1.set_value(0)
                    if not queue.is_empty():
                        channel_1.set_value(1)
                        queue.remove_item()
            else:
                if not queue.is_empty():
                    channel_1.set_value(1)
                    queue.remove_item()
    else:
        if channel_1.get_value() == 1:
            channel_1.generate()
            if channel_1.get_processed():
                channel_1.set_value(0)
                channel_2.set_value(1)

            if not queue.is_empty():
                if channel_1.get_value() == 0:
                    channel_1.set_value(1)
                    queue.remove_item()
        else:
            if not queue.is_empty():
                queue.remove_item()
                channel_1.set_value(1)

def statistics(channel_1, channel_2, request):
    all_requests = request.get_requests()
    all_discards = request.get_discards() + channel_1.get_discards()
    p_otk = (all_discards / all_requests)

    print("All requests: %d" %all_requests)
    print("A: %d" % channel_2.get_outs())
    print("P_otk: %f" % p_otk)
    print("Q: %f" % (1 - p_otk))

def main():
    request = Request(p)
    queue = Queue()
    channel_1 = Channel(p1)
    channel_2 = Channel(p2)

    for i in range(iterations):
        request.generate()
        if request.was_request():
            if queue.is_empty():
                queue.add_item()
                calculate(channel_1, channel_2, queue, request)
            else:
                calculate(channel_1, channel_2, queue, request)
                if not queue.is_empty():
                    request.add_discard()
                else:
                    queue.add_item()
        else:
            calculate(channel_1, channel_2, queue, request)


    statistics(channel_1, channel_2, request)

if __name__ == "__main__":
    main()
