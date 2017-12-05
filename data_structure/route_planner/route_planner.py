from helpers import Map, load_map, show_map
from student_code import shortest_path

map_10 = load_map('map-10.pickle')
show_map(map_10)

map_10.intersections

# intersection 0 connects to intersections 7, 6, and 5
map_10.roads[0]

# full connectivity of the map
map_10.roads

map_40 = load_map('map-40.pickle')
show_map(map_40)

show_map(map_40, start=5, goal=34, path=[5,16,37,12,34])
