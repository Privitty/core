def convert_cpu_arch_to_npm_cpu_arch(arch):
    if arch == "x86_64":
        return "x64"
    if arch == "i686":
        return "ia32"
    if arch == "aarch64":
        return "arm64"
    if arch in ("armv7", "arm"):
        return "arm"
    return arch

def convert_os_to_npm_os(os):
    if os == "windows":
        return "win32"
    if os in ("darwin", "linux"):
        return os
    if os.startswith("android"):
        return "android"
    return os
