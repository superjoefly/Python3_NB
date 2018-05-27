# Import Modules
import threading
import time

def main():
    # Create class:
    class MyMessenger(threading.Thread):
        # Define run function:
        def run(self):
            # Loop to print thread name:
            for _ in range(10):
                # Delay the loops:
                time.sleep(1)
                # Display current threads name:
                print(threading.currentThread().getName())

    # Create the threads:
    x = MyMessenger(name="Sending...")
    y = MyMessenger(name="Receiving...")

    # Run threads at the same time (threading):
    x.start()
    y.start()

main()
