from landsatxplore.earthexplorer import EarthExplorer

username = "USERNAME"
password = "PASSWORD"

ee = EarthExplorer(username, password)

ee.download('LC08_L1GT_010059_20211017_20211026_01_T2', output_dir='./data')

ee.logout()