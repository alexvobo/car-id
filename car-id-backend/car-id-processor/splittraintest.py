from pathlib import Path
import threading

train_path = 'D:/Machine Learning/train'
test_path = 'D:/Machine Learning/test'

p = 'D:/Machine Learning/car-id'


def get_paths(data_path):
    return [child for child in Path(data_path).iterdir() if child.is_dir()]


def copy_files(files, out_dir):
    for file in files:
        file.replace(out_dir.joinpath(file.name))


def copy_thread(files, out_dir):
    copythread = threading.Thread(
        target=copy_files, args=(files, out_dir))
    copythread.start()


def main(data_path, out_path, train_ratio):
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
                train_len = int(len(files) * (train_ratio))
                training_files = files[:train_len]
                testing_files = files[train_len:]

                # 5 let's create the directories if it doesn't exist
                out_path_train = Path(train_path).joinpath(
                    brand.name).joinpath(model.name).joinpath(gen.name)
                out_path_test = Path(test_path).joinpath(
                    brand.name).joinpath(model.name).joinpath(gen.name)
                if not out_path_train.exists():
                    out_path_train.mkdir(parents=True)

                if not out_path_test.exists():
                    out_path_test.mkdir(parents=True)
                # 6 Now we can copy all the files from initial location to training/testing locations
                copy_thread(training_files, out_path_train)
                copy_thread(testing_files, out_path_test)


if __name__ == '__main__':

    main(p, 'test', 0.5)
