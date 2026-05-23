import time

class Timer:
    def __enter__(self):
        #save start time
        self.start_time = time.time()
        return self

    def __exit__(self, *args):
        #calculate elapsed time 
        elapsed_time = time.time() - self.start_time

        print(f"Elapsed time: {elapsed_time:.4f} seconds")
        

with Timer():
    #simulation time with sleep
    time.sleep(1)
    print("Done!")