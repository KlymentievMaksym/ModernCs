import unittest
import sys
import lab1


class Tests(unittest.TestCase):
    def test_different_shape(self):
        csv_with_different_shape = ['text, text, text\n', 'text, text\n', 'text, rehire\n', 'text, text, text\n']
        exit_code = lab1.transorm_from_csv_to_json(csv_with_different_shape)
        self.assertEqual(exit_code, 1)
    
    def test_different_values(self):
        csv_with_different_shape = ['Name,Index,Will continue\n', 'AlGeom,1,True\n', 'ModernCS,2.0,False\n']
        exit_code, json_text = lab1.transorm_from_csv_to_json(csv_with_different_shape, receive_stdout=True)
        self.assertEqual(exit_code, 0)
        self.assertEqual(json_text, '[{"Name": "AlGeom", "Index": 1, "Will continue": "True"}, {"Name": "ModernCS", "Index": 2.0, "Will continue": "False"}]')


if __name__ == '__main__':
    unittest.main()
