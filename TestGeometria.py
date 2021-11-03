import unittest
from model.Geometria import Geometria
from view.View import View
import random

class testGeometria(unittest.TestCase):
    __a = 0
    __b = 0
    __c = 0
    __g = None

    @classmethod
    def setUpClass(cls):
        print('setUpClass() -> OK')
        # genera numeros aleatorios para probar casa caso
        cls.a = round(random.uniform(0, 100), 2)
        cls.b = round(random.uniform(0, 100), 2)
        cls.c = round(random.uniform(0, 100), 2)
        cls.g = Geometria(cls.a, cls.b, cls.c)

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass() -> OK')
        cls.a = 0
        cls.b = 0
        cls.c = 0

    def setUp(self):
        print('setUp() -> OK')


    def test_areaCuadrado(self):

        print(self.a)
        result = self.g.areaCuadrado(self.a)
        self.assertEqual(result,self.a*self.a)
        print(f"{result} = {self.a*self.a}")

    def test_areaCirculo(self):
        PI = 3.1416
        result = self.g.areaCirculo(self.a)
        self.assertEqual(result, PI * pow(self.a, 2))

    def test_areaTiangulo(self):
        result = self.g.areaTiangulo(self.a , self.b)
        self.assertEqual(result, (self.a * self.b) / 2)

    def test_areaRectangulo(self):
        result = self.g.areaRectangulo(self.a,self.b)
        self.assertEqual(result,self.a*self.b)



    def test_areaPentagono(self ):
        result = self.g.areaPentagono(self.a,self.b)
        self.assertEqual(result,(self.a * self.b)/2)

    def test_areaRombo(self):
        result = self.g.areaRombo(self.a,self.b)
        self.assertEqual(result, (self.a * self.b)/2)

    def test_areaRomboide(self):
        result = self.g.areaRomboide( self.a, self.b)
        self.assertEqual(result,self.a*self.b)


    def test_areaTrapecio(self):
        result = self.g.areaTrapecio(self.a, self.b,self.c)
        self.assertEqual(result,((self.a + self.b)/2)*self.c)

    def tearDown(self):
        print('tearDown() -> OK')

    def test_set_figuraName(self):
        case = random.randint(1,9)

        figura = ""

        if case == 1:
            figura = "Cuadrado"
        elif case == 2:
            figura = "Circulo"
        elif case == 3:
            figura = "Tiangulo"
        elif case == 4:
            figura = "Rectangulo"
        elif case == 5:
            figura = "Pentagono"
        elif case == 6:
            figura = "Rombo"
        elif case == 7:
            figura = "Romboide"
        elif case == 8:
            figura = "Trapecio"

        self.g.set_figuraName(case)
        result = self.g.figuraName
        self.assertEqual(figura,result)

    def test_switch(self):
        case = random.randint(1, 9)
        sw = {
            1: self.g.areaCuadrado(self.a),
            2: self.g.areaCirculo(self.a),
            3: self.g.areaTiangulo(self.a, self.b),
            4: self.g.areaRectangulo(self.a, self.b),
            5: self.g.areaPentagono(self.a, self.b),
            6: self.g.areaRombo(self.a, self.b),
            7: self.g.areaRomboide(self.a, self.b),
            8: self.g.areaTrapecio(self.a, self.b, self.c)
        }

        result = {
            1: self.a * self.a,
            2: 3.1416 * pow(self.a, 2),
            3: self.a*self.b/2,
            4: self.a*self.b,
            5: (self.a * self.b)/2,
            6: (self.a * self.b)/2,
            7: self.a*self.b,
            8: ((self.a + self.b)/2)*self.c
        }

        self.assertEqual(sw.get(case),result.get(case))


if __name__ == '__main__':
    unittest.main()
