import json
import os
import tomllib

from .convert_platform import convert_cpu_arch_to_npm_cpu_arch, convert_os_to_npm_os

def write_package_json(platform_path, rust_target, my_binary_name):
    parts = rust_target.split("-")
    if len(parts) == 3:
        cpu_arch, _vendor, os_name = parts
    else:
        cpu_arch, _vendor, os_name, _env = parts[0], parts[1], parts[2], parts[3]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, "../../package.json")) as f:
        base_package_name = json.load(f)["name"]
    with open(os.path.join(script_dir, "../../../Cargo.toml"), "rb") as f:
        version = tomllib.load(f)["package"]["version"]

    name = base_package_name + "-" + convert_os_to_npm_os(os_name) + "-" + convert_cpu_arch_to_npm_cpu_arch(cpu_arch)
    package_json = {
        "name": name,
        "version": version,
        "os": [convert_os_to_npm_os(os_name)],
        "cpu": [convert_cpu_arch_to_npm_cpu_arch(cpu_arch)],
        "main": my_binary_name,
        "license": "MPL-2.0",
        "repository": {"type": "git", "url": "https://github.com/Privitty/core.git", "directory": "deltachat-rpc-server"},
    }
    with open(platform_path + "/package.json", "w") as f:
        f.write(json.dumps(package_json, indent=4))
