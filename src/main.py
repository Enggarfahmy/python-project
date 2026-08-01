import sys


def check_environment() -> None:
    """Fungsi untuk mengecek lingkungan Python yang aktif."""
    print("==========================================")
    print("🚀 Python Industrial Setup Active!")
    print(f"Python Version : {sys.version.split()[0]}")
    print(f"Executable Path: {sys.executable}")
    print("==========================================")


if __name__ == "__main__":
    check_environment()
