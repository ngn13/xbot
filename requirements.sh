#!/bin/bash -e

check_hash() {
  if ! echo "$2 $1" | sha256sum -c > /dev/null; then
    echo "Hash verification for $1 failed!"
    exit 1
  fi
  echo "Hash verification success!"
}

VERSION="1.8.4"
HASH="b60c0aad83e1452a1646aef2b7e223cb66cb9a9cae52aaafb3d4ac9f46688580"

echo ">> Downloading slixmpp"
wget https://codeberg.org/poezio/slixmpp/archive/slix-$VERSION.tar.gz
echo ">> Extracting slixmpp"
tar xf slix-$VERSION.tar.gz

cd slixmpp
  echo ">> Installing slixmpp"
  python3 setup.py install
cd ..

rm -rf slixmpp slix-$VERSION.tar.gz

echo ">> Installing requests"
pip3 install requests

echo ">> Installed all the requirements"
