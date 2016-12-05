# Read in LAPD csv

import pandas as pd
import sklearn.cluster
import numpy
import csv

# 14 columns/lists
# only want DATE OCC, TIME OCC, AREA, RD, Crm Cd, Location 1
# 6 lists
# groups = dict(a=headers, b=)

dateocc = []
timeocc = []
area = []
rd = []
crmcd = []
location = []

def readCSV(filename):
	# with open(filename, 'rb') as csvfile:
	# 	csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	# 	for row in csvreader:
			# print ' '.join(row)

	df = pd.read_csv(filename)
	dateocc = df['DATE OCC'].astype(str).str[:-12]
	timeocc = df['TIME OCC']
	area = df['AREA']
	rd = df['RD']
	crmcd = df['Crm Cd']
	location = df['Location 1']
	
	# return json.loads(response.read())
	# https://data.lacity.org/api/views/azy9-n2gp/rows.csv?accessType=DOWNLOAD, https://data.lacity.org/A-Safe-City/LAPD-Crime-and-Collision-Raw-Data-for-2014/azy9-n2gp

# def readCSVurl(url):
# 	response = urllib2.urlopen(url)
# 	return csv.reader(response.read())

# def getNeighborhoods():
# 	dict = {}
# 	filename ='la-county-neighborhoods-current.geojson' 

# 	with open(filename) as json_data:
# 		js = json.load(json_data)
# 		# json_data.close()
# 		for neighborhood in js['features']:
# 			dict[neighborhood['properties']['name']] = neighborhood["geometry"]
# 			neighborhood_names.append((neighborhood['properties']['name']).encode("utf-8"))
# 		return js, dict

# csv14 = readCSVurl('https://data.lacity.org/A-Safe-City/LAPD-Crime-and-Collision-Raw-Data-for-2014/azy9-n2gp') 

# for row in csv14:
# 	print row[0]
# 	print row[1]
readCSV("LAPD_Crime_and_Collision_Raw_Data_for_2014.csv")
print location
# parsedjs, neighborhoods = getNeighborhoods()

# print "Bikelanes: "
# print bikelanes



# def coord_to_neighborhood(coordinates):
# 	# coord = coordinates[0]
# 	# for coord in coordinates:
# 	point = Point(coordinates)
# 	for neighborhood in parsedjs['features']:
# 		polygon = shape(neighborhood['geometry'])
# 		if polygon.contains(point):
# 			# print 'Found ', coordinates,' in neighborhood: ', (neighborhood['properties']['name']).encode("utf-8")
# 			return (neighborhood['properties']['name']).encode("utf-8")


# def classifyBikelanes():
# 	for bikelane in bikelanes:
# 		print
# 		# print 'BIKELANE: ', bikelane['the_geom']['coordinates']
# 		list_of_coords = bikelane['the_geom']['coordinates']
# 		# print 'List of Coordinates: ', list_of_coords
# 		list_of_neigh = []
# 		for coordinate in list_of_coords:
# 			for coord in coordinate:
# 			# list_of_coords = [x[i] for x in list_of_coords]
# 				# print 'Coordinate: ', coord
# 				neigh = coord_to_neighborhood(coord)
# 				if neigh not in list_of_neigh:
# 					list_of_neigh.append(neigh)
# 		# print 'This bikelane goes through: ', list_of_neigh
# 		classified.append(list_of_neigh)
# 	return classified


# classified = classifyBikelanes()

# classified_file = open('classified_routes.txt', 'wt')

# Save the classified array of neighborhoods into a file
# with open('crimecollision2014.csv', 'wb') as f:
# 	writer = csv.writer(f)
# 	writer.writerows(classified)

# print open('./LAPD_Crime_and_Collision_Raw_Data_for_2014.csv', 'rt').read()


