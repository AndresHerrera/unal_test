import json
from landsatxplore.api import API

username = "USERNAME"
password = "PASSWORD"
# Initialize a new API instance and get an access key
api = API(username, password)

# Search for Landsat TM scenes
scenes = api.search(
    dataset='landsat_8_c1',
    latitude=1.8035,
    longitude=-78.6298,
    start_date='2010-01-01',
    end_date='2022-01-31',
    max_cloud_cover=20
)

print(f"{len(scenes)} scenes found.")

# Process the result
for scene in scenes:
    print(scene['acquisition_date'].strftime('%Y-%m-%d'))
    print(scene['landsat_product_id'])
    # Write scene footprints to disk
    fname = f"{scene['landsat_product_id']}.geojson"
    with open(fname, "w") as f:
        json.dump(scene['spatial_coverage'].__geo_interface__, f)

api.logout()