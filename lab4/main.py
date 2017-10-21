from channel import Channel
from queue import Queue
from request import Request

p = 0.5
p1 = 0.45
p2 = 0.35

iterations = 1000000


def main():
    request = Request(p)
    queue = Queue()
    channel_1 = Channel(p1)
    channel_2 = Channel(p2)

    for i in range(iterations):
        channel_1.generate()
        channel_2.generate()
        request.generate()

        if (channel_2.get_processed() == False):
            if (channel_1.get_processed()):
                channel_1.add_discard()

            if not queue.is_empty() and channel_1.get_processed():
                channel_1.set_processed(False)
                queue.remove_item()

            if (request.has_request() == True):
                if (queue.is_full()):
                    request.add_discard()
                    request.set_has_request(False)
                elif (not queue.is_full() and not queue.is_empty()):
                    queue.add_item()
                    request.set_has_request(False)
                else:
                    if (channel_1.get_processed() == True):
                        channel_1.add_item()
                        request.set_has_request(False)
                    else:
                        queue.add_item()
                        request.set_has_request(False)
        else:


        if (channel_1.get_state()):
            if ()

        if (request.get_state()):
            if queue.is_full():
                request.add_discard()
            else:
                queue.add_item()


if __name__ == "__main__":
    main()
