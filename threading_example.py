"""Threading Example"""

# The following program uses threading:


# Import Modules
import threading
import time


# The main() function creates a threading class and
# starts the threads which run simultaneously:
def main():
    """This is the main function:"""

    # Create class:
    class MyMessenger(threading.Thread):
        """This is the MyMessenger Class"""

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


# Call main:
main()
