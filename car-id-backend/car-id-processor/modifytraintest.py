from os import name
from pathlib import Path
import threading
from PIL import Image
from multiprocessing import Process
import os
import tensorflow as tf
train_path = 'D:/Machine Learning/train'
test_path = 'D:/Machine Learning/test'


train_out = train_path+'-MODIFIED'
test_out = test_path+'-MODIFIED'

lock = threading.Lock()


def get_paths(data_path):
    return [child for child in Path(data_path).iterdir() if child.is_dir()]


def copy_files(files, out_dir):
    for file in files:
        file.replace(out_dir.joinpath(file.name))


def copy_thread(files, out_dir):
    copythread = threading.Thread(
        target=copy_files, args=(files, out_dir))
    copythread.start()


def moveFiles(data_path, out_path):
    # 1 get brand paths
    brand_paths = get_paths(data_path)
    for brand in brand_paths:
        # 2 get model paths
        model_paths = get_paths(brand)
        for model in model_paths:
            # 3 get generation paths
            gen_paths = get_paths(model)
            for gen in gen_paths:
                # 4 each gen contains image files for that brand/model/gen (path is the label)
                files = list(gen.iterdir())
                # 5 let's create the directories if they don't exist
                fix_gen = "-".join(g.strip() for g in gen.name.split("-"))
                folder_name = brand.name+"_"+model.name+"_"+fix_gen

                out_path_new = Path(out_path).joinpath(
                    folder_name)

                if not out_path_new.exists():
                    out_path_new.mkdir(parents=True)

                # 6 Now we can copy all the files from initial location to training/testing locations

                copy_thread(files, out_path_new)


def make_path(parent_folder, folder_name, index):
    return parent_folder+"/" + folder_name+"_"+index+".jpg"


def fix_paths(parent_path):

    pics = list(parent_path.iterdir())
    paths_to_fix = [p for p in pics if "(" in str(p)]

    if paths_to_fix:
        num_total = len(pics)
        num_broken = len(paths_to_fix)
        num_to_start = num_total-num_broken

        for p in paths_to_fix:
            folder_name = str(p).split('\\')[-2]
            try:
                os.rename(p, make_path(str(parent_path),
                                       folder_name, str(num_to_start)))
            except Exception as e:
                print("Could not fix " + str(p))
            num_to_start += 1
        # print(str(pics[0]).split('\\')[-2] + " fixed")


def verify(parent_path):
    pics = list(parent_path.iterdir())
    for pic in pics:
        #! WE HAVE TO TEST IF IMAGE IS BROKEN WITH PIL

        filecontents = tf.io.read_file(str(pic))
        try:
            image = tf.io.decode_image(filecontents, channels=3)
        except Exception:
            # print out the names of corrupt files
            # lock.acquire()
            os.remove(pic)
            # lock.release()


def renameFiles(p):
    paths = get_paths(p)
    for car_path in paths:
        # print('in '+car_path.name)
        verify(car_path)

        print("Done with " + car_path.name)


if __name__ == '__main__':
    pro1 = Process(target=renameFiles, args=(train_path,))
    pro2 = Process(target=renameFiles, args=(test_path,))

    pro1.start()
    pro2.start()

    pro1.join()
    pro2.join()
    # Process(target=moveFiles, args=(train_path, train_out)).start()
    # Process(target=moveFiles, args=(train_path, train_out)).start()
    #  t1 = threading.Thread(
    #      target=moveFiles, args=(train_path, train_out))
    #  t2 =  threading.Thread(
    #      target=moveFiles, args=(test_path, test_out))

    #  t1.start()
    #  t2.start()

    #  t1.join()
    #  t2.join()
