# REMOVE SNAP

# Stop snapd services
sudo systemctl stop snapd && sudo systemctl disable snapd

# Purge snapd
sudo apt purge -y snapd gnome-software-plugin-snap

# Remove no longer needed folders
rm -rf ~/snap
sudo rm -rf /snap /var/snap /var/lib/snapd /var/cache/snapd /usr/lib/snapd

# Prevent reinstall
sudo apt-mark hold snap snapd
cat <<EOF | sudo tee /etc/apt/preferences.d/snapd
Package: snapd
Pin: origin *
Pin-Priority: -1
EOF


# INSTALL FLATPAK

# To install Flatpak on Ubuntu 18.10 (Cosmic Cuttlefish) or later, simply run:
sudo apt install flatpak

# With older Ubuntu versions:
sudo add-apt-repository ppa:flatpak/stable
sudo apt update
sudo apt install flatpak

# Install the Software Flatpak plugin
sudo apt install gnome-software-plugin-flatpak

# Add the Flathub repository
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo





















