# Makefile for building the embedded project

CC = arm-none-eabi-gcc
CFLAGS = -Wall -O2 -mcpu=cortex-m4 -mthumb
LDFLAGS = -T stm32f4xx.ld

SRC = src/main.c src/model.c src/input_preprocessing.c src/output_postprocessing.c
INCLUDE = -Iinclude -Itensorflow/lite/micro

OBJ = $(SRC:.c=.o)

all: hvac_classifier

hvac_classifier: $(OBJ)
    $(CC) $(CFLAGS) $(OBJ) -o hvac_classifier $(LDFLAGS)

%.o: %.c
    $(CC) $(CFLAGS) $(INCLUDE) -c $< -o $@

clean:
    rm -f $(OBJ) hvac_classifier

.PHONY: all clean
