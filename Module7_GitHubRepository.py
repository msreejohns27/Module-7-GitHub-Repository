import unittest


class SmartLight:
    def __init__(self, name):
        self.name = name
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True
        if self.brightness == 0:
            self.brightness = 100
        print(f'{self.name} is now ON at {self.brightness}% brightness.')

    def turn_off(self):
        self.is_on = False
        print(f'{self.name} is now OFF.')

    def set_brightness(self, level):
        if level < 0 or level > 100:
            print('Brightness must be between 0 and 100.')
            return
        self.brightness = level
        if level > 0:
            self.is_on = True
        else:
            self.is_on = False
        print(f'{self.name} brightness set to {self.brightness}%.')


# Create an object to test the class
living_room_light = SmartLight("Living Room Light")
living_room_light.turn_on()
living_room_light.set_brightness(50)
living_room_light.turn_off()
class TestSmartLight(unittest.TestCase):

    def setUp(self):
        self.light = SmartLight("Test Light")

    def test_initial_state(self):
        self.assertFalse(self.light.is_on)
        self.assertEqual(self.light.brightness, 0)

    def test_turn_on(self):
        self.light.turn_on()
        self.assertTrue(self.light.is_on)
        self.assertEqual(self.light.brightness, 100)

    def test_turn_off(self):
        self.light.turn_on()
        self.light.turn_off()
        self.assertFalse(self.light.is_on)

    def test_set_brightness_valid(self):
        self.light.set_brightness(75)
        self.assertEqual(self.light.brightness, 75)
        self.assertTrue(self.light.is_on)

    def test_set_brightness_zero_turns_off(self):
        self.light.set_brightness(0)
        self.assertFalse(self.light.is_on)

    def test_set_brightness_invalid(self):
        self.light.set_brightness(150)
        self.assertEqual(self.light.brightness, 0)  # unchanged since invalid


if __name__ == '__main__':
    unittest.main()