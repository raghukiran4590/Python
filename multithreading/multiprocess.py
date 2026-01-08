import multiprocessing
import time
import requests

def function1(name):
    print(f'started process-1: {name}')
    print(f'ended process-1: {name}')

def function2(name):
    print(f'started process-2: {name}')
    print(f'ended process-2: {name}')

def function3(name):
    print(f'started process-3: {name}')
    print(f'ended process-3: {name}')

def fetch_url(url):
    response = requests.get(url)
    print(f'Fetched {url} with status code: {response.status_code}')

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=function1, args=('process-1',))
    process2 = multiprocessing.Process(target=function2, args=('process-2',))
    process3 = multiprocessing.Process(target=function3, args=('process-3',))
    process4 = multiprocessing.Process(target=fetch_url, args=('https://www.example.com',))

    process1.start()
    process2.start()
    process3.start()
    process4.start()


    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('All processes have finished execution.')
    time.sleep(1)  # Just to ensure all print statements are flushed before the main program exits
    print('Main program ends here.')

