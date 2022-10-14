from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from typing import Optional
from src.process.process import process_images
from src.utils.loaders import *

DEFAULT_OUTPUT_PATH_SUFFIX = "_aug"


class App:
    def __init__(self, config: Config, output_dir: Optional[str]):
        self.config = config
        self.output_dir = output_dir

    def __trigger_process(self, dir_path: str) -> None:
        images = load_images_from_dir(dir_path)
        process_images(images, self.config, self.output_dir)

    def __select_dir(self) -> None:
        path = filedialog.askdirectory(initialdir=".")
        print(path)

        if self.output_dir == None:
            self.output_dir = f"{path}{DEFAULT_OUTPUT_PATH_SUFFIX}"

        if not os.path.isdir(self.output_dir):
            os.mkdir(self.output_dir)

        print(self.output_dir)
        self.__trigger_process(path)

    def run(self) -> None:
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()
        ttk.Label(self.frame, text="Select a directory to process").grid(
            column=0, row=0
        )
        ttk.Button(self.frame, text="Quit", command=self.root.destroy).grid(
            column=0, row=1
        )
        ttk.Button(self.frame, text="Select Directory", command=self.__select_dir).grid(
            column=1, row=1
        )
        self.root.mainloop()
