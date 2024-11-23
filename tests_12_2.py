import unittest
import runner_1 as rr


class TournamentTest(unittest.TestCase):
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run1 = rr.Runner('Усэйн', 10)
        self.run2 = rr.Runner('Андрей', 9)
        self.run3 = rr.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for testkey, testval in cls.all_results.items():
            print(f'TEST: {testkey}')
            for key, val in testval.items():
                result[key] = str(val.name)
            print(result)

    def testrun_1(self):
        run_1 = rr.Tournament(90, self.run1, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run1} и {self.run3}'] = finish

    def testrun_2(self):
        run_1 = rr.Tournament(90, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run2} и {self.run3}'] = finish

    def testrun_3(self):
        run_1 = rr.Tournament(90, self.run1, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run1}, {self.run2} и {self.run3}'] = finish


if __name__ == "__main__":
    unittest.main()