

import unittest
class TestMethods(unittest.TestCase):
    def test_freq(self):
        self.assertEqual(freq(),'ba')

def freq():
    l = ["foo", "foo", "bar", "bar", "bar", 'ba', 'ba', 'ba', 'ba']
    d = {}
    for word in l:
        if word not in d.keys():
            d[word] = 1
        elif word in d.keys():
            d[word] += 1
        else:
            print("HELP YOU BROKE ME.")

    maximum = 0
    maxString = ''
    for i in d.keys():
        if d[i] > maximum:
            maximum = d[i]
            maxString = i

    return maxString
if __name__ == '__main__':
    unittest.main()