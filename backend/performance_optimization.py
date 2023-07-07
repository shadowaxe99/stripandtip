```python
import os
import threading
from queue import Queue
from video_processing import process_video
from image_processing import process_image
from storage_system import store_file

class Worker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            function, args = self.queue.get()
            try:
                function(*args)
            finally:
                self.queue.task_done()

def optimize_performance():
    num_worker_threads = os.cpu_count() * 2
    queue = Queue()

    for _ in range(num_worker_threads):
        worker = Worker(queue)
        worker.daemon = True
        worker.start()

    for video in videos_to_process:
        queue.put((process_video, (video,)))

    for image in images_to_process:
        queue.put((process_image, (image,)))

    for file in files_to_store:
        queue.put((store_file, (file,)))

    queue.join()
```