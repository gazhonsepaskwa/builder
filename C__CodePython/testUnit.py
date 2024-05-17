import unittest
from unittest.mock import patch
from Joueur import Joueur
from Case_vol import Case_vol

class TestCaseVol(unittest.TestCase):
    
    def setUp(self):
        self.joueur1 = Joueur()
        self.joueur2 = Joueur()

        self.joueur1.jetonsTractopelle = 0
        self.joueur2.jetonsTractopelle = 5
        
        self.joueur1.jetonsBateau = 0
        self.joueur2.jetonsBateau = 5
        
        self.joueur1.jetonsCamion = 0
        self.joueur2.jetonsCamion = 5
        
        self.joueur1.jetonsGrue = 0
        self.joueur2.jetonsGrue = 5

        self.case_vol = Case_vol(num=1, pos=(0, 0))
        
    def test_voler_tractopelle(self):
        with patch('builtins.input', side_effect=['2', '1']):
            self.case_vol.voler(self.joueur1, [self.joueur1, self.joueur2])
            
            self.assertEqual(self.joueur1.jetonsTractopelle, 1)
            self.assertEqual(self.joueur2.jetonsTractopelle, 4)
            
    def test_voler_bateau(self):
        with patch('builtins.input', side_effect=['2', '2']):
            self.case_vol.voler(self.joueur1, [self.joueur1, self.joueur2])
            
            self.assertEqual(self.joueur1.jetonsBateau, 1)
            self.assertEqual(self.joueur2.jetonsBateau, 4)
            
    def test_voler_camion(self):
        with patch('builtins.input', side_effect=['2', '3']):
            self.case_vol.voler(self.joueur1, [self.joueur1, self.joueur2])
            
            self.assertEqual(self.joueur1.jetonsCamion, 1)
            self.assertEqual(self.joueur2.jetonsCamion, 4)
            
    def test_voler_grue(self):
        with patch('builtins.input', side_effect=['2', '4']):
            self.case_vol.voler(self.joueur1, [self.joueur1, self.joueur2])
            
            self.assertEqual(self.joueur1.jetonsGrue, 1)
            self.assertEqual(self.joueur2.jetonsGrue, 4)
    
if __name__ == '__main__':
    unittest.main(exit=False)
