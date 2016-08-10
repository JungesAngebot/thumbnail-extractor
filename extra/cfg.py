from commonspy.configuration import OverwriteableConfiguration

config = OverwriteableConfiguration.create_from_file('../config/config.json')

print(config.property('kaltura.ks'))
