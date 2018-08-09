# -*- coding: utf-8 -*-
import os

if __name__ == '__main__':
    print(os.path.dirname(os.path.abspath('.')))
    print(os.path.abspath(os.path.join(os.path.dirname(__file__))))
    print(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))