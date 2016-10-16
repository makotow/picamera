import os
import sys

from datetime import datetime
import time
import picamera


def create_output_file(outpu_dir):
    expand_output_dir = os.path.expanduser(output_dir)
    file_name = datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".jpg"
    return open(os.path.join(expand_output_dir,file_name), 'wb')


def capture(output_dir):
    output_file = create_output_file(output_dir)
    camera = picamera.PiCamera()

    try:
        camera.start_preview()
        time.sleep(2.0)
        camera.capture(output_file)

    finally:
        camera.close()

    output_file.close()

if __name__ == '__main__':
    args = sys.argv
    output_dir = args[1]
    if os.path.exists(output_dir):
        capture(output_dir)
    else:
        print("Does not exist output directory. ")
