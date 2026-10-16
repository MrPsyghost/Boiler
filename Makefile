.PHONY: build

PYTHON = .venv/Scripts/python.exe
ISCC = "C:\Users\shiva\AppData\Local\Programs\Inno Setup 6\ISCC.exe"

run: clean build cfg clean-after-build

clean-after-build:
	cmd /c "if exist build rmdir /s /q build"
	cmd /c "if exist boiler.spec del /q boiler.spec"

clean:
	cmd /c "if exist build rmdir /s /q build"
	cmd /c "if exist dist rmdir /s /q dist"
	cmd /c "if exist boiler.spec del /q boiler.spec"

installer:
	$(ISCC) compiler.iss

build:
	"$(PYTHON)" -m PyInstaller \
		--clean \
		--noconfirm \
		--onefile \
		--name boiler \
		--icon src/boiler.ico \
		--add-data "src/boiler.cfg;." \
		--collect-all pyfiglet \
		src/main.py

cfg:
	"$(PYTHON)" -c "import shutil; shutil.copy2('src/boiler.cfg', 'dist/boiler.cfg')"