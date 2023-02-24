#oppong Ameyaw clifford
6944721
#list of available cars and their prices
cars={"Land rover":120000, "Toyota Corolla":50000, "Tesla":510000,
      "Ford":105000, "kia":45600000, "Lamborghini":550000,
      "BMW":152100, "Ferrari":580990, "Jaguar":310500, 
      "Cadillac":121000, "Honda":80000, "Chevrolet":438000,
      "Jeep":109350, "Bugatti":317500, "Dodge":435089,
      "Kia":30100, "Peugot":100990, "Mazda":66500,
      "Audi":251000, "GMC":189000, "Volvo":21900,
      "Acura":199350, "jeep":300501, "Hyundai":135089,
      "Genesis":311100, "Buick":190990, "Land Rover":660500,
      "Range Rover":651000, "Citroen":179000, "Optima":20900}
car_name=input("Input car_name: ")
if car_name in cars:
    print("Available here")
    car_price=cars[car_name]
    print(f"The price of {car_name} is GHS{car_price}.")
else:
    print(f"Sorry,{car_name} is not available at the moment.")