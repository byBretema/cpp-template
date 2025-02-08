import os
import sys
import shutil
import subprocess
import argparse

def command_exists(cmd):
    return shutil.which(cmd) is not None

def error_exit(message):
    print(f"[ERR] - {message}", file=sys.stderr)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Build script")
    parser.add_argument("-c", "--cleanup", action="store_true", help="Cleanup build directory")
    parser.add_argument("-r", "--release", action="store_true", help="Build in Release mode")
    parser.add_argument("-g", "--cmakegen", type=str, default="Ninja", help="CMake generator")
    args = parser.parse_args()

    # Check required commands
    if not command_exists("uvx"):
        error_exit("Command 'uvx' is required (https://docs.astral.sh/uv/#installation)")
    if not command_exists("cmake"):
        error_exit("Command 'cmake' is required")

    build_type = "Release" if args.release else "Debug"
    cmake_gen = args.cmakegen

    if cmake_gen == "Ninja" and not command_exists("ninja"):
        error_exit("Command 'ninja' is required")

    build_dir = "build"

    # Cleanup
    if args.cleanup and os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir, exist_ok=True)

    # Change to build directory
    os.chdir(build_dir)

    # Deps management
    conan_profile = os.path.expanduser("~/.conan2/profiles/default")
    if not os.path.exists(conan_profile):
        subprocess.run(["uvx", "conan", "profile", "detect"], check=True)

    subprocess.run([
        "uvx", "conan", "install", "..", f"-s=build_type={build_type}", "--build=missing", "-of=."]
    , check=True)

    # Config + Build
    preset = "conan-default" if os.name == "nt" else f"conan-{build_type.lower()}"
    subprocess.run([
        "cmake", "-G", cmake_gen, "..", f"--preset={preset}",
        f"-DCMAKE_BUILD_TYPE={build_type}", "--no-warn-unused-cli"
    ], check=True)

    subprocess.run(["cmake", "--build", ".", "-j", str(os.cpu_count()), "--config", build_type], check=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        error_exit("User interrupts execution.")
    except PermissionError:
        error_exit("Some files are in use, cannot run the script.")
    except Exception as e:
        error_exit(f"Unexpected... {type(e)} :: {e}")
