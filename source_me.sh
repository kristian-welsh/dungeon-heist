run() { python3 ./src; }
test() {
  coverage run -m unittest discover ./src/test
  coverage report
  coverage html
}
