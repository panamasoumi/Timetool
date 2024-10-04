import time

def stopwatch():
    print("Press Enter to start and Ctrl+C to stop the stopwatch.")
    input()     
    print("Started...")
    start_time = time.time()    

    try:
        while True:
            elapsed_time = time.time() - start_time  
            mins, secs = divmod(elapsed_time, 60)  
            timer = f'{int(mins):02d}:{int(secs):02d}'
            print(timer, end="\r")  
            time.sleep(1)  
    except KeyboardInterrupt:
        print("\nStopped at:", timer)  
if __name__ == "__main__":
    stopwatch()
