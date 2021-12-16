#!/usr/bin/env python3

import sys
import task


class Dec16a(task.StrTask):
    """
    """
    def get_versionsum(self, binarydigits):
        version, typeid = int(''.join(binarydigits[:3]), 2), int(''.join(binarydigits[3:6]), 2)
        del binarydigits[:6]

        versionsum = version
        if typeid == 4:
            while True:
                pkt, bits = binarydigits[0], binarydigits[1:5]
                del binarydigits[:5]
                if pkt == '0':
                    break
        else:
            lengthtypeid = binarydigits[0]
            if lengthtypeid == '0':
                numbits = int(''.join(binarydigits[1:16]), 2)
                subpacketbinarydigits = binarydigits[16:numbits + 16]
                del binarydigits[:numbits + 16]
                while True and subpacketbinarydigits:
                    if len(list(filter(lambda x: x == '0', subpacketbinarydigits))) == len(subpacketbinarydigits):
                        break

                    versionsum += self.get_versionsum(subpacketbinarydigits)
            else:
                numsubpackets = int(''.join(binarydigits[1:12]), 2)
                del binarydigits[:12]
                for i in range(numsubpackets):
                    versionsum += self.get_versionsum(binarydigits)

        return versionsum
        
    def run(self, line):
        binarydigits = list(''.join(map(lambda x: '{0:04b}'.format(int(x, 16)), line)))

        versionsum = 0
        while binarydigits:
            if len(list(filter(lambda x: x == '0', binarydigits))) == len(binarydigits):
                break

            versionsum += self.get_versionsum(binarydigits)
        return versionsum

class Dec16b(task.StrTask):
    """
    """
    def parsepacket(self, binarydigits):
        version, typeid = int(''.join(binarydigits[:3]), 2), int(''.join(binarydigits[3:6]), 2)
        del binarydigits[:6]

        if typeid == 4:
            valuebits = []
            while True:
                bitpktheader, bits = binarydigits[0], binarydigits[1:5]
                del binarydigits[:5]
                valuebits += bits
                if bitpktheader == '0':
                    break

            value = int(''.join(valuebits), 2)
        else:
            subvalues = []
            lengthtypeid = binarydigits[0]
            if lengthtypeid == '0':
                numbits = int(''.join(binarydigits[1:16]), 2)
                subpacketbinarydigits = binarydigits[16:numbits + 16]
                del binarydigits[:numbits + 16]
                while True and subpacketbinarydigits:
                    if len(list(filter(lambda x: x == '0', subpacketbinarydigits))) == len(subpacketbinarydigits):
                        break

                    subvalues.append(self.parsepacket(subpacketbinarydigits))
            else:
                numsubpackets = int(''.join(binarydigits[1:12]), 2)
                del binarydigits[:12]
                for i in range(numsubpackets):
                    subvalues.append(self.parsepacket(binarydigits))
            
            if typeid == 0:
                value = sum(subvalues)
            elif typeid == 1:
                value = 1
                for prod in subvalues:
                    value *= prod
            elif typeid == 2:
                value = min(subvalues)
            elif typeid == 3:
                value = max(subvalues)
            elif typeid == 5:
                value = 1 if subvalues[0] > subvalues[1] else 0
            elif typeid == 6:
                value = 1 if subvalues[0] < subvalues[1] else 0
            elif typeid == 7:
                value = 1 if subvalues[0] == subvalues[1] else 0

        return value
        
    def run(self, line):
        binarydigits = list(''.join(map(lambda x: '{0:04b}'.format(int(x, 16)), line)))

        value = 0
        while binarydigits:
            if len(list(filter(lambda x: x == '0', binarydigits))) == len(binarydigits):
                break

            value += self.parsepacket(binarydigits)
        return value

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Dec16a().run_tests_from_commandline()
        Dec16b().run_tests_from_commandline()
    else:
        Dec16a().runtests()
        Dec16b().runtests()
