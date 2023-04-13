RAIN_WATER_EFFICIENCY = 0.8   # Efficiency of rainwater use
IRRIGATION_EFFICIENCY = 0.7   # Efficiency of irrigation system
WATER_DENSITY = 1000          # Density of water in kg/m^3

# Input variables
crop_water_req = float(input("Enter the crop water requirement in mm: "))
rainfall = float(input("Enter the total rainfall in mm: "))
runoff = float(input("Enter the runoff in mm: "))
evaporation = float(input("Enter the evaporation losses in mm: "))
deep_perc = float(input("Enter the deep percolation losses in mm: "))
soil_water_content = float(input("Enter the soil water content in mm: "))
soil_texture = input("Enter the soil texture (options: 'sand', 'loam', 'clay'): ")

# Soil water holding capacity based on soil texture
if soil_texture == 'sand':
    soil_water_capacity = 100   # Water holding capacity of sand soil in mm/m
elif soil_texture == 'loam':
    soil_water_capacity = 200   # Water holding capacity of loam soil in mm/m
elif soil_texture == 'clay':
    soil_water_capacity = 300   # Water holding capacity of clay soil in mm/m

# Effective rainfall
effective_rainfall = (rainfall - runoff - evaporation - deep_perc) * RAIN_WATER_EFFICIENCY

# Irrigation water requirement
irrigation_water_req = ((crop_water_req - soil_water_content - effective_rainfall) / IRRIGATION_EFFICIENCY) / WATER_DENSITY

print('The irrigation water requirement is', round(irrigation_water_req, 2), 'm³.')

