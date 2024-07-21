from pyinaturalist import *

def get_all_species_observations(taxon_name):
	try:
		response = get_observations(taxon_name=taxon_name)
		species_data = []
		for obs in response['results']:
			species_data.append({
				'id': obs['id'],
				'taxon': obs['taxon']['name'],
				'observed_on': obs['observed_on'],
				'location': obs['place_guess'],
				'latitude': obs['geojson']['coordinates'][1],
				'longitude': obs['geojson']['coordinates'][0]
			})
		return species_data
	except Exception as e:
		return f"Error: {e}"

if __name__ == '__main__':
	species_name = input("> ")
	#species = get_taxa_autocomplete(q=species_name)
	observations = get_all_species_observations(species_name)
	pprint(observations)
	for obs in observations:
		print(f"ID: {obs['id']} | Taxon: {obs['taxon']} | Observed on: {obs['observed_on']} | Location: {obs['location']} | Lat/Long: {obs['latitude']:.6f}, {obs['longitude']:.6f}")
