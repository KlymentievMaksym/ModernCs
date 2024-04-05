import unittest
import os
import lab1


class Tests(unittest.TestCase):
    
    def test_different_values(self):
        csv_with_different_shape = ['Name,Index,Will continue\n', 'AlGeom,1,True\n', 'ModernCS,2.0,False\n']
        exit_code, json_text = lab1.transorm_from_csv_to_json(csv_with_different_shape, receive_stdout=True)
        self.assertEqual(exit_code, 0)
        self.assertEqual(json_text, '[{"Name": "AlGeom", "Index": 1, "Will continue": "True"}, {"Name": "ModernCS", "Index": 2.0, "Will continue": "False"}]')

    def test_valid_input(self):
        csv_with_different_shape = ['Name,Index,Will continue\n', 'AlGeom,1,True\n', 'ModernCS,2.0,False\n']
        exit_code, json_text = lab1.transorm_from_csv_to_json(csv_with_different_shape, receive_stdout=True)
        self.assertEqual(exit_code, 0)
        self.assertEqual(json_text, '[{"Name": "AlGeom", "Index": 1, "Will continue": "True"}, {"Name": "ModernCS", "Index": 2.0, "Will continue": "False"}]')
    
    def test_invalid_input(self):
        csv_with_different_shape = ['Name,Index,Will continue\n', 'AlGeom,1,True\n', 'ModernCS,2.0,False\n', 'text, text\n']
        exit_code = lab1.transorm_from_csv_to_json(csv_with_different_shape)
        self.assertEqual(exit_code, 1)
        csv_with_different_shape = 'Name,Index,Will continue\nAlGeom,1,True\n'
        exit_code = lab1.transorm_from_csv_to_json(csv_with_different_shape, absolute_false=False)
        self.assertEqual(exit_code, 2)
        
    def test_empty_input(self):
        csv_with_different_shape = []
        exit_code = lab1.transorm_from_csv_to_json(csv_with_different_shape)
        self.assertEqual(exit_code, 0)
    
    def test_not_exist_file(self):
        os.system('type 3.csv 2> stderr1.txt | python lab1.py > NUL 2> NUL')
        with open('stderr1.txt', 'r') as f:
            stderr = f.read()
            self.assertEqual(stderr, 'The system cannot find the file specified.\n')
        
    def test_empty_file(self):
        os.system('type 2.csv | python lab1.py > stdin.txt 2> NUL')
        with open('stdin.txt', 'r') as f:
            stdin = f.read()
            self.assertEqual(stdin, '[]\n')
        
    def test_errors_to_stderr(self):
        os.system('type 1.csv | python lab1.py > NUL 2> stderr.txt')
        with open('stderr.txt', 'r') as f:
            stderr = f.read()
            # print(stderr)
            self.assertEqual(stderr, 'csv file on row 2 are not full\ncsv file on row 3 are not full\n')
    
    def test_exit_codes(self):
        csv_with_different_shape = ['Name,Index,Will continue\n', 'AlGeom,1,True\n', 'ModernCS,2.0,False\n', 'text, text\n']
        exit_code = lab1.transorm_from_csv_to_json(csv_with_different_shape)
        self.assertEqual(exit_code, 1)
        csv_with_different_shape = ['Name,Index,Will continue\n', 'AlGeom,1,True\n', 'ModernCS,2.0,False\n']
        exit_code = lab1.transorm_from_csv_to_json(csv_with_different_shape)
        self.assertEqual(exit_code, 0)
    
    def test_to_100_coverage(self):
        csv_with_different_shape = ['Name,Index,Will continue\n', 'AlGeom,1,True\n', 'ModernCS,2.0,False\n']
        exit_code = lab1.transorm_from_csv_to_json(csv_with_different_shape, absolute_false=True)
        self.assertEqual(exit_code, 0)
    
    """
    + тест на перевірку обробки валідних даних з stdin
    + тест на перевірку обробки невалідних даних з stdin
    + тест, коли stdin порожній
    + тести на перевірку даних з args (файл з валідними даними, файл з невалідними даними)
    + тест, коли переданого файлу не існує
    + тест, коли файл порожній
    + тест, який перевіряє, що помилки пишуться саме в stderr
    + тести на exit codes окремо
    """


if __name__ == '__main__':
    unittest.main()
