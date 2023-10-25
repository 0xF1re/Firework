path = /home/$(shell whoami)/.firework
all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD)/kernel_module modules
uninstall:
	sudo rm -rf $(path)
install:
	mkdir $(path) $(path)/plugins
	cp -r kernel_module $(path)
	cp firework/launcher.py $(path)
	cp firework/main.py $(path)
	cp requerements.txt $(path)
clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD)/kernel_module clean
