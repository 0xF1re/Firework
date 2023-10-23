path = /home/$(shell whoami)/.firework
all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD)/kernel_module modules
uninstall:
	sudo rm -rf $(path)
install:
	sudo python3 src/tools/useradd.py
	mkdir $(path) $(path)/plugins
	cp -r kernel_module $(path)
	cp -r src/pluginManager $(path)
	cp src/launcher.py $(path)
	cp src/main.py $(path)
	cp requerements.txt $(path)
clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD)/kernel_module clean
