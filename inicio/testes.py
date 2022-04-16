import unittest

from Atividades import comer, dormir

class atividadestestes(unittest.TestCase):

    def test_comer(self):
        self.assertEqual(
            comer('qiabo', True),
            'Estou comendo quiabo pq e saudavel'
        )

        self.assertEqual(
            comer(comida= 'pizza',eh_saudavel=False),
            'Estou comendo pizza pq fodase'
        )

if __name__ == '__main__':
    unittest.main()

