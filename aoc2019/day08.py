#!/usr/bin/env python3

import sys


def read_data(file):
    with open(file) as f:
        return str(f.read())


def parse_image(data, width, heigth):
    """Return layers"""
    layers = []
    idx = 0
    size = width * heigth
    while idx + size <= len(data):
        layers.append(data[idx:idx+size])
        idx += size
    return layers


def layer_with_fewest_zeroes(layers):
    zero_count = len(layers[0])  # init to all zeroes
    layer = -1
    for i in range(len(layers)):
        cnt = layers[i].count('0')
        if cnt < zero_count:
            layer = i + 1
            zero_count = cnt
    return layer


def layer_checksum(layers, layer):
    data = layers[layer-1]
    return data.count('1') * data.count('2')


def render_image(layers):
    size = len(layers[0])
    image = ''
    for i in range(size):
        added = False
        for layer in layers:
            if layer[i] != '2':
                image += layer[i]
                added = True
                break
        assert added
    return image


def print_image(image, width):
    image = image.replace('0', ' ')
    image = image.replace('1', 'o')  # Unicode: chr(2588)
    idx = 0
    while idx + width <= len(image):
        print(image[idx:idx+width])
        idx += width


def self_test():
    layers = parse_image('123456789012', 3, 2)
    print(layers)
    layer = layer_with_fewest_zeroes(layers)
    assert len(layers) == 2
    assert layer == 1
    assert layer_checksum(layers, layer) == 1
    layers = parse_image('0222112222120000', 2, 2)
    image = render_image(layers)
    print_image(image, 2)
    assert image == '0110'


if sys.argv[1] == '-t' or sys.argv[1] == '--test':
    self_test()
else:
    data = read_data(sys.argv[1])
    layers = parse_image(data, 25, 6)
    layer = layer_with_fewest_zeroes(layers)
    print(f"Layer check (fewest zeroes): {layer} -> {layer_checksum(layers, layer)}")
    image = render_image(layers)
    print_image(image, 25)
