def convert_units(value, from_unit='meters', to_unit='feet', **nunits):
    units={'meters': 1, 'feet': 3.28084, 'inches': 39.3701, 'centimeters': 100, 'millimeters': 1000}
    units.update(nunits)

    return round(value * units[to_unit] / units[from_unit], 3)

# а далее в задании 9
if __name__ == "__main__": 
    print(convert_units(1, 'meters', 'feet'))
    print(convert_units(2, 'feet', 'centimeters'))
    print(convert_units(10, 'centimeters', 'millimeters'))
    print(convert_units(1, 'meters', 'yards', yards=1.09361))
    print(convert_units(50, 'filons', 'yards', yards=1.09361, filons=1.76))