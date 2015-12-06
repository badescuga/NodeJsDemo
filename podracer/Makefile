all: lib
	gcc -Wall unicorn.c -o unicorn -I../../python/rpi-ws281x/lib -L../../python/rpi-ws281x/lib -lm -lws2811 -lpng

lib:
	make -C ../../python/rpi-ws281x/lib/ lib

clean:
	-rm unicorn easy

clearhat:
	gcc -Wall clearhat.c -o clearhat -I../../python/rpi-ws281x/lib -L../../python/rpi-ws281x/lib -lm -lws2811

play:
	gcc -Wall play.c -o play -I../../python/rpi-ws281x/lib -L../../python/rpi-ws281x/lib -lm -lws2811 -lpng
easy:
	gcc -Wall easy.c -o easy -I../../python/rpi-ws281x/lib -L../../python/rpi-ws281x/lib -lm -lws2811
