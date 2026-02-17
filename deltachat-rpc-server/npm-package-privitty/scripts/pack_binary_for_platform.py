import subprocess
import sys
from os import path, makedirs, chdir, chmod
from shutil import copy

# run from npm-package-privitty/
chdir(path.join(path.dirname(path.abspath(__file__)), "../"))

if len(sys.argv) < 3:
    print("Usage: pack_binary_for_platform.py <cargo-target> <binary_path>")
    sys.exit(1)

target = sys.argv[1].strip()
binary_path = sys.argv[2].strip()

out = subprocess.run(["rustc", "--print", "target-list"], capture_output=True, check=True)
if target not in out.stdout.decode("utf-8"):
    print("Unknown target:", target)
    sys.exit(1)

makedirs("platform_package", exist_ok=True)
platform_path = "platform_package/" + target
makedirs(platform_path, exist_ok=True)

binary_name = path.basename(binary_path)
dest = platform_path + "/" + binary_name
copy(binary_path, dest)
chmod(dest, 0o555)

from src.make_package import write_package_json
write_package_json(platform_path, target, binary_name)
