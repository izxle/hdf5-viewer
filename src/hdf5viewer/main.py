"""HDF5 File Viewer entry point."""

import argparse
import logging
import os
import sys

from PyQt6.QtWidgets import QApplication

from hdf5viewer.cli.parse_cli_args import parse_cli_args
from hdf5viewer.gui.main_window import MainWindow

if sys.platform == "win32":
    # Set Windows Taskbar Icon
    import ctypes

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("hdf5viewer")


def main() -> None:
    """HDF5 File Viewer entry point."""
    parser = argparse.ArgumentParser(
        prog="HDF5 File Viewer",
        description="A File Viewer for HDF5 Files.",
    )
    parser.add_argument("filename", help="H5 file to load", nargs="?", default="")
    parser.add_argument("-e", "--export", help="Export H5 File to output file")
    parser.add_argument(
        "-l", "--list", help="List all Groups and Datasets", action="store_true"
    )
    parser.add_argument(
        "-t",
        "--tree",
        help="List all Groups and Datasets recursively as tree",
        action="store_true",
    )
    parser.add_argument(
        "-p", "--plain", help="Disable pretty printing", action="store_true"
    )
    parser.add_argument(
        "-d", "--debug", help="Enable debug logging", action="store_true"
    )
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(
            level=0,
            format="%(asctime)s: [%(levelname)s] - %(message)s",
            handlers=[
                logging.FileHandler(os.path.join("hdf5viewer.log")),
                logging.StreamHandler(sys.stdout),
            ],
            force=True,
        )
    else:
        logging.basicConfig(
            level=20,
            format="%(asctime)s: [%(levelname)s] - %(message)s",
            handlers=[logging.StreamHandler(sys.stdout)],
            force=True,
        )

    if args.export is not None or any([args.list, args.tree]):
        parse_cli_args(args)
    else:
        logging.info("Starting as gui")
        app = QApplication(sys.argv)
        app.setOrganizationName("HDF5Viewer")
        app.setApplicationName("HDF5ViewerPython")
        main_win = MainWindow(init_file_path=args.filename)
        main_win.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    main()
