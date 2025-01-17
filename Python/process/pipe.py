import multiprocessing
#import multiprocessing.rocess
import time

def sender(pipe):
    messages = ["Hello", "How are you?", "Goodbye"]
    for msg in messages:
        print(f"Sending: {msg}")
        pipe.send(msg)
        time.sleep(1)
    pipe.send(None)  # Signal receiver to stop

def receiver(pipe):
    while True:
        msg = pipe.recv()
        if msg is None:  # Stop signal
            break
        print(f"Received: {msg}")

parent_conn, child_conn = multiprocessing.Pipe()

process1 = multiprocessing.Process(target=sender, args=(parent_conn,))
process2 = multiprocessing.Process(target=receiver, args=(child_conn,))

process1.start()
process2.start()

process1.join()
process2.join()

print("Pipe communication finished.")
