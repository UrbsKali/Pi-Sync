from cx_Freeze import setup, Executable

setup(name="Pi Sync",
      version="1.0",
      description="The Best sync app of the market \n Why ? because it's me !",
      executables=[Executable(script="Pi-Sync.pyw", base = "Win32GUI",)])
