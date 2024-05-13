#!/bin/bash -e

check_hash() {
  if ! echo "$2 $1" | sha256sum -c > /dev/null; then
    echo "Hash verification for $1 failed!"
    exit 1
  fi
  echo "Hash verification success!"
}

pip_depends="setuptools requests"

for d in $pip_depends; do
  echo ">> Installing $d (pip)"
  pip install $d
done

SLIX_VERSION="1.8.4"
SLIX_HASH="b60c0aad83e1452a1646aef2b7e223cb66cb9a9cae52aaafb3d4ac9f46688580"

echo ">> Downloading slixmpp"
wget -q --show-progress "https://codeberg.org/poezio/slixmpp/archive/slix-$SLIX_VERSION.tar.gz"
check_hash "slix-$SLIX_VERSION.tar.gz" "$SLIX_HASH"

echo ">> Extracting slixmpp"
tar xf "slix-$SLIX_VERSION.tar.gz"

pushd slixmpp
  echo ">> Installing slixmpp"
  python3 setup.py install
popd

rm -rf "slixmpp" *.tar.gz*
echo ">> Installed all the requirements"
