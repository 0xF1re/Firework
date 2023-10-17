path = /home/$(shell whoami)/.firework
all:
	cargo build
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD)/kernel_module modules
uninstall:
	sudo rm -rf $(path)
install:
	sudo python3 src/tools/useradd.py
	mkdir $(path) $(path)/plugins
	cp target/debug/Firework $(path)
	cp -r kernel_module $(path)
	cp -r src/pluginManager $(path)
	cp src/launcher.py $(path)
	sudo chown firework:firework $(path) -R
	sudo chmod a+x $(path) -R
clean:
	rm -rf target
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD)/kernel_module clean
debug:
	cargo build
	sudo insmod kernel_module/firemodule.ko
	sudo target/debug/Firework
