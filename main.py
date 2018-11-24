import NAS_settings
import NAS_ubuntu
import NAS_helper
import NAS_raspbian
import NAS_arch

NAS_settings.init()

NAS_ubuntu.seed_ubuntu()
NAS_raspbian.seed_raspbian()
NAS_arch.seed_arch()